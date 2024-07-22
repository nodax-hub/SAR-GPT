class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self, results, filename="report.txt"):
        with open(filename, 'w') as f:
            for key, value in results.items():
                f.write(f"{key}: {value}\n")
