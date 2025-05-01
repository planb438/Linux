import re   # Regular expression module for pattern matching
# Function to analyze logs and count occurrences of keywords
# This script analyzes log files and counts occurrences of specified keywords.
# It uses regular expressions to search for keywords in the log data.
# The script reads a log file, searches for specified keywords, and counts their occurrences.
# The script can be used to monitor system logs, application logs, or any text-based log files.
# The script is useful for identifying issues, errors, or specific events in log files.
# The script can be customized to search for different keywords based on user requirements.
# The script can be extended to include additional features such as filtering, sorting, and exporting results.
# The script can be run as a standalone program or imported as a module.
# The script is written in Python and can be run on any platform that supports Python.
# The script is compatible with Python 3.x and uses standard libraries.
# The script is easy to understand and modify, making it suitable for both beginners and experienced programmers.




# The script can be used as a starting point for building more complex log analysis solutions.
# The script can be integrated with other tools and frameworks for enhanced functionality.
# The script can be scheduled to run at regular intervals using a task scheduler or cron job.
# The script can be modified to include options for real-time monitoring and alerting.      




# The script can be customized to suit specific log analysis requirements and workflows.        


def analyze_logs(log_file, keywords):
    # Open the log file
    with open(log_file, 'r') as file:
        log_data = file.readlines()

    # Dictionary to store keyword counts
    keyword_counts = {keyword: 0 for keyword in keywords}

    # Analyze log data
    for line in log_data:
        for keyword in keywords:
            if re.search(keyword, line):
                keyword_counts[keyword] += 1

    # Print keyword counts
    print("Log Analysis Results:")
    for keyword, count in keyword_counts.items():
        print(f"{keyword}: {count}")

if __name__ == "__main__":
    # Specify the log file and keywords to search for
    log_file = "/var/log/syslog"
    keywords = ["error", "warning", "authentication failure"]

    # Analyze logs
    analyze_logs(log_file, keywords)

# Note: Replace '/var/log/syslog' with the actual path to your log file
# This script analyzes log files and counts occurrences of specified keywords.
# It uses regular expressions to search for keywords in the log data.
# The script reads a log file, searches for specified keywords, and counts their occurrences.
# The script can be used to monitor system logs, application logs, or any text-based log files. 
