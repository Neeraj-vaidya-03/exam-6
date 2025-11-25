import os
from datetime import datetime

print("----\n  Welcome to personal journal manager----")
print("--\n please select an option---")

print("1.add entry")
print("2.view all entries")
print("3.search entry")
print("4.delete all entries")
print("5.exit")

choice = int(input("enter your choice(1-5):"))

match choice:
    case 1: 
        def add_entry():
            try:
               entry =input("\n write your journal entry:\n")
               time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
               full_entry =(f"{time} {entry} \n")
               with open("journal.txt" , "a")as file:
                    file.write(full_entry + "\n")
                    print("\n entry saved successfully!")
            except Exception as e:
                print(f"error wirting to file:{e}")
        add_entry()
        
    case 2 :
        def view_entries():
            try:
                with open("journal entry" ,"r")as file:
                 time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                 entries =file.read()
                
                if entries .strip():
                    print("\n--- journal entries found---\n")
                else:
                    print(" no entries  available")
            except Exception as e:
                print(f"error in reading files:{e}")
        view_entries()
        
    case 3:
        def search_entry():
            try:
                keyword = input("\n enter the txt to search:")
                found = False 
                
                with open("file name")as file:
                    entries = file.readlines()
                    for entries in entries:
                        if keyword in entries:
                            print(entries.strip())
                            found = True
            except Exception as e:
                print(f"error in searching entries:{e}")
        search_entry() 
        
    case 4:
        def delete_entries():
            try:
                confirm = input("\n are you sure to delete all entries? (yes/no):")
                if confirm.lower() == "yes":
                    os.remove("journal.txt")
                    print("\n all entries deleted.")
                else:
                    print("\n cancelled.")
            except Exception as e:
                  print(f"error deleteing file:{e}")
        delete_entries()
        
    case 5:
        print("\n thank you for using the journal.goodbye!")
                
                
        
                        
                    
                
                