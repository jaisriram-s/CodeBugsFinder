import ast

class BugDetector(ast.NodeVisitor):
    def __init__(self):
        self.bugs = []

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                if "password" in target.id.lower():
                    if isinstance(node.value, ast.Constant):
                        self.bugs.append({
                            "id": "CBF001",
                            "line": node.lineno,
                            "severity": "HIGH",
                            "issue": "Hardcoded Password"
                        })
                if "api_key" in target.id.lower():
                    self.bugs.append({
                        "id": "CBF006",
                        "line": node.lineno,
                        "severity": "HIGH",
                        "issue": "Hardcoded API Key"
   
                          })

        self.generic_visit(node)

    def visit_While(self, node):
        if isinstance(node.test, ast.Constant):
            if node.test.value is True:
                self.bugs.append({
                    "id": "CBF002",
                    "line": node.lineno,
                    "severity": "HIGH",
                    "issue": "Possible Infinite Loop"
                })

        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id == "print":
                self.bugs.append({
                    "id": "CBF003",
                    "line": node.lineno,
                    "severity": "LOW",
                    "issue": "Debug Print Statement"
                })

        self.generic_visit(node)

    def visit_Try(self, node):
        for handler in node.handlers:
            if len(handler.body) == 1:
                if isinstance(handler.body[0], ast.Pass):
                    self.bugs.append({
                        "id": "CBF004",
                        "line": handler.lineno,
                        "severity": "MEDIUM",
                        "issue": "Empty Exception Handler"
                    })
        for handler in node.handlers:
            if handler.type is None:
                 self.bugs.append({
                      "id": "CBF007",
                      "line": handler.lineno,
                      "severity": "MEDIUM",
                      "issue": "Bare Exception Detected"
                 })

        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            if alias.name == "*":
                self.bugs.append({
                    "id": "CBF008",
                    "line": node.lineno,
                    "severity": "MEDIUM",
                    "issue": "Wildcard Import Detected"
            })

        self.generic_visit(node)


def scan_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        source = file.read()

    tree = ast.parse(source)

    detector = BugDetector()
    detector.visit(tree)

    return detector.bugs