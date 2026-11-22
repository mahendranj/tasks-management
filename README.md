# Task Management - Cerebrum P3 Automation

Automated task creation system that reads task files and creates them in Cerebrum P3 enterprise application.

## 📁 Directory Structure

```
tasks-management/
├── Input/
│   ├── tasks.csv.enc               # Encrypted task list (source of truth)
│   └── TODO *.txt                  # Legacy monthly .txt files (archive only, no longer read)
├── Output/
│   └── Daily_Reports/
│       └── [Daily execution logs]
├── encrypt_decrypt.py              # Fernet encrypt/decrypt helper for tasks.csv
├── README.md
├── IMPLEMENTATION_GUIDE.md
└── .gitignore                      # Blocks plaintext tasks.csv / tasks_decrypted.csv
```

## 📝 Input Format

Tasks live in `Input/tasks.csv.enc`, an encrypted CSV. Plaintext `tasks.csv` is
**never committed** (it is git-ignored). Columns:

| Column | Description |
|---|---|
| Title | Task title |
| Description | Task description |
| Due Date | Due date of the task |
| Severity | Severity level in Cerebrum |
| Billing Type | Billing type in Cerebrum |

Fixed values applied to every task on creation: **Assignee** = Mahendran J,
**Status** = Not Started, **Task_Type** = Production.

### Editing the task list

```bash
export ENCRYPTION_KEY=<your key>
python encrypt_decrypt.py decrypt   # Input/tasks.csv.enc -> tasks_decrypted.csv
# edit tasks_decrypted.csv, save it as Input/tasks.csv
python encrypt_decrypt.py encrypt   # Input/tasks.csv -> Input/tasks.csv.enc
rm -f tasks_decrypted.csv Input/tasks.csv
```

Generate a new key with `python encrypt_decrypt.py generate`.

## ⚙️ Automation

**Scheduled Execution:**
- **Time:** Every weekday at 8:30 AM IST (3:00 AM UTC)
- **Frequency:** Monday - Friday
- **Process:**
  1. Clone the repo
  2. Decrypt `Input/tasks.csv.enc` using the `ENCRYPTION_KEY` secret
  3. Parse the CSV tasks
  4. Log into Cerebrum P3 at `CEREBRUM_URL` (`CEREBRUM_EMAIL`, `CEREBRUM_PASSWORD`)
  5. Create each task in Cerebrum
  6. Log results to `Output/Daily_Reports/`
  7. Securely delete the decrypted file
  8. Commit and push the logs

## 📊 Output Files

Daily execution creates logs in `Output/Daily_Reports/`:

- `creation_log_YYYYMMDD.txt` - Successfully created tasks
- `errors_YYYYMMDD.txt` - Failed task creations
- `summary_YYYYMMDD.txt` - Execution summary

## 🔐 Security

- `ENCRYPTION_KEY`, `CEREBRUM_EMAIL` and `CEREBRUM_PASSWORD` are stored as secrets (`CEREBRUM_URL` is a plain variable) in the cloud environment
- Task data is committed only in encrypted form (`tasks.csv.enc`)
- The decrypted CSV is deleted after every run
- Never committed to GitHub
- Personal Access Token for GitHub push operations
- Execution logs available at: https://claude.ai/code/routines

## 🚀 Setup Instructions

See `IMPLEMENTATION_GUIDE.md` for complete setup steps.

---

**Cloud Routine:** Daily Task Allocation via Claude  
**Repository:** https://github.com/mahendranj/tasks-management  
**Last Updated:** 2026-11-22
