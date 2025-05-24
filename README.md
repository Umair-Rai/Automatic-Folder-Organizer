# Automatic-Folder-Organizer
Automatically move files into folders based on file type.
# 🗂️ Folder Organizer App – Python Automation Project

A simple yet powerful Python script that **automatically organizes your files** into folders based on their file types (Images, Documents, Videos, Scripts, and Others).  
This is a beginner-level automation project using `os`, `shutil`, and `file extension matching` – perfect for learning real-world Python file handling.

---

## 📌 Features

- ✅ Automatically organizes all files into type-based folders
- 📁 Supports file types: `.jpg`, `.png`, `.pdf`, `.mp4`, `.docx`, `.txt`, `.py`, and more
- 💡 Creates folders if they don’t exist already
- 🛡️ Skips non-files (folders)
- 🧼 Moves unknown file types to a general `Others` folder

---

## 📂 Folder Structure (Before → After)
Downloads/
├── resume.pdf
├── image1.jpg
├── script.py
├── video.mp4
└── random.xyz



⬇️ Becomes:

Downloads/
├── Docs/
│ └── resume.pdf
├── Images/
│ └── image1.jpg
├── Scripts/
│ └── script.py
├── Videos/
│ └── video.mp4
└── Others/
└── random.xyz


---

## 🚀 How to Run

### 1. Clone the Repo or Download the Script
```bash
git clone https://github.com/Umair-Rai/Automatic-Folder-Organizer.git
cd Automatic-Folder-Organizer
