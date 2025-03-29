import os
import subprocess
import argparse

# Define file extensions to count as code
CODE_EXTENSIONS = {
    ".c", ".cpp", ".h", ".hpp", ".py", ".js", ".ts", ".java",
    ".cs", ".go", ".rs", ".swift", ".php", ".html", ".css", ".odin",
    ".rb", ".swift", ".kt", ".m", ".mm", ".lua", ".sh", ".pl", ".r",
    ".dart", ".scala", ".hs", ".clj", ".groovy", ".vb", ".rs", ".tsx",
    ".coffee", ".ex", ".exs", ".jl"
}

def clone_or_update_repo(repo_url, repo_path):
    """Clones a GitHub repo if it doesn't exist, otherwise updates it."""
    if not os.path.exists(repo_path):
        print(f"Cloning repository into {repo_path}...")
        subprocess.run(["git", "clone", repo_url, repo_path], check=True)
    else:
        print(f"Updating repository in {repo_path}...")
        subprocess.run(["git", "-C", repo_path, "pull"], check=True)

def count_lines_in_repo(repo_path):
    """Counts lines of code in the given repository path."""
    total_lines = 0
    for root, _, files in os.walk(repo_path):
        for file in files:
            if any(file.endswith(ext) for ext in CODE_EXTENSIONS):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        line_count = sum(1 for _ in f)
                        total_lines += line_count
                except Exception as e:
                    print(f"Skipping {file_path} due to error: {e}")
    return total_lines

def main():
    parser = argparse.ArgumentParser(description="Count lines of code in a GitHub repository.")
    parser.add_argument("repo_url", help="GitHub repository URL")
    parser.add_argument("repo_path", help="Local path to clone/update the repository")
    
    args = parser.parse_args()

    clone_or_update_repo(args.repo_url, args.repo_path)
    total_lines = count_lines_in_repo(args.repo_path)

    print(f"Total lines of code in {args.repo_path}: {total_lines}")

if __name__ == "__main__":
    main()