# 🐧 Linux CLI Python Scripts

This repository contains a collection of **Python-based command-line tools** designed to automate and simplify common **Linux system administration tasks**.

---

## 📂 What's Included

| Script | Description |
|--------|-------------|
| `disk_usage_report.py` | Displays disk usage per mount point or directory |
| `user_audit.py`        | Lists system users and their last login time |
| `process_killer.py`    | Finds and kills processes by name |
| `system_uptime.py`     | Prints current system uptime and load averages |
| `log_monitor.py`       | Watches a log file and highlights specific keywords |

---

## ⚙️ Requirements

- Python 3.6+
- Runs on most Linux distros (Ubuntu, CentOS, Debian, etc.)
- No external dependencies (uses `os`, `subprocess`, etc.)

---

## 🚀 Usage

Clone the repo and run any script:

```bash
git clone https://github.com/<username>/linux-cli-python-scripts.git
cd linux-cli-python-scripts
python3 disk_usage_report.py
