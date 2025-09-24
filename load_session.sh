#!/bin/bash

# Exit on any error
set -e

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SESSION_DIR="$SCRIPT_DIR/session"
SRC_DIR="$SCRIPT_DIR/src"
BACKUP_DIR="$SCRIPT_DIR/backup"

# Check if session directory exists
if [ ! -d "$SESSION_DIR" ]; then
    echo "Error: Session directory '$SESSION_DIR' does not exist."
    exit 1
fi

# Check if src directory exists
if [ ! -d "$SRC_DIR" ]; then
    echo "Error: Source directory '$SRC_DIR' does not exist."
    exit 1
fi

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Get available sessions
sessions=()
for dir in "$SESSION_DIR"/*; do
    if [ -d "$dir" ]; then
        session_num=$(basename "$dir")
        sessions+=("$session_num")
    fi
done

# Sort sessions numerically
IFS=$'\n' sessions=($(sort -n <<<"${sessions[*]}"))
unset IFS

# Check if any sessions exist
if [ ${#sessions[@]} -eq 0 ]; then
    echo "No sessions found in '$SESSION_DIR'."
    exit 1
fi

# Display available sessions
echo "What session would you like to load?"
echo
for i in "${!sessions[@]}"; do
    echo "$((i + 1)). Session ${sessions[i]}"
done
echo

# Get user choice
while true; do
    read -p "Enter your choice (1-${#sessions[@]}): " choice
    
    # Validate input
    if [[ "$choice" =~ ^[0-9]+$ ]] && [ "$choice" -ge 1 ] && [ "$choice" -le "${#sessions[@]}" ]; then
        selected_session="${sessions[$((choice - 1))]}"
        break
    else
        echo "Invalid choice. Please enter a number between 1 and ${#sessions[@]}."
    fi
done

echo
echo "Selected session: $selected_session"
echo

# Generate timestamp for backup filename
timestamp=$(date +"%Y-%m-%d-%I-%M-%S-%p" | tr '[:upper:]' '[:lower:]')
backup_filename="src-$timestamp.tar.gz"
backup_path="$BACKUP_DIR/$backup_filename"

# Create backup of current src directory
echo "Creating backup of current src directory..."
cd "$SCRIPT_DIR"
if [ "$(ls -A "$SRC_DIR" 2>/dev/null)" ]; then
    tar -czf "$backup_path" -C src .
    echo "Backup created: $backup_filename"
else
    echo "Source directory is empty, creating empty backup file..."
    touch "$backup_path"
fi

# Clear src directory, preserving .gitkeep
echo "Clearing src directory (preserving .gitkeep)..."
find "$SRC_DIR" -maxdepth 10 -not -name ".gitkeep" -not -name "." -not -name ".." -exec rm -rf {} + 2>/dev/null || true

# Copy session content to src directory
session_path="$SESSION_DIR/$selected_session"
echo "Loading session $selected_session..."

if [ "$(ls -A "$session_path" 2>/dev/null)" ]; then
    cp -r "$session_path"/* "$SRC_DIR"/ 2>/dev/null || true
    cp -r "$session_path"/.*[!.]* "$SRC_DIR"/ 2>/dev/null || true
    echo "Session $selected_session loaded successfully!"
else
    echo "Warning: Session $selected_session directory is empty."
fi

echo
echo "Operation completed!"
echo "- Backup saved to: backup/$backup_filename"
echo "- Session $selected_session loaded into src directory"