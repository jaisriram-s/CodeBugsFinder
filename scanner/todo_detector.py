def detect_todo(filepath):
    bugs = []

    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line_no, line in enumerate(lines, start=1):
        if "TODO" in line.upper():
            bugs.append({
                "id": "CBF005",
                "line": line_no,
                "severity": "LOW",
                "issue": "TODO Comment Found"
            })

    return bugs