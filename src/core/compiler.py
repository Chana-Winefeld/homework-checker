import subprocess
import os
from typing import Tuple


class JavaCompiler:
    @staticmethod
    def compile(java_file_path: str) -> Tuple[bool, str]:
        if not java_file_path or not os.path.exists(java_file_path):
            return False, "קובץ ה-Java לא נמצא."

        try:
            # מריצים את פקודת הקימפול של ג'אווה מאחורי הקלעים
            result = subprocess.run(
                ['javac', java_file_path],
                capture_output=True,
                text=True,
                timeout=10
            )

            # returncode 0 אומר שהפקודה הסתיימה בהצלחה ללא שגיאות
            if result.returncode == 0:
                return True, ""
            else:
                # אם יש שגיאה, נחזיר את טקסט השגיאה המדויק של Java
                return False, result.stderr

        except FileNotFoundError:
            return False, "שגיאה: פקודת 'javac' לא נמצאה. ודאי שמותקן JDK על המחשב ושמוגדר משתנה סביבה PATH."
        except subprocess.TimeoutExpired:
            return False, "שגיאה: תהליך הקימפול לקח יותר מדי זמן (Timeout)."
        except Exception as e:
            return False, f"שגיאה לא צפויה: {str(e)}"