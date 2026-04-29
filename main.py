import os
from src.file_manager.scanner import DirectoryScanner
from src.utils.excel_generator import ExcelGenerator
from src.ui.dashboard import GraderApp

def process_homework(root_folder, task_name):
    try:
        report_path = os.path.join(root_folder, "דוח_הגשות_כללי.xlsx")

        # סריקה לפי שם הקובץ
        scanner = DirectoryScanner(root_folder)
        tasks = scanner.get_student_tasks(task_name)

        if not tasks:
            return False

        # יצירת הדוח
        return ExcelGenerator.generate_report(tasks, task_name, report_path)

    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    app = GraderApp(process_homework)
    app.run()