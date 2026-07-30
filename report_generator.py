class ReportGenerator:

    def generate(self, analysis, output_file):

        with open(output_file, "w") as file:

            file.write("=" * 50 + "\n")
            file.write("LOG ANALYSIS REPORT\n")
            file.write("=" * 50 + "\n\n")

            file.write("Log Level Summary\n")
            file.write("-" * 30 + "\n")

            for level, count in analysis["level_count"].items():
                file.write(f"{level}: {count}\n")

            file.write("\n")

            file.write("Most Frequent Messages\n")
            file.write("-" * 30 + "\n")

            for message, count in analysis["messages"].most_common():
                file.write(f"{message} -> {count}\n")

        print("Report generated successfully!")