import requests
from bs4 import BeautifulSoup
import subprocess
import os

REPOSITORY_DIR = './repo_dir/'

def fetch_repositories(username):
    base_url = f"https://github.com/{username}?tab=repositories"
    repo_list = []

    while True:
        response = requests.get(base_url)
        if response.status_code != 200:
            print(f"Failed to retrieve data for {username}!")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        repos = soup.find_all('div', class_='d-inline-block mb-1')
        for repo in repos:
            repo_url = "https://github.com/" + repo.find('a')['href']
            repo_list.append(repo_url)

        next_page = soup.find('a', rel='next')
        if next_page:
            base_url = "https://github.com" + next_page['href']
        else:
            break

    return repo_list

def clone_repo(repo_url, directory):
    """Clone the repository into the specified directory."""
    subprocess.run(['git', 'clone', repo_url, directory], check=True)

def list_directories(base_dir):
    """Returns a list of all directories within a given base directory."""
    directories = []
    base_path = base_dir  # Ensures path starts with './'
    
    for entry in os.listdir(base_path):
        path = os.path.join(base_path, entry)
        if os.path.isdir(path):
            directories.append(path)
    
    return directories

def scan_with_bandit():
    print("Scanning with Bandit...")
    subprocess.run(['bandit', '-r', REPOSITORY_DIR, '-iii'], capture_output=False, text=True)

def scan_with_flake8():
    print("Scanning with Flake8...")
    # Add your Flake8 scanning logic here

def scan_with_pylint():
    print("Scanning with PyLint...")
    # Add your PyLint scanning logic here

def scan_with_all(repo_dir):
    print("Scanning with all tools...")
    scan_with_bandit(repo_dir)
    scan_with_flake8(repo_dir)
    scan_with_pylint(repo_dir)


def main():
    usernames_input = input("Enter GitHub usernames separated by space: ")
    usernames = usernames_input.split()
    base_dir = './repo_dir'
    os.makedirs(base_dir, exist_ok=True)
    for username in usernames:
        print(f"Fetching repositories for {username}...")
        repositories = fetch_repositories(username)
        if repositories:
            print(f"Cloning repositories for {username}...")
            for repo_url in repositories:
                if os.path.exists(os.path.join(base_dir, repo_url.split('/')[-1])):
                    print(f"Repository already exists. Skipping {repo_url}")
                else:
                    repo_dir = os.path.join(base_dir, repo_url.split('/')[-1])
                    print(f"Cloning {repo_url} into {repo_dir}...")
                    clone_repo(repo_url, repo_dir)
                    print("Clone completed.")
        else:
            print(f"No repositories found or error in fetching repositories for {username}.")
    
    all_repos = list_directories(base_dir)
    
    # Benutzer nach Tool fragen und ausführen
    print("Which Tool you want to use to scan the repositories?")
    print("1. Bandit")
    print("2. Flake8")
    print("3. PyLint")
    print("4. All")
    choice = input("Enter your choice (1-4): ")
    switcher = {
        '1': scan_with_bandit,
        '2': scan_with_flake8,
        '3': scan_with_pylint,
        '4': scan_with_all
    }
    func = switcher.get(choice, scan_with_all)
    func()

if __name__ == "__main__":
    main()