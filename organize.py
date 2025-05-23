import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

 
load_dotenv()

def load_categories_from_env():
    categories = {}
    for key, value in os.environ.items():
        categories[key.capitalize()] = [ext.strip().lower() for ext in value.split(",") if ext]
    return categories

def get_category(extension, categories):
    for category, extensions in categories.items():
        if extension in extensions:
            return category
    return 'Others'

def organize_folder(folder_path, categories):
    folder = Path(folder_path)
    if not folder.exists() or not folder.is_dir():
        print("Invalid folder path.")
        return

    moved=0
    others_folder= folder / 'Others'# create 'Others' folder if it doesn't exist
    if  others_folder.exists():
        #check for files in Others folder for updated categories 
        #assuming only new categories are added
        for item in others_folder.iterdir():
            if item.is_file():
                ext = item.suffix.lower()
                category = get_category(ext, categories)
                if category != 'Others':
                    # move the file to the target folder
                    destination = folder / category / item.name
                    counter = 1
                    # handling duplicate file names
                    while destination.exists():
                        destination = folder / category / f"{item.stem}_{counter}{item.suffix}"
                        counter += 1
                    shutil.move(str(item), str(destination))
                    moved+=1
                    print(f"Moved: {item.name} → {category}/")

    for item in folder.iterdir():
        if item.is_file():
            
            ext = item.suffix.lower()
            category = get_category(ext, categories)
            target_folder = folder / category
            target_folder.mkdir(exist_ok=True)# create new folder if it doesn't exist

            destination = target_folder / item.name
            counter = 1
            # handling duplicate file names
            while destination.exists():
                destination = target_folder / f"{item.stem}_{counter}{item.suffix}"
                counter += 1
            # move the file to the target folder
            shutil.move(str(item), str(destination))
            moved+=1
            print(f"Moved: {item.name} → {category}/")
    print(f"Total files moved: {moved}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Organize files in a folder by type (extensions from .env).")
    parser.add_argument("path", help="Path to the folder to organize.")
    args = parser.parse_args()

    file_categories = load_categories_from_env()
    organize_folder(args.path, file_categories)

if __name__ == "__main__":
    main()