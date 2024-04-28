import os
import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def filter_resources(output_dir, keyword):
    """
    Filters the downloaded resources to ensure they contain the keyword 'Sam Altman'.
    This function assumes that all files in the directory are text-based (e.g., HTML, TXT).
    """
    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if keyword.lower() not in content.lower():
                    os.remove(file_path)
                    print(f"Removed {filename} as it does not contain the keyword.")

def main():
    config = load_config()
    output_dir = config['output_directory']
    keyword = config['search_keyword']
    filter_resources(output_dir, keyword)

if __name__ == "__main__":
    main()
