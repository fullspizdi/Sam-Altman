import requests
from bs4 import BeautifulSoup
import os
import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {str(e)}")
        return None

def scrape_site(url, keyword, file_types, max_files, output_dir):
    html_content = fetch_html(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        resources = []
        for file_type in file_types:
            resources.extend(soup.find_all('a', href=True))
        
        saved_count = 0
        for resource in resources:
            if any(resource['href'].endswith(f".{ft}") for ft in file_types):
                if keyword.lower() in resource.text.lower():
                    if saved_count < max_files:
                        download_resource(resource['href'], output_dir)
                        saved_count += 1
                    else:
                        break

def download_resource(link, output_dir):
    try:
        response = requests.get(link)
        response.raise_for_status()
        file_name = link.split('/')[-1]
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Saved {file_name} to {output_dir}")
    except requests.RequestException as e:
        print(f"Failed to download {link}: {str(e)}")

def main():
    config = load_config()
    keyword = config['search_keyword']
    output_dir = config['output_directory']
    file_types = config['file_types']
    websites = config['websites_to_search']
    max_files = config['max_files_per_type']

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for website in websites:
        scrape_site(website, keyword, file_types, max_files, output_dir)

if __name__ == "__main__":
    main()
