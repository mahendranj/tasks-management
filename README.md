# Task Management - Cerebrum P3 Automation

Automated task creation system that reads task files and creates them in Cerebrum P3 enterprise application.

## 📁 Directory Structure

```
tasks-management/
├── Input/
│   ├── TODO November 2026.txt
│   ├── TODO October 2026.txt
│   └── TODO September 2026.txt
├── Output/
│   └── Daily_Reports/
│       └── [Daily execution logs]
├── README.md
├── .gitignore
└── IMPLEMENTATION_GUIDE.md
```

## 📝 Input Format

Task files in `Input/` folder use this format:

```
DD-MM-YYYY
----------
Task description 1
Task description 2

DD-MM-YYYY
----------
Task description
```

## ⚙️ Automation

**Scheduled Execution:**
- **Time:** Every weekday at 8:30 AM IST (3:00 AM UTC)
- **Frequency:** Monday - Friday
- **Process:**
  1. Read task files from Input folder
  2. Parse task details
  3. Log into Cerebrum P3
  4. Create tasks in the system
  5. Log results to Output/Daily_Reports/
  6. Commit and push results to GitHub

## 📊 Output Files

Daily execution creates logs in `Output/Daily_Reports/`:

- `creation_log_YYYYMMDD.txt` - Successfully created tasks
- `errors_YYYYMMDD.txt` - Failed task creations
- `summary_YYYYMMDD.txt` - Execution summary

## 🔐 Security

- Credentials stored securely in cloud routine configuration
- Never committed to GitHub
- Personal Access Token for GitHub push operations
- Execution logs available at: https://claude.ai/code/routines

## 🚀 Setup Instructions

See `IMPLEMENTATION_GUIDE.md` for complete setup steps.

---

**Cloud Routine:** Daily Task Allocation via Claude  
**Repository:** https://github.com/mahendranj/tasks-management  
**Last Updated:** 2026-11-21
