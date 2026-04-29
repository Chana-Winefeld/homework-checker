import pandas as pd
import os
import tkinter.messagebox as messagebox


class ExcelGenerator:
    @staticmethod
    def generate_report(tasks, target_date: str, output_path: str):
        # מנקה רווחים מהשמות למניעת תקלות זיהוי
        current_results = {str(task.student_name).strip(): ("V" if task.java_file_path else "X") for task in tasks}

        try:
            if os.path.exists(output_path):
                # קריאת הקובץ - עמודה 0 (השמות) היא טקסט נקי לחלוטין
                df = pd.read_excel(output_path, index_col=0)

                # בדיקה והוספת תלמידים חדשים מבלי לדרוס ישנים
                for student in current_results.keys():
                    if student not in df.index:
                        df.loc[student] = "---"
            else:
                # יצירת טבלה חדשה
                df = pd.DataFrame(index=list(current_results.keys()))
                df.index.name = "שם התלמיד"

            # הוספת התרגיל החדש בלבד ושמירת ההיסטוריה
            df[target_date] = df.index.map(current_results).fillna("X")

            # כתיבה לאקסל
            writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
            df.to_excel(writer, sheet_name='מעקב הגשות')
            workbook = writer.book
            worksheet = writer.sheets['מעקב הגשות']

            # עיצובים
            header_fmt = workbook.add_format({'bold': True, 'bg_color': '#D7E4BC', 'border': 1, 'align': 'center'})
            cell_fmt = workbook.add_format({'border': 1, 'align': 'center'})
            green_fmt = workbook.add_format(
                {'bg_color': '#C6EFCE', 'font_color': '#006100', 'border': 1, 'align': 'center'})
            red_fmt = workbook.add_format(
                {'bg_color': '#FFC7CE', 'font_color': '#9C0006', 'border': 1, 'align': 'center'})

            # רוחב עמודות
            worksheet.set_column(0, 0, 25)  # שם התלמיד
            worksheet.set_column(1, 50, 12)  # תרגילים (t1, t2...)

            # עיצוב כותרות
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num + 1, value, header_fmt)
            worksheet.write(0, 0, df.index.name, header_fmt)

            # עיצוב תאי השמות (כדי שיהיו עם מסגרת ויישור לאמצע)
            for row_num, student_name in enumerate(df.index):
                worksheet.write(row_num + 1, 0, str(student_name), cell_fmt)

            # צביעת V ו-X מתחילה מעמודה B (אינדקס 1) והלאה
            worksheet.conditional_format(1, 1, len(df), len(df.columns), {
                'type': 'cell', 'criteria': 'equal to', 'value': '"V"', 'format': green_fmt
            })
            worksheet.conditional_format(1, 1, len(df), len(df.columns), {
                'type': 'cell', 'criteria': 'equal to', 'value': '"X"', 'format': red_fmt
            })

            writer.close()
            return True

        except PermissionError:
            messagebox.showerror("קובץ פתוח", "קובץ האקסל פתוח. סגרי אותו וניסי שוב.")
            return False
        except Exception as e:
            messagebox.showerror("שגיאה", f"תקלה בעדכון: {str(e)}")
            return False