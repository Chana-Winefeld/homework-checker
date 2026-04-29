import requests
import urllib3
import json
import time

# השתקת אזהרות נטפרי
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AIAnalyzer:
    def __init__(self, api_key: str):
        self.api_key = api_key
        # נסיגה למודל 1.5 פלאש - לעיתים קרובות יש לו מכסות פנויות יותר
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"

    def analyze_code(self, student_code: str, assignment_description: str):
        prompt = f"Analyze Java: {assignment_description}\nCode: {student_code}\nFormat: STATUS: [עבר/נכשל] FEEDBACK: [Hebrew]"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        headers = {"Content-Type": "application/json"}

        last_error = ""

        for attempt in range(3):
            try:
                # הוספת Connection: close עוזרת לעיתים בבעיות SSL של נטפרי
                response = requests.post(
                    self.url,
                    json=payload,
                    headers={"Connection": "close"},
                    verify=False,
                    timeout=45
                )

                if response.status_code == 200:
                    data = response.json()
                    text = data['candidates'][0]['content']['parts'][0]['text']
                    status = "עבר" if "STATUS: עבר" in text else "נכשל"
                    feedback = text.split("FEEDBACK:")[1].strip() if "FEEDBACK:" in text else text
                    return status, feedback

                last_error = f"שגיאת שרת {response.status_code}"
                if response.status_code == 429:
                    print(f"ניסיון {attempt + 1} נכשל בגלל עומס, מחכה 20 שניות...")
                    time.sleep(20)
                else:
                    break  # שגיאה אחרת (כמו 404 או 400) - אין טעם לנסות שוב

            except Exception as e:
                last_error = f"שגיאת תקשורת: {str(e)}"
                time.sleep(5)

        # אם הגענו לכאן, נכתוב לאקסל את השגיאה האחרונה שקרתה
        return "שגיאה", f"כישלון סופי: {last_error}"