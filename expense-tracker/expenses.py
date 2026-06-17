#!/usr/bin/env python3
"""
💰 Expense Tracker — Kiza's Python Day 1 Project

A CLI tool to track daily expenses with persistent storage.
Builds: variables, functions, conditionals, loops, file I/O, JSON, dicts, lists
"""

import json
import os
from datetime import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "expenses.json")


def load_expenses():
    """Load expenses from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense():
    """Add a new expense with user input."""
    print("\n--- ➕ Add Expense ---")
    description = input("Description: ").strip()
    if not description:
        print("❌ Description cannot be empty.")
        return

    category = input("Category (e.g., Food, Transport, Bills, Shopping): ").strip().title()
    if not category:
        print("❌ Category cannot be empty.")
        return

    while True:
        try:
            amount = float(input("Amount (₦): "))
            if amount <= 0:
                print("❌ Amount must be positive.")
                continue
            break
        except ValueError:
            print("❌ Invalid amount. Enter a number (e.g., 1500).")

    date = input("Date (YYYY-MM-DD, Enter for today): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date,
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Added: {description} — ₦{amount:,.2f} ({category})")


def list_expenses():
    """Display all expenses in a formatted table."""
    expenses = load_expenses()
    if not expenses:
        print("\n📭 No expenses recorded yet.")
        return

    print("\n--- 📋 All Expenses ---")
    print(f"{'#':<4} {'Date':<12} {'Category':<18} {'Description':<28} {'Amount':<12}")
    print("-" * 74)

    for i, exp in enumerate(expenses, 1):
        print(
            f"{i:<4} {exp['date']:<12} {exp['category']:<18} "
            f"{exp['description']:<28} ₦{exp['amount']:<9,.2f}"
        )


def show_summary():
    """Show total spending and category breakdown."""
    expenses = load_expenses()
    if not expenses:
        print("\n📭 No expenses recorded yet.")
        return

    total = sum(exp["amount"] for exp in expenses)
    print(f"\n--- 📊 Summary ---")
    print(f"💰 Total spent:    ₦{total:,.2f}")
    print(f"📝 Total entries:  {len(expenses)}")

    # Category breakdown
    categories = {}
    for exp in expenses:
        cat = exp["category"]
        categories[cat] = categories.get(cat, 0) + exp["amount"]

    print(f"\n📂 By Category:")
    for cat, amt in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        pct = (amt / total) * 100
        bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
        print(f"  {cat:<18} ₦{amt:>8,.2f} ({pct:5.1f}%) {bar}")


def delete_expense():
    """Delete an expense by its number."""
    expenses = load_expenses()
    if not expenses:
        print("\n📭 No expenses to delete.")
        return

    list_expenses()
    try:
        idx = int(input("\nEnter # to delete (0 to cancel): "))
        if idx == 0:
            return
        removed = expenses.pop(idx - 1)
        save_expenses(expenses)
        print(f"🗑️ Deleted: {removed['description']} — ₦{removed['amount']:,.2f}")
    except (ValueError, IndexError):
        print("❌ Invalid number.")


def menu():
    """Main menu loop."""
    while True:
        print("\n" + "═" * 42)
        print("          💰 EXPENSE TRACKER")
        print("═" * 42)
        print("  1. ➕  Add Expense")
        print("  2. 📋  List All Expenses")
        print("  3. 📊  Show Summary")
        print("  4. 🗑️  Delete Expense")
        print("  5. 🚪  Exit")
        print("═" * 42)

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("👋 Goodbye! Track those expenses! 💰")
            break
        else:
            print("❌ Invalid choice. Enter 1-5.")


if __name__ == "__main__":
    menu()
