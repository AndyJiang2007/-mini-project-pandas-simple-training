from grade_analyzer.report import Report
from grade_analyzer.students import Students
import sys

def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python <main.py> <input.csv> <output.txt>")
        return 1
    stus = Students(sys.argv[1])
    repo = Report(stus)
    repo.write_report(sys.argv[2])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())