import scrapy
import json
import os
import subprocess

class GithubUserReposSpider(scrapy.Spider):
    name = 'github_user_repos'
    user_name = 'your_github_username'  # Set the GitHub username here

    def start_requests(self):
        urls = [f'https://api.github.com/users/{self.user_name}/repos']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Parse the JSON response
        repos = json.loads(response.body_as_unicode())
        for repo in repos:
            repo_url = repo['clone_url']
            yield {
                'name': repo['name'],
                'clone_url': repo_url
            }
            self.clone_repo(repo_url)

    def clone_repo(self, repo_url):
        """Clone the repository into the specified directory."""
        base_dir = './repo_dir'
        os.makedirs(base_dir, exist_ok=True)
        repo_dir = os.path.join(base_dir, repo_url.split('/')[-1])
        subprocess.run(['git', 'clone', repo_url, repo_dir], check=True)

