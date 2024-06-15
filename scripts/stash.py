import os
import shutil
import uuid
import zipfile

def stash_changes():
    # Generate a unique stash ID
    stash_id = str(uuid.uuid4())[:8]

    # Determine the stash directory path
    script_dir = os.path.dirname(os.path.realpath(__file__))
    git_web_dir = os.path.join(script_dir, "..", ".git_web")
    stash_dir = os.path.join(git_web_dir, "stash")

    # Create stash directory if it doesn't exist
    if not os.path.exists(stash_dir):
        os.makedirs(stash_dir)

    # Create stash directory for this stash ID
    stash_id_dir = os.path.join(stash_dir, stash_id)
    os.makedirs(stash_id_dir)

    # Copy current directory contents to stash
    for root, _, files in os.walk(script_dir):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, script_dir)
            stash_file_path = os.path.join(stash_id_dir, rel_path)
            os.makedirs(os.path.dirname(stash_file_path), exist_ok=True)
            shutil.copy2(file_path, stash_file_path)

    print(f"Changes stashed with ID: {stash_id}")

if __name__ == "__main__":
    stash_changes()
