import os
import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def save_resource(content, file_name, output_dir):
    """
    Saves the content to a file in the specified output directory.
    """
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'wb') as file:
        file.write(content)
    print(f"Saved {file_name} to {output_dir}")

def setup_storage_directory(output_dir):
    """
    Ensures that the storage directory exists. If not, it creates the directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory {output_dir}")
    else:
        print(f"Directory {output_dir} already exists")

def main():
    config = load_config()
    output_dir = config['output_directory']
    setup_storage_directory(output_dir)

if __name__ == "__main__":
    main()
