import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder doesn't exist.")
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Docs": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov"],
        "Scripts": [".py", ".js", ".ts"],
        "Others": []
    }

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            found = False
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    found = True
                    break
            if not found:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))

    print("Files organized successfully!")

# Enter the Folder Address you want to Organize 
organize_folder("C:\\Your Path")
