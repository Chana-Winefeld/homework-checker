# 📚 Homework Checker System

## 🚀 Overview
A smart Python automation tool designed to help teachers automatically verify Java homework submissions across multiple student directories and generate a structured Excel report.

This system eliminates manual checking and significantly improves grading efficiency.

---

## 🎯 Problem It Solves
Teachers often waste time manually searching for student submissions across folders.

This tool automates the entire process:
- Navigates through all student directories
- Checks if the required Java file exists
- Generates a clean Excel report with results

---

## ⚙️ How It Works
1. Teacher enters the exercise name to check
2. The system scans all student folders
3. For each student:
   - Searches for a `.java` file matching the exercise name
4. Generates an Excel file with results:
   - ✔ File exists
   - ✖ File missing

The Excel file is updated each run (no duplicates, always refreshed).

---

## 📁 Project Structure
homework-checker/
│
├── main.py # Main execution file
├── src/ # Core logic modules
├── requirements.txt # Dependencies
├── .gitignore
└── README.md

---

## 📊 Output Example

| Student Name | Exercise_1 |
|-------------|------------|
| David       | ✔          |
| Sarah       | ✖          |
| Noa         | ✔          |

---

## 🛠️ Technologies Used
- Python 🐍
- os / pathlib (file system traversal)
- Excel automation (openpyxl / pandas)
- Data handling & automation logic

---

## 💡 Key Features
- 🔍 Automatic directory scanning
- 📂 Multi-student support
- ☕ Java file validation
- 📊 Excel report generation
- 🔄 Overwrites previous results cleanly
- ⚡ Fast and scalable

---

## 🔮 Future Improvements
- GUI interface for teachers
- Support for multiple programming languages
- Web-based dashboard
- Cloud storage integration
- Automatic submission upload system

---

## 👩‍💻 Author
Developed by **Chana Winfeld**  
Software Engineering Student | Full Stack Developer

---

## ⭐ Why This Project Matters
This project demonstrates:
- File system automation
- Real-world problem solving
- Data processing pipelines
- Clean software architecture thinking

Perfect for academic and professional portfolio.