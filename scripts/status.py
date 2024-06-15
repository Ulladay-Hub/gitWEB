import os

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
    print("[3] Exit")

def status():
    list_commits()
    list_stashes()
    main_menu()

if __name__ == "__main__":
    status()
