import re

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
