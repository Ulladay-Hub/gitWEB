import os

def initialize_git_web_repo():
    # Determine the directory where this script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Create .git_web directory if it doesn't exist
    git_web_dir = os.path.join(script_dir, "..", ".git_web")
    if not os.path.exists(git_web_dir):
        os.makedirs(git_web_dir)
        print(f"Initialized empty GitWEB repository in {os.path.abspath(git_web_dir)}")
    else:
        print(f"Reinitialized existing GitWEB repository in {os.path.abspath(git_web_dir)}")

    # Create commits directory within .git_web if it doesn't exist
    commits_dir = os.path.join(git_web_dir, "commits")
    if not os.path.exists(commits_dir):
        os.makedirs(commits_dir)

if __name__ == "__main__":
    initialize_git_web_repo()
