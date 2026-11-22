# Cerebrum P3 - Automated Task Creation

## 📊 Input File Format

Tasks are read from `Input/tasks.csv.enc` (Fernet-encrypted CSV) with columns:
`Title, Description, Due Date, Severity, Billing Type`.
Assignee (Mahendran J), Status (Not Started) and Task_Type (Production) are set
automatically. The old `Input/TODO *.txt` files are kept as an archive only.

Encrypt/decrypt with `encrypt_decrypt.py` using the `ENCRYPTION_KEY` environment variable.

----------
Task description 1
Task description 2

DD-MM-YYYY
----------
Task description
```

Example from your file:
```
02-11-2026
----------
updated comments in Few K5D documents
GetREICommunicationLogStatus
Maximum Optimization (Favor Speed) (/O2) in SCIXLResource
```

---

## 🚀 Implementation Steps

### STEP 1: GitHub Repository Setup

1. Create a new GitHub repository named `tasks-management`
   - Visit: https://github.com/new
   - Owner: mahendranj
   - Repo name: `tasks-management`
   - Visibility: Public or Private (your choice)
   - Click "Create repository"

2. Push local files to GitHub:
```bash
cd C:\Tasks
git add .
git commit -m "Initial commit: Task automation setup"
git branch -M main
git remote add origin https://github.com/mahendranj/tasks-management.git
git push -u origin main
```

3. Create a **GitHub Personal Access Token** (PAT) for cloud routine:
   - Go to: https://github.com/settings/tokens/new
   - Scopes: `repo` (full control of private repositories)
   - Expiration: 90 days (or as needed)
   - Copy the token (save it securely)

### STEP 2: Cerebrum P3 Information

**I need from you:**

1. **Login Credentials:**
   - User ID (email): ?
   - Password: ?

2. **Task Creation Fields:**
   - After logging in, what are the form fields for creating a task?
   - What is the URL for task creation page?
   - Example fields:
     - Task Title / Description
     - Project / Module
     - Priority
     - Assigned To (Person)
     - Due Date
     - Status
     - Other custom fields?

3. **Task Mapping:**
   - CSV columns map 1:1: Title, Description, Due Date, Severity, Billing Type

### STEP 3: Cloud Routine Creation

Once you provide the information above, I will:

1. Create cloud routine configuration
2. Set schedule: 8:30 AM IST (3:00 AM UTC), Weekdays
3. Configure browser automation to:
   - Decrypt and read Input/tasks.csv.enc
   - Parse CSV tasks
   - Log into Cerebrum P3
   - Create task for each entry
   - Log results to Output folder
   - Push results back to GitHub

---

## 📝 What to Provide

**Urgent:** Please provide:

1. ✅ **Cerebrum P3 Login Email**
2. ✅ **Cerebrum P3 Password**
3. ✅ **Screenshot of task creation form** (or describe form fields)
4. ✅ **GitHub Personal Access Token** (for cloud routine to push results)

**Optional but helpful:**
- Default Project/Priority/Assignee for new tasks
- Any custom field mappings
- Error notification preferences (email, Slack, etc.)

---

## 🔐 Security Notes

- Credentials will be stored securely in cloud routine
- Never exposed in GitHub or logs
- Personal Access Token can be revoked anytime
- Each routine run is logged at claude.ai/code/routines

