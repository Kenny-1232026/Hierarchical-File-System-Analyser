

from pathlib import Path
import json

all_files = []
final_report = {}

total_file = 0
total_folder = 0
total_size = 0

def analyze_a_folder(path):

    global total_file
    global total_folder
    global total_size

    #---------(processes folder path)
    if path.exists():

        for item in path.iterdir():
            if item.is_file():
                file_info = {
                    "name": item.name,
                    "size": item.stat().st_size,
                    "extension": item.suffix,
                    "full_path": str(item)
                }
                all_files.append(file_info)
                total_file += 1
                total_size += item.stat().st_size

            elif item.is_dir():
                total_folder += 1
                analyze_a_folder(item)

            largest_file = max(all_files, key=lambda x: x["size"])
        
        print(f"Total_files: {total_file}")
        print(f"Total_folders: {total_folder}")
        print(f"Totals_size: {total_size}")
        print(f"Largest_file: {largest_file}")

        report = {
            "total_files": total_file,
            "total_folders": total_folder,
            "total_size": total_size,
            "largest_file": largest_file,
        }

        with open("report.json", "w") as f:
            json.dump(report, f, indent = 4)
    
    else:
        print("Enter a valid file path!")


def main_menu():
    while True:
        print("\n===== Welcome =====")
        print("\n1. Analyze a folder/file")
        print("2. Exit")
        menu = input("pick a menu: ").strip().lower()

        if menu == "1":
            path = Path(input("Enter folder path: "))
            analyze_a_folder(path)

        elif menu == "2":
            print("Exit successful!")
            break

        else:
            print("This input is not recognized")
main_menu()
