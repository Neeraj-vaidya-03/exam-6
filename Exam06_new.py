import os
from datetime import datetime

def add_entry():
    try:
        entry = input("\nWrite your journal entry:\n")
        time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        full_entry = f"{time} {entry}\n\n"

        with open("journal.txt", "a") as file:
            file.write(full_entry)

        print("\n Entry saved successfully!")

    except Exception as e:
        print(f"Error writing to file: {e}")


def view_entries():
    try:
        with open("journal.txt", "r") as file:
            entries = file.read()

        if entries.strip():
            print("\n--- Journal Entries Found ---\n")
            print(entries)
        else:
            print("\nNo entries available.")

    except FileNotFoundError:
        print("\njournal.txt file not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


def search_entry():
    try:
        keyword = input("\nEnter text to search: ")
        found = False

        with open("journal.txt", "r") as file:
            entries = file.readlines()

        print("\n--- Search Results ---")
        for line in entries:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

        if not found:
            print("No matching entries found.")

    except FileNotFoundError:
        print("\njournal.txt not found.")
    except Exception as e:
        print(f"Error searching entries: {e}")


def delete_entries():
    try:
        confirm = input("\nDelete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            os.remove("journal.txt")
            print("\nAll entries deleted.")
        else:
            print("\nCancelled.")

    except FileNotFoundError:
        print("\nNothing to delete.")
    except Exception as e:
        print(f"Error deleting file: {e}")


while True:

    print("\n---- Welcome to Personal Journal Manager ----")
    print("1. Add Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice (1-5): "))
    except:
        print("Please enter numbers only.")
        continue

    match choice:
        case 1:
            add_entry()

        case 2:
            view_entries()

        case 3:
            search_entry()

        case 4:
            delete_entries()

        case 5:
            print("\nThank you for using the Journal. Goodbye!")
            break

        case _:
            print("\nInvalid option. Try again.")
