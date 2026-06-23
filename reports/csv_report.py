import csv

def export_csv(bugs, filename="output/report.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "File",
            "Rule ID",
            "Line",
            "Severity",
            "Issue"
        ])

        for bug in bugs:
            writer.writerow([
                bug["file"],
                bug["id"],
                bug["line"],
                bug["severity"],
                bug["issue"]
            ])