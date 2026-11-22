# Cerebrum P3 – Create / Update Tasks from an Excel File (Shareable)

Share this file, together with an Excel file, with anyone who uses Claude. Claude opens the
**internal browser** (a browser on a computer that can reach the Cerebrum site), reads the
Excel rows, and creates or updates one task per row.

Only the URL is fixed. Everything else (assignee, status, task type, etc.) comes from the
Excel file or from the person running it.

**URL (fixed):** `https://enterpriseapps.tsts.in:44444/cerebrump3/web/`

---

## 1. Master prompt (copy and paste this to Claude)

```
Follow the instructions in CEREBRUM_TASKS_FROM_EXCEL.md.

Excel file: <attach or give the path of the .xlsx file>
Cerebrum URL: https://enterpriseapps.tsts.in:44444/cerebrump3/web/

Open the internal browser, go to the URL, and log in. If I am not logged in, ask me to log in
myself in the browser; do not ask me to type my password into the chat.
Read every row of the Excel file. For each row, create the task in Cerebrum, or update it if a
matching task already exists. Use only the values in the Excel row. For any field that is
empty, use the defaults I give below; if there is no default, ask me.

Defaults for empty cells (optional):
  Assignee: <name>
  Status: <e.g. Not Started>
  Task_Type: <e.g. Production>

Before changing anything, show me how many rows you read and how many will be created and
updated, and wait for my OK. After each row, check the task really exists in Cerebrum.
Write the three log files described in the instructions. Never invent results: if a row
fails, log the real error and continue. Do not print my password.
```

---

## 2. Excel format

The first row is the header. Column names are matched ignoring upper/lower case. Extra
columns are ignored. Only include the columns you need.

| Column | Required | Notes |
|---|---|---|
| Title | Yes | Rows with no Title are logged as errors and skipped. |
| Description | No | |
| Due Date | No | Excel date or text. Convert to the format the Cerebrum form expects. |
| Severity | No | Must match a value in Cerebrum's dropdown. |
| Billing Type | No | Must match a value in Cerebrum's dropdown. |
| Assignee | No | Person's name exactly as shown in Cerebrum. Changes per row or per file. |
| Status | No | Value from Cerebrum's Status dropdown. |
| Task_Type | No | Value from Cerebrum's Task Type dropdown. |
| Task ID | No | If present, the row updates that task instead of creating a new one. |
| *Any other field* | No | If the Cerebrum form has another field, add a column with the same name as the form label. Claude fills it in. |

Value priority for each field: **Excel cell, then the default in the prompt, then ask the user.**
Do not guess a dropdown value. If it does not match, log an error for that row.

---

## 3. Instructions for Claude

1. **Read the Excel file** (Python `openpyxl` or `pandas`). Parse each row into the columns
   above. Tell the user the number of rows. Do not print full task contents unless asked.
2. **Open the internal browser** and go to the URL. This must be a browser running on a
   computer that can reach the site; the site is usually reachable only from the company
   network or VPN.
   - Built-in browser or Claude in Chrome on the user's own computer is the right choice.
   - A cloud session usually cannot reach this host. If the page does not load, **stop**
     and tell the user the exact host (`enterpriseapps.tsts.in`, port `44444`) and the
     error. Do not invent results.
3. **Log in.** Use the session the user is already logged in with. If a login page appears,
   ask the user to log in themselves. Never ask for the password in chat, and never write it
   in a file or log.
4. **Look at the form first.** Open the create-task form once and note the real field names
   and dropdown values. Use them to check the Excel values before changing anything.
5. **Plan and confirm.** For each row decide: *update* (Task ID given, or an existing task
   has the same Title and Due Date) or *create*. Show the user the counts and wait for OK.
6. **Do the work row by row.** Fill in the form from the row, submit, and verify the task now
   exists with the right values (success message, or open the task and check). Only then
   count it as done.
7. **On failure,** record the real error, take no further action on that row, and continue.
8. **Never create duplicates.** On a repeated run, rows that already exist are updated or
   skipped, not created again.
9. **Write logs** (section 4) and report: rows read, created, updated, failed.
10. Delete any temporary copies of the data you made.

## 4. Output logs

Write to `Output/Daily_Reports/` (or the folder the user names). Use today's date as `YYYYMMDD`:

- `creation_log_YYYYMMDD.txt` – one line per created or updated task: row number, title,
  Task ID if known, "created" or "updated", time.
- `errors_YYYYMMDD.txt` – one line per failed row with the real error message.
- `summary_YYYYMMDD.txt` – totals (read, created, updated, failed) and the overall status.

Never log passwords, tokens, or task descriptions. Titles and IDs are enough.

## 5. Rules

- Do not make up results. If blocked, log the real error and report it.
- Do not print or store secrets.
- Change only what the Excel row says. Leave other fields on existing tasks as they are.
- Do not commit the Excel file if it holds confidential data.
- Commit and push the logs only if the user asks.

## 6. Troubleshooting

| Problem | What to do |
|---|---|
| Page won't load, or "connection reset" | The server is probably reachable only from the company network or VPN. Use the browser on a computer connected to it. |
| Login page appears | Ask the user to log in in the browser, then continue. |
| Dropdown value not found | Log an error for that row with the value and the allowed options. Do not guess. |
| Assignee not found | Check the spelling against the name shown in Cerebrum. |
