import os
import zipfile
from datetime import datetime

def list_commits():
    # Determine the commits directory path
    script_dir = os.path.dirname(os.path.realpath(__file__))
    git_web_dir = os.path.join(script_dir, "..", ".git_web")
    commits_dir = os.path.join(git_web_dir, "commits")

    # List all commit directories and read their messages
    commit_ids = os.listdir(commits_dir)
    if commit_ids:
        print("Current Commits:")
        for commit_id in commit_ids:
            commit_message_file = os.path.join(commits_dir, commit_id, "commit_message.txt")
            if os.path.isfile(commit_message_file):
                with open(commit_message_file, "r") as f:
                    commit_info = f.read().strip()
                print(f"- Commit ID: {commit_id}\n  {commit_info}\n")
    else:
        print("No commits yet.")

def list_stashes():
    # Determine the stash directory path
    script_dir = os.path.dirname(os.path.realpath(__file__))
    git_web_dir = os.path.join(script_dir, "..", ".git_web")
    stash_dir = os.path.join(git_web_dir, "stash")

    # List all stash directories
    stash_ids = os.listdir(stash_dir)
    if stash_ids:
        print("\nCurrent Stashes:")
        for stash_id in stash_ids:
            print(f"- {stash_id}")
    else:
        print("\nNo stashes yet.")

def main_menu():
    print("\n[1] Push")
    print("[2] Add stashes to commit")
    print("[3] Detailed View")
    print("[4] Exit")

def detailed_view():
    choice = input("Enter commit ID for detailed view (or 'S' for stash): ").strip()
    if choice.lower() == 's':
        view_stash_details()
    else:
        view_commit_details(choice)

def view_commit_details(commit_id):
    # Determine the commits directory path
    script_dir = os.path.dirname(os.path.realpath(__file__))
    git_web_dir = os.path.join(script_dir, "..", ".git_web")
    commits_dir = os.path.join(git_web_dir, "commits")

    # Check if commit_id exists
    commit_dir = os.path.join(commits_dir, commit_id)
    if not os.path.exists(commit_dir):
        print(f"Commit ID '{commit_id}' does not exist.")
        return

    # Read commit message
    commit_message_file = os.path.join(commit_dir, "commit_message.txt")
    if os.path.isfile(commit_message_file):
        with open(commit_message_file, "r") as f:
            commit_info = f.read().strip()
        print(f"Commit ID: {commit_id}")
        print(commit_info)

    # List files in the commit zip
    commit_zip_file = os.path.join(commit_dir, f"{commit_id}.zip")
    if os.path.isfile(commit_zip_file):
        print("\nFiles:")
        with zipfile.ZipFile(commit_zip_file, "r") as zipf:
            for file_info in zipf.infolist():
                print(f"- {file_info.filename}")

def view_stash_details():
    # To be implemented based on your stash handling logic
    print("Stash details to be implemented.")

def status():
    list_commits()
    list_stashes()
    main_menu()

    while True:
        choice = input("\nEnter option: ").strip()
        
        if choice == '1':
            print("Pushing commits...")
            # Implement push logic here
        elif choice == '2':
            print("Adding stashes to commit...")
            # Implement add stashes to commit logic here
        elif choice == '3':
            detailed_view()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    status()

