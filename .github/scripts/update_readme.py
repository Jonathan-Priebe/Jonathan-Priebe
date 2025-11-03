#!/usr/bin/env python3
"""
Script to automatically update README.md with project descriptions from linked repositories.
"""

import re
import requests
import os

def get_readme_excerpt(repo_url, max_lines=5):
    """
    Fetches the README from a GitHub repository and returns an excerpt.
    
    Args:
        repo_url: Full GitHub repository URL (e.g., https://github.com/user/repo)
        max_lines: Maximum number of lines to extract from the README
    
    Returns:
        String containing the README excerpt
    """
    # Extract owner and repo name from URL
    match = re.search(r'github\.com/([^/]+)/([^/]+?)(?:\.git)?$', repo_url)
    if not match:
        return f"❌ Could not parse repository URL: {repo_url}"
    
    owner, repo = match.groups()
    
    # GitHub API endpoint for README
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    
    headers = {}
    github_token = os.getenv('GITHUB_TOKEN')
    if github_token:
        headers['Authorization'] = f'token {github_token}'
    
    try:
        # Get README content
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        # Get the download URL for the raw content
        download_url = response.json()['download_url']
        readme_response = requests.get(download_url)
        readme_response.raise_for_status()
        
        # Extract first few meaningful lines (skip title and empty lines)
        lines = readme_response.text.split('\n')
        excerpt_lines = []
        found_content = False
        
        for line in lines:
            # Skip the first title line and empty lines at the start
            if not found_content:
                if line.strip() and not line.strip().startswith('#'):
                    found_content = True
                elif line.strip().startswith('#'):
                    continue
                else:
                    continue
            
            # Add meaningful content
            if line.strip():
                excerpt_lines.append(line)
                if len(excerpt_lines) >= max_lines:
                    break
        
        excerpt = '\n'.join(excerpt_lines)
        return excerpt if excerpt else "No description available."
        
    except requests.exceptions.RequestException as e:
        return f"❌ Error fetching README: {str(e)}"

def update_readme():
    """
    Updates the README.md file with current project information.
    """
    readme_path = 'README.md'
    
    # Read current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define the pattern to find the projects section
    pattern = r'(## 🚀 Currently Working On\n\n)(<!-- PROJECT_START -->)(.*?)(<!-- PROJECT_END -->)'
    
    # Check if the pattern exists
    if not re.search(pattern, content, re.DOTALL):
        print("❌ Could not find project markers in README.md")
        print("Please ensure your README has <!-- PROJECT_START --> and <!-- PROJECT_END --> markers")
        return
    
    # Extract repository URL from the content between markers
    match = re.search(pattern, content, re.DOTALL)
    if match:
        project_section = match.group(3)
        
        # Find repository URL
        repo_match = re.search(r'\[View Repository\]\((https://github\.com/[^)]+)\)', project_section)
        if repo_match:
            repo_url = repo_match.group(1)
            print(f"📥 Fetching README from: {repo_url}")
            
            # Extract repo name and description from URL pattern
            repo_name_match = re.search(r'github\.com/[^/]+/([^/]+)', repo_url)
            repo_name = repo_name_match.group(1) if repo_name_match else "Project"
            
            # Get README excerpt
            excerpt = get_readme_excerpt(repo_url, max_lines=2)
            
            # Build new project section
            new_project_section = f'''### 🎮 {repo_name}

> {excerpt}

📁 [View Repository]({repo_url})
'''
            
            # Replace the content between markers
            new_content = re.sub(
                pattern,
                rf'\1\2\n{new_project_section}\n\4',
                content,
                flags=re.DOTALL
            )
            
            # Write updated content
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ README.md updated successfully!")
        else:
            print("❌ Could not find repository URL in project section")
    else:
        print("❌ Could not parse project section")

if __name__ == '__main__':
    update_readme()
