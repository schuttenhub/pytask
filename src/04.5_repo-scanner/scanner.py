import sys
import subprocess
import os

def clone_repo(repo_url, directory):
    """Clone the repository into the specified directory."""
    subprocess.run(['git', 'clone', repo_url, directory], check=True)

def main(file_path):
    # Create the directory if it doesn't exist
    base_dir = './repo_dir'
    os.makedirs(base_dir, exist_ok=True)
    
    # Open and read the file containing the repo URLs
    with open(file_path, 'r') as file:
        for line in file:
            repo_url = line.strip()
            if repo_url:
                repo_dir = os.path.join(base_dir, repo_url.split('/')[-1])
                print(f"Cloning {repo_url} into {repo_dir}...")
                clone_repo(repo_url, repo_dir)
                print("Clone completed.")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clone_repos.py <file_with_repo_urls>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
