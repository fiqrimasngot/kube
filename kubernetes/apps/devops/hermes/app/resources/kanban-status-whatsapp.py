#!/usr/bin/env python3
"""Print new Kanban status changes for the WhatsApp cron job."""

from __future__ import annotations

import glob
import json
import sqlite3
from pathlib import Path

ROOT = Path("/opt/data")
STATE_PATH = ROOT / "cron" / "kanban-whatsapp-state.json"
EVENT_KINDS = {
    "archived",
    "assigned",
    "blocked",
    "changes_requested",
    "claimed",
    "completed",
    "crashed",
    "created",
    "gave_up",
    "promoted",
    "reopened_review",
    "review_requested",
    "scheduled",
    "specified",
    "timed_out",
    "unblocked",
}


def board_databases() -> list[Path]:
    paths = [ROOT / "kanban.db"]
    paths.extend(Path(path) for path in glob.glob(str(ROOT / "kanban" / "boards" / "*" / "kanban.db")))
    return sorted({path for path in paths if path.is_file()})


def board_name(path: Path) -> str:
    if path == ROOT / "kanban.db":
        return "default"
    return path.parent.name


def load_state() -> dict[str, int]:
    try:
        data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}
    return {str(key): int(value) for key, value in data.items()}


def save_state(state: dict[str, int]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = STATE_PATH.with_suffix(".tmp")
    temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(STATE_PATH)


def current_event_id(connection: sqlite3.Connection) -> int:
    row = connection.execute("SELECT COALESCE(MAX(id), 0) FROM task_events").fetchone()
    return int(row[0])


def read_changes(connection: sqlite3.Connection, after_id: int) -> list[sqlite3.Row]:
    placeholders = ",".join("?" for _ in EVENT_KINDS)
    return connection.execute(
        f"""
        SELECT e.id, e.task_id, e.kind, t.title, t.status, t.assignee
        FROM task_events AS e
        JOIN tasks AS t ON t.id = e.task_id
        WHERE e.id > ? AND e.kind IN ({placeholders})
        ORDER BY e.id
        """,
        (after_id, *sorted(EVENT_KINDS)),
    ).fetchall()


def main() -> None:
    state = load_state()
    changes: list[str] = []

    for database in board_databases():
        key = str(database)
        with sqlite3.connect(database) as connection:
            connection.row_factory = sqlite3.Row
            latest = current_event_id(connection)
            if key not in state:
                state[key] = latest
                continue
            for row in read_changes(connection, state[key]):
                assignee = row["assignee"] or "unassigned"
                changes.append(
                    f"[{board_name(database)}] {row['task_id']} {row['kind']}: "
                    f"{row['title']} | status={row['status']} | assignee={assignee}"
                )
            state[key] = latest

    save_state(state)
    if changes:
        print("Kanban update")
        print("\n".join(changes))


if __name__ == "__main__":
    main()
