import os
from typing import List
from src.models.data_models import StudentTask


class DirectoryScanner:
    def __init__(self, root_path: str):
        self.root_path = root_path

    def get_student_tasks(self, task_name: str) -> List[StudentTask]:
        """
        סורק את תיקיות התלמידים ומחפש קובץ Java ספציפי בתוכן.
        """
        tasks = []
        if not os.path.exists(self.root_path):
            return tasks

        # וידוא ששם הקובץ מסתיים ב-.java
        filename_to_find = task_name if task_name.lower().endswith(".java") else f"{task_name}.java"

        for student_dir in os.listdir(self.root_path):
            student_path = os.path.join(self.root_path, student_dir)

            if os.path.isdir(student_path):
                # מחפשים את הקובץ ישירות בתוך תיקיית התלמיד
                potential_file_path = os.path.join(student_path, filename_to_find)

                # יצירת משימה - אם הקובץ קיים נשמור את הנתיב שלו, אם לא - None
                task = StudentTask(
                    student_name=student_dir,
                    folder_path=student_path,
                    java_file_path=potential_file_path if os.path.exists(potential_file_path) else None
                )
                tasks.append(task)
        return tasks