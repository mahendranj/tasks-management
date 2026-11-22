# Cerebrum P3 – Create Tasks from an Excel File

Hand this file to Claude (another account) together with the Excel file. Claude reads the rows
of the Excel file and creates one task per row in Cerebrum P3.

## 1. What you provide

| Item | Details |
|---|---|
| Excel file | `.xlsx` (or `.xls`). First sheet, first row is the header. |
| Cerebrum URL | `https://enterpriseapps.tsts.in:44444/cerebrump3/web/` |
| Login | Cerebrum P3 email and password, supplied as environment variables or secrets. **Never write them in this file, the repo, or the logs.** |

Environment variables Claude should use:

```
CEREBRUM_URL=https://enterpriseapps.tsts.in:44444/cerebrump3/web/
CEREBRUM_EMAIL=<login email>
CEREBRUM_PASSWORD=<password>
```

## 2. Excel format

Header row (names are matched case-insensitively, extra columns are ignored):

| Title | Description | Due Date | Severity | Billing Type |
|---|---|---|---|---|

- **Title** is required. Skip empty rows. Report rows with no Title as errors.
- **Due Date** may be an Excel date or text. Normalise to the format Cerebrum's form expects.
- **Severity** and **Billing Type** must match values available in Cerebrum's dropdowns.
  If a value does not match, log an error for that row. Do not guess.

Fixed values applied to every task:

| Field | Value |
|---|---|
| Assignee | Mahendran J (change here if another person should own the tasks) |
| Status | Not Started |
| Task_Type | Production |

## 3. Instructions for Claude

1. Read the Excel file (for example with Python `openpyxl` or `pandas`). Parse every data row
   into Title, Description, Due Date, Severity, Billing Type.
2. Show the user the number of rows parsed. Do not print the full task contents unless asked.
3. Check that `CEREBRUM_URL` is reachable. If the connection is blocked or reset, **stop**.
   Tell the user the exact host (`enterpriseapps.tsts.in`, port `44444`) and what failed.
   Do not invent results.
   - Network allowlist: the host `enterpriseapps.tsts.in` must be allowed in the environment.
   - The server may accept connections only from the office network or VPN. If a cloud session
     cannot reach it, run the task from a machine that can, such as the user's own computer.
4. Log in to Cerebrum P3 with `CEREBRUM_EMAIL` and `CEREBRUM_PASSWORD` (browser automation,
   for example Playwright).
5. For each row, open the create-task form and fill in Title, Description, Due Date, Severity,
   Billing Type, plus the fixed values above. Submit. Confirm the task was created
   (success message or the new task appears) before counting it as created.
6. If a row fails, record the real error and continue with the next row.
7. Do not create a task twice. If the run is repeated, check for an existing task with the same
   Title and Due Date first.
8. Write the logs (section 4), then delete any decrypted or temporary copies of the data.
9. Report to the user: rows parsed, created, failed, and where the logs are.

## 4. Output logs

Write to `Output/Daily_Reports/` (or the folder the user names), using today's date `YYYYMMDD`:

- `creation_log_YYYYMMDD.txt` – one line per created task (row number, title, time)
- `errors_YYYYMMDD.txt` – one line per failed row with the real error message
- `summary_YYYYMMDD.txt` – totals: parsed, created, failed, and the overall status

Never log passwords, the Excel file contents beyond task titles, or tokens.

## 5. Rules

- Do not fabricate results. If something is blocked, log the real error and report it.
- Do not print secrets.
- Do not commit the Excel file if it contains confidential data. Add it to `.gitignore`.
- Commit and push only the logs, and only if the user asks.
