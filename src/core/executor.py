import subprocess
import os
from typing import Tuple


class JavaExecutor:
    @staticmethod
    def run_and_check(java_file_path: str, input_data: str, expected_output: str) -> Tuple[bool, str]:
        # חילוץ שם הקלאס והתיקייה (למשל Main מתוך Main.java)
        working_dir = os.path.dirname(java_file_path)
        class_name = os.path.basename(java_file_path).replace(".java", "")

        try:
            # הרצת הקוד באמצעות פקודת java
            process = subprocess.run(
                ['java', '-cp', working_dir, class_name],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=5  # הגנה מפני לולאות אינסופיות של תלמידים
            )

            actual_output = process.stdout.strip()

            if process.returncode != 0:
                return False, f"שגיאת הרצה (Runtime Error): {process.stderr}"

            if actual_output == expected_output.strip():
                return True, "הפלט תקין!"
            else:
                return False, f"פלט שגוי. צפוי: '{expected_output}', התקבל: '{actual_output}'"

        except subprocess.TimeoutExpired:
            return False, "שגיאה: הקוד נתקע (ייתכן לולאה אינסופית)"
        except Exception as e:
            return False, f"שגיאה לא צפויה: {str(e)}"