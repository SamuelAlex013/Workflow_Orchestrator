# ==============================================================================
# Step 2: Extract Raw Content
# ==============================================================================
#
# Description:
# This script performs the deep extraction of documentation and contextual
# knowledge. It reads the `nodes_manifest.json` file and, based on the source
# type, fetches the raw content for each entry.
# - For official nodes, it reads the local Markdown files from the cloned n8n-docs repo.
# - For community nodes, it clones their respective GitHub repos and extracts README.md.
# - Placeholders for forum and template scraping are included as per the blueprint.
#
# Output:
# A structured directory named `raw_data` containing the raw, unprocessed
# text content for each discovered item.
# ==============================================================================

import os
import json
from git import Repo, GitCommandError

# --- CONFIGURATION ---
MANIFEST_FILE = './backend/app/services/RAG/docs/nodes_manifest.json'
OUTPUT_DIR = './raw_data/'
COMMUNITY_REPOS_DIR = './temp/community_repos/'

# --- EXTRACTION LOGIC ---

def extract_official_node_content(node_entry, output_path):
    """Reads the content from a local markdown file for an official node."""
    try:
        with open(node_entry['markdownPath'], 'r', encoding='utf-8') as f:
            content = f.read()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"    -> ERROR reading {node_entry['markdownPath']}: {e}")
        return False

def extract_community_node_content(node_entry, output_path):
    """Clones a community repo and extracts its README.md file."""
    repo_url = node_entry['repositoryUrl']
    if not repo_url or not repo_url.startswith('https://github.com'):
        print(f"    -> SKIPPED: Invalid or missing GitHub repository URL.")
        return False
        
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    local_repo_path = os.path.join(COMMUNITY_REPOS_DIR, repo_name)

    try:
        if not os.path.exists(local_repo_path):
             print(f"    -> Cloning {repo_url}...")
             Repo.clone_from(repo_url, local_repo_path)
        else:
             print(f"    -> Repo exists, skipping clone.")
    except GitCommandError as e:
        print(f"    -> ERROR cloning {repo_url}: {e}")
        return False
        
    readme_path = os.path.join(local_repo_path, 'README.md')
    if not os.path.exists(readme_path):
        print(f"    -> SKIPPED: README.md not found in {repo_name}.")
        return False

    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"    -> ERROR reading {readme_path}: {e}")
        return False

# --- PLACEHOLDERS FOR ADVANCED SCRAPING ---
def scrape_forum_threads():
    """
    Placeholder for forum scraping logic as per Blueprint 3.1.
    This would involve using requests and BeautifulSoup4 to scrape
    community.n8n.io for problem-solution threads.
    """
    print("\nSkipping forum scraping (placeholder)...")
    return

def scrape_workflow_templates():
    """
    Placeholder for template scraping logic as per Blueprint 3.2.
    This would involve scraping n8n.io/workflows to extract the
    link between use-case descriptions and workflow JSON.
    """
    print("Skipping workflow template scraping (placeholder)...")
    return

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    if not os.path.exists(MANIFEST_FILE):
        print(f"FATAL: Manifest file '{MANIFEST_FILE}' not found. Please run 1_discover_nodes.py first.")
    else:
        with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
            manifest = json.load(f)

        print("=============================================")
        print("      n8n Universal Content Extraction     ")
        print("=============================================")
        
        # Process Official Nodes
        official_output_dir = os.path.join(OUTPUT_DIR, 'official')
        os.makedirs(official_output_dir, exist_ok=True)
        print("\nExtracting content for official nodes...")
        for node in manifest['official_nodes']:
            filename = os.path.basename(node['markdownPath'])
            output_file = os.path.join(official_output_dir, filename)
            print(f"  -> Processing: {node['nodeName']}")
            extract_official_node_content(node, output_file)
            
        # Process Community Nodes
        community_output_dir = os.path.join(OUTPUT_DIR, 'community')
        os.makedirs(community_output_dir, exist_ok=True)
        os.makedirs(COMMUNITY_REPOS_DIR, exist_ok=True)
        print("\nExtracting content for community nodes...")
        for node in manifest['community_nodes']:
            filename = node['packageName'] + '.md'
            output_file = os.path.join(community_output_dir, filename)
            print(f"  -> Processing: {node['packageName']}")
            extract_community_node_content(node, output_file)
            
        # Run placeholder scrapers
        scrape_forum_threads()
        scrape_workflow_templates()
        
        print(f"\nContent extraction complete. Raw data saved in '{OUTPUT_DIR}'.")
