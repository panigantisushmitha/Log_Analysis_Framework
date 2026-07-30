from parser import LogParser
from analyzer import LogAnalyzer
from report_generator import ReportGenerator
from utils import load_config


def main():

    print("=" * 50)
    print("Configurable Log Analysis Framework")
    print("=" * 50)

    # Load configuration
    config = load_config("config/config.json")

    parser = LogParser()
    analyzer = LogAnalyzer()
    report = ReportGenerator()

    all_logs = []

    # Parse all log files
    for log_file in config["log_files"]:

        print(f"Reading: {log_file}")

        logs = parser.parse(log_file)

        all_logs.extend(logs)

    print(f"\nTotal Logs Parsed: {len(all_logs)}")

    # Analyze logs
    analysis = analyzer.analyze(all_logs)

    # Generate report
    report.generate(
        analysis,
        config["report_file"]
    )

    print("\nAnalysis Completed Successfully!")
    print(f"Report saved to: {config['report_file']}")


if __name__ == "__main__":
    main()