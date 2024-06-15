import os
import uuid
import zipfile
from datetime import datetime

def create_commit(message, description):
    # Generate a unique commit ID
    commit_id = str(uuid.uuid4())[:8]

    # Determine the commits directory path
    script_dir = os.path.dirname(os.path.realpath(__file__))
    git_web_dir = os.path.join(script_dir, "..", ".git_web")
    commits_dir = os.path.join(git_web_dir, "commits")

    # Create commit directory
    commit_dir = os.path.join(commits_dir, commit_id)
    os.makedirs(commit_dir)

    # Create commit message file with timestamp
    commit_message_file = os.path.join(commit_dir, "commit_message.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(commit_message_file, "w") as f:
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Message: {message}\n")
        f.write(f"Description: {description}\n")

    # Create a zip file with current directory contents
    commit_zip_file = os.path.join(commit_dir, f"{commit_id}.zip")
    with zipfile.ZipFile(commit_zip_file, "w") as zipf:
        for root, _, files in os.walk(script_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, script_dir))

    print(f"Created commit {commit_id}")

if __name__ == "__main__":
    # Example usage: ask user for commit message and description
    message = input("Enter commit message: ")
    description = input("Enter commit description: ")
    create_commit(message, description)

