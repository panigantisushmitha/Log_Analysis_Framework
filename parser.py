import re

class LogParser:

    pattern = re.compile(
        r"(\d{4}-\d{2}-\d{2})\s"
        r"(\d{2}:\d{2}:\d{2})\s"
        r"(INFO|WARNING|ERROR)\s"
        r"(.+)"
    )

    def parse(self, filepath):

        logs = []

        with open(filepath, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                match = self.pattern.match(line)

                if match:

                    logs.append({
                        "date": match.group(1),
                        "time": match.group(2),
                        "level": match.group(3),
                        "message": match.group(4)
                    })

        return logs