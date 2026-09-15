#!/bin/sh
# Stop hook: system notification when Claude has finished its turn and is waiting for the human.
# stdin — the event JSON (not needed), read it and throw it away so the pipe is not held.
cat >/dev/null 2>&1 || :
PROJECT="${CLAUDE_PROJECT_DIR:-$PWD}"
TITLE="Claude Code · $(basename "$PROJECT")"
MSG="Done, waiting for you"
if command -v osascript >/dev/null 2>&1; then
  osascript -e "display notification \"$MSG\" with title \"$TITLE\" sound name \"Glass\"" >/dev/null 2>&1
elif command -v notify-send >/dev/null 2>&1; then
  notify-send "$TITLE" "$MSG" >/dev/null 2>&1
fi
exit 0
