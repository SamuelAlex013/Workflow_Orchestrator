# ==============================================================================
# Step 1: Discover All n8n Nodes
# ==============================================================================
#
# Description:
# This script systematically discovers all official and community n8n nodes.
# - It queries the npm Registry API with multiple keywords to find all community packages.
# - It clones the official n8n-docs repository to parse the nav.yml sitemap,
#   identifying all official Core and App nodes.
#
# Output:
# A single `nodes_manifest.json` file containing a unified list of all
# discovered nodes, their source types, and URLs for the next extraction step.
# ==============================================================================

import os
import json
import requests
import yaml
from git import Repo, GitCommandError

# --- CONFIGURATION ---
NPM_KEYWORDS = [
    'n8n-community-node-package',
    'n8n-node',
    'n8n-nodes',
    'n8n.io-nodes',
]
NPM_SEARCH_URL = 'https://registry.npmjs.org/-/v1/search'
NPM_PACKAGE_URL = 'https://registry.npmjs.org/'
N8N_DOCS_REPO_URL = 'https://github.com/n8n-io/n8n-docs.git'
LOCAL_DOCS_REPO_PATH = './temp/n8n-docs'
OUTPUT_FILE = './backend/app/services/RAG/docs/nodes_manifest.json'

# --- PART 1: COMMUNITY NODE DISCOVERY ---

def query_npm(keyword, page=0, size=250):
    """Queries the npm registry API for a given keyword."""
    params = {'text': f'keywords:{keyword}', 'size': size, 'from': page * size}
    try:
        response = requests.get(NPM_SEARCH_URL, params=params, timeout=20)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error querying npm for '{keyword}': {e}")
        return None

def discover_community_nodes():
    """Finds all community nodes by querying npm with multiple keywords."""
    print("Starting community node discovery from npm...")
    unique_packages = set()
    for keyword in NPM_KEYWORDS:
        print(f"  -> Querying for keyword: '{keyword}'")
        page = 0
        while True:
            results = query_npm(keyword, page)
            if not results or not results.get('objects'):
                break
            for package in results['objects']:
                unique_packages.add(package['package']['name'])
            if len(results['objects']) < 250:
                break
            page += 1
    
    print(f"Found {len(unique_packages)} unique community packages.")
    
    community_nodes = []
    for name in sorted(list(unique_packages)):
        try:
            print(f"  -> Fetching details for: {name}")
            response = requests.get(f"{NPM_PACKAGE_URL}{name}", timeout=10)
            response.raise_for_status()
            package_data = response.json()
            latest_version = package_data.get('dist-tags', {}).get('latest', 'N/A')
            repo_info = package_data.get('versions', {}).get(latest_version, {}).get('repository', {})
            repo_url = repo_info.get('url', 'N/A')
            
            # Clean up git+https prefix
            if repo_url.startswith('git+'):
                repo_url = repo_url[4:]
            
            community_nodes.append({
                'packageName': name,
                'sourceType': 'community',
                'repositoryUrl': repo_url,
                'version': latest_version,
                'description': package_data.get('description', 'N/A'),
            })
        except requests.RequestException as e:
            print(f"    -> Could not fetch details for {name}: {e}")
            
    return community_nodes

# --- PART 2: OFFICIAL NODE DISCOVERY ---

def clone_or_pull_repo(repo_url, local_path):
    """Clones a repository if it doesn't exist, or pulls the latest changes."""
    if os.path.exists(local_path):
        print(f"Pulling latest changes for {local_path}...")
        try:
            repo = Repo(local_path)
            repo.remotes.origin.pull()
        except GitCommandError as e:
            print(f"Could not pull repo {local_path}: {e}")
    else:
        print(f"Cloning {repo_url} to {local_path}...")
        try:
            Repo.clone_from(repo_url, local_path)
        except GitCommandError as e:
            print(f"Could not clone repo {repo_url}: {e}")

def parse_nav_yml(nav_data, base_path=""):
    """Recursively parses the nav.yml file to build a flat list of documentation pages."""
    pages = []
    if isinstance(nav_data, list):
        for item in nav_data:
            pages.extend(parse_nav_yml(item, base_path))
    elif isinstance(nav_data, dict):
        for key, value in nav_data.items():
            if isinstance(value, str):
                if value.startswith('integrations/'):
                    pages.append({
                        'nodeName': key,
                        'sourceType': 'official',
                        'markdownPath': os.path.join(LOCAL_DOCS_REPO_PATH, 'docs', value)
                    })
            elif isinstance(value, list):
                pages.extend(parse_nav_yml(value, base_path))
    return pages

def discover_official_nodes():
    """Finds all official nodes by parsing the n8n-docs repository."""
    print("\nStarting official node discovery from n8n-docs repository...")
    clone_or_pull_repo(N8N_DOCS_REPO_URL, LOCAL_DOCS_REPO_PATH)
    
    nav_file_path = os.path.join(LOCAL_DOCS_REPO_PATH, 'nav.yml')
    if not os.path.exists(nav_file_path):
        print("FATAL: nav.yml not found in docs repository.")
        return []
        
    with open(nav_file_path, 'r', encoding='utf-8') as f:
        nav_data = yaml.safe_load(f)
        
    official_nodes = parse_nav_yml(nav_data)
    print(f"Found {len(official_nodes)} official node documentation pages.")
    return official_nodes

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    print("=============================================")
    print("      n8n Universal Knowledge Discovery      ")
    print("=============================================")
    
    community_nodes = discover_community_nodes()
    official_nodes = discover_official_nodes()
    
    master_manifest = {
        'official_nodes': official_nodes,
        'community_nodes': community_nodes,
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(master_manifest, f, indent=2)
        
    print(f"\nDiscovery complete. Master manifest saved to '{OUTPUT_FILE}'.")
