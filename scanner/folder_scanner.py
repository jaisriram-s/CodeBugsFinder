import os
from scanner.bug_detector import scan_file
from scanner.todo_detector import detect_todo

def scan_folder(folder_path):
    all_bugs = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)

                print("Scanning:", filepath)

                bugs = scan_file(filepath)
                bugs.extend(detect_todo(filepath))

                for bug in bugs:
                    bug["file"] = filepath

                all_bugs.extend(bugs)

    return all_bugs