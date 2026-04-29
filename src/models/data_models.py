from dataclasses import dataclass
from typing import Optional

@dataclass
class TestResult:
    is_compiled: bool
    is_passed: bool
    error_message: Optional[str] = None
    student_output: Optional[str] = None

@dataclass
class StudentTask:
    student_name: str
    folder_path: str
    java_file_path: Optional[str] = None
    result: Optional[TestResult] = None
