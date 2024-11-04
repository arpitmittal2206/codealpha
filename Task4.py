# TASK 4 : TASK AUTOMATION WITH PYHTON SCRIPTS...

import os
import shutil

# Define file type categories and extensions
FILE_TYPES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

def organize_files(folder_path):
    # Check if the specified folder exists
    if not os.path.isdir(folder_path):
        print("The specified folder path does not exist.")
        return
    
    # Create folders for each file type category
    for category in FILE_TYPES.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Organize files into folders based on their extensions
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Only process files (ignore subfolders)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            
            # Check the file type and move to the corresponding folder
            for category, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(folder_path, category)
                    shutil.move(file_path, destination_folder)
                    print(f"Moved '{filename}' to '{category}' folder.")
                    break
            else:
                # For files with unknown extensions, move to an 'Others' folder
                other_folder = os.path.join(folder_path, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, other_folder)
                print(f"Moved '{filename}' to 'Others' folder.")
    
    print("File organization completed.")

# Prompt the user for the folder path to organize
folder_path = input("Enter the folder path to organize: ")
organize_files(folder_path)
