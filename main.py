import os
from scraper import scrape_site, load_config

def main():
    # Load configuration settings
    config = load_config()
    keyword = config['search_keyword']
    output_dir = config['output_directory']
    file_types = config['file_types']
    websites = config['websites_to_search']
    max_files = config['max_files_per_type']

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory {output_dir}")
    else:
        print(f"Directory {output_dir} already exists")

    # Scrape each website for resources containing the keyword
    for website in websites:
        scrape_site(website, keyword, file_types, max_files, output_dir)

if __name__ == "__main__":
    main()
