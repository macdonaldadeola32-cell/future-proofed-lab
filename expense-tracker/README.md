# 💰 Expense Tracker

**My first Python project** — a CLI tool to track daily expenses.

## What It Does

- ➕ Add expenses with description, category, amount & date
- 📋 List all expenses in a formatted table
- 📊 Show total spending + category breakdown with visual bars
- 🗑️ Delete expenses by number
- 💾 Saves everything to a JSON file (persistent between runs)

## What I Learned

| Concept | How I Used It |
|---------|---------------|
| Variables | Storing user input, file paths, expense data |
| Functions | `add_expense()`, `list_expenses()`, `show_summary()`, etc. |
| Conditionals | Input validation, menu choices, empty-state checks |
| Loops | Main menu loop, iterating expense lists |
| Lists | Storing all expenses |
| Dictionaries | Each expense as a key-value pair |
| File I/O | Reading/writing `expenses.json` |
| JSON | Serializing/deserializing expense data |
| Error Handling | `try/except` for invalid number input |

## How to Run

```bash
cd expense-tracker
python3 expenses.py
```

## Next Steps

- Send this to GitHub
- Add expense editing
- Add date filtering
- Add CSV export
