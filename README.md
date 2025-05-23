# 🗂️ File Organizer (Python)

A simple Python script to automatically organize files in a folder based on their file extensions. Categories and extensions are defined in a `.env` file for flexibility and easy updates.

---

## 🚀 Features

- Organizes files into subfolders like `Images`, `Documents`, `Videos`, etc.
- File categories are configurable via `.env`
- Automatically re-categorizes files from the `Others/` folder if the `.env` is updated
- Handles duplicate file names by appending a counter

---

## 📦 Requirements

- Python 3.6+
- `python-dotenv`

## Setup 
```
git clone  https://github.com/Sumvit/FileOrganizer.git
cd FileOrganizer

pip install -r requirements.txt
```
## Run 
```
python organize.py /path/to/your/folder

```
## Example output 
```
Moved: resume.pdf → Documents/
Moved: vacation.jpg → Images/
Moved: code.py → Code/
Moved: unknown.xyz → Others/
Total files moved: 4

```
# 📢 Install as a CLI Tool 
```
pip install .

```

## Run
```
organize-folder /path/to/your/folder
```
## To uninstall the CLI tool
```
pip uninstall file-organizer
```
