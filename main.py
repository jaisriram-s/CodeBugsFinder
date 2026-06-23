from scanner.folder_scanner import scan_folder

bugs = scan_folder("samples")

print("\n===== CodeBugFinder Report =====\n")

if not bugs:
    print("No bugs found.")
else:
    for bug in bugs:
        print(
            f"{bug['file']} | "
            F"{bug['id']} | "
            f"Line {bug['line']} | "
            f"{bug['severity']} | "
            f"{bug['issue']}"
        )
with open("output/report.txt", "w") as report:
    report.write("===== CodeBugFinder Report =====\n\n")

    for bug in bugs:
        report.write(
            f"Line {bug['line']} | "
            f"{bug['severity']} | "
            f"{bug['issue']}\n"
        )

print("\nReport saved to output/report.txt")
high = 0
medium = 0
low = 0

for bug in bugs:
    if bug["severity"] == "HIGH":
        high += 1
    elif bug["severity"] == "MEDIUM":
        medium += 1
    elif bug["severity"] == "LOW":
        low += 1

print("\n===== SUMMARY =====")
print(f"HIGH   : {high}")
print(f"MEDIUM : {medium}")
print(f"LOW    : {low}")
print(f"TOTAL  : {len(bugs)}")

from reports.csv_report import export_csv
export_csv(bugs)

print("CSV report saved to output/report.csv")
from reports.json_report import export_json

export_json(bugs)

print("JSON report saved to output/report.json")
