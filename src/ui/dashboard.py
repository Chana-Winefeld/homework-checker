import tkinter as tk
from tkinter import filedialog, messagebox
import threading


class GraderApp:
    def __init__(self, run_callback):
        self.root = tk.Tk()
        self.root.title("בודק הגשות תלמידים")
        self.root.geometry("600x500")
        self.run_callback = run_callback

        self.folder_path = tk.StringVar()
        self.task_name = tk.StringVar()
        self._build_ui()

    def _build_ui(self):
        # בחירת תיקייה
        tk.Label(self.root, text="1. בחרי תיקיית תלמידים ראשית:", font=("Arial", 10, "bold")).pack(pady=15)
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()
        tk.Entry(btn_frame, textvariable=self.folder_path, width=45).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="בחר...", command=self._browse_folder).pack(side=tk.LEFT)

        # הזנת שם המטלה
        tk.Label(self.root, text="2. איזה תרגיל לבדוק? (למשל: t1):", font=("Arial", 10, "bold")).pack(pady=15)
        tk.Entry(self.root, textvariable=self.task_name, width=25, justify='center', font=("Arial", 12)).pack()

        # כפתור הפעלה
        self.run_btn = tk.Button(self.root, text="בדוק הגשות ועדכן אקסל", command=self._on_click_run,
                                 bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), height=2, width=30)
        self.run_btn.pack(pady=40)

        self.status_label = tk.Label(self.root, text="מוכן", fg="gray")
        self.status_label.pack()

    def _browse_folder(self):
        path = filedialog.askdirectory()
        if path: self.folder_path.set(path)

    def _on_click_run(self):
        if not self.folder_path.get() or not self.task_name.get():
            messagebox.showwarning("חסר נתונים", "נא לבחור תיקייה ולהזין את שם התרגיל")
            return

        self.run_btn.config(state=tk.DISABLED)
        self.status_label.config(text="סורק הגשות... נא להמתין", fg="blue")

        thread = threading.Thread(target=self._execute)
        thread.start()

    def _execute(self):
        success = self.run_callback(self.folder_path.get(), self.task_name.get())

        def finish():
            self.run_btn.config(state=tk.NORMAL)
            if success:
                self.status_label.config(text="הבדיקה הסתיימה בהצלחה!", fg="green")
                messagebox.showinfo("סיום", "האקסל עודכן בהצלחה!")
            else:
                self.status_label.config(text="הבדיקה נכשלה", fg="red")

        self.root.after(0, finish)

    def run(self):
        self.root.mainloop()