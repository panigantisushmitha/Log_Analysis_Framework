from collections import Counter


class LogAnalyzer:

    def analyze(self, logs):

        level_count = Counter()

        messages = Counter()

        for log in logs:

            level_count[log["level"]] += 1

            messages[log["message"]] += 1

        return {
            "level_count": level_count,
            "messages": messages
        }