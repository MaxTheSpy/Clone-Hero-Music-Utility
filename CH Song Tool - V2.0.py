import os
import shutil

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help():
    clear_console()
    print("Help:")
    print("This script organizes folders into a structure based on band names and song names.")
    print("\nFolder Setup:")
    print("1. Your music folder should contain subfolders named in the format 'Band - Song Name'.")
    print("2. For example, if you have a band named 'The Great Band' and a song named 'Hit Single',")
    print("   you should have a folder named 'The Great Band - Hit Single'.")
    print("\nHow the Script Works:")
    print("1. The script will iterate through each folder in the specified music folder.")
    print("2. It will split the folder names based on ' - ' to determine the band name and song name.")
    print("3. It will create a new folder for each band if it doesn't already exist.")
    print("4. The script will move each song folder into the corresponding band folder.")
    print("5. If a folder with the same name already exists, you will be given options to:")
    print("   - Overwrite the existing folder")
    print("   - Skip moving the folder")
    print("   - Delete the existing folder")
    print("\nOptions:")
    print("1. Sort songs into band folders: Organizes your folders as described.")
    print("2. Fix Bad Songs: Handles issues listed in pasted content.")
    print("3. Exit: Closes the script.")
    print("h: Show this help text.")
    print("\nInfo:")
    print("If you run into any problems, please contact maxthespy on Discord.")
    print("Use at your own risk.")
    input("Hit Enter to return to the menu...")
def sort_songs_into_band_folders():
    clear_console()
    
    source_directory = input('Path to your music folder: ').strip()
    
    if not os.path.isdir(source_directory):
        print("The provided path is not a directory or does not exist.")
        input("Hit Enter to return to the menu...")
        return

    for folder_name in os.listdir(source_directory):
        folder_path = os.path.join(source_directory, folder_name)
        
        if os.path.isdir(folder_path):
            split_name = folder_name.split(' - ')

            if len(split_name) > 1:
                parent_folder_name = split_name[0].strip()
                parent_folder_path = os.path.join(source_directory, parent_folder_name)

                if not os.path.exists(parent_folder_path):
                    os.makedirs(parent_folder_path)

                destination_path = os.path.join(parent_folder_path, folder_name)

                if os.path.exists(destination_path):
                    while True:
                        choice = input(f"The folder '{folder_name}' already exists in '{parent_folder_name}'. Overwrite, skip, or delete? (o/s/d): ").lower()
                        if choice == 'o':
                            try:
                                shutil.rmtree(destination_path)
                                shutil.move(folder_path, destination_path)
                                print(f"Overwritten and moved {folder_name} to {parent_folder_name}/")
                                break
                            except Exception as e:
                                print(f"An error occurred while overwriting: {e}")
                        elif choice == 's':
                            print(f"Skipped moving {folder_name}.")
                            break
                        elif choice == 'd':
                            try:
                                shutil.rmtree(folder_path)
                                print(f"Deleted {folder_name}.")
                                break
                            except Exception as e:
                                print(f"An error occurred while deleting: {e}")
                        else:
                            print("Invalid choice. Please enter 'o', 's', or 'd'.")
                else:
                    try:
                        shutil.move(folder_path, destination_path)
                        print(f"Moved {folder_name} to {parent_folder_name}/")
                    except Exception as e:
                        print(f"An error occurred while moving: {e}")

    print("Sorting complete.")
    input("Hit Enter to return to the menu...")

import os
import shutil

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def fix_bad_songs():
    clear_console()
    print("Please copy and paste everything under 'ERROR: These folders contain charts that another song has (duplicate charts)!'")
    print("When finished pasting, type 'fix' and press Enter:")
    
    bad_songs_content = []
    while True:
        line = input()
        if line.strip().lower() == 'fix':
            break
        bad_songs_content.append(line.strip())

    if not bad_songs_content:
        print("No content provided.")
        input("Hit Enter to return to the menu...")
        return

    for line in bad_songs_content:
        if not line:
            continue

        try:
            # Find the split point for the path
            split_point = line.find('(')
            if split_point == -1:
                print(f"Line '{line}' is not in the expected format.")
                continue

            original_path = line[:split_point].strip()
            duplicate_path = line[split_point:].strip()

            # Remove leading '(' and trailing ')' from the duplicate path
            if duplicate_path.startswith('('):
                duplicate_path = duplicate_path[1:].strip()
            if duplicate_path.endswith(')'):
                duplicate_path = duplicate_path[:-1].strip()

            # Check for additional unwanted text at the beginning of the duplicate path
            # Remove the text before the actual path if it's not part of the file name
            start_index = duplicate_path.find('c:\\')
            if start_index != -1:
                duplicate_path = duplicate_path[start_index:]

            print(f"\n1. Original Path: {original_path}")
            print(f"2. Duplicate Path: {duplicate_path}")

            while True:
                choice = input("Which path do you want to delete? (1 for Original Path, 2 for Duplicate Path, or n to skip): ").strip().lower()
                if choice == '1':
                    if os.path.isdir(original_path):
                        try:
                            shutil.rmtree(original_path)
                            print(f"Deleted {original_path}.")
                        except Exception as e:
                            print(f"An error occurred while deleting {original_path}: {e}")
                    else:
                        print(f"The path '{original_path}' does not exist.")
                    break
                elif choice == '2':
                    if os.path.isdir(duplicate_path):
                        try:
                            shutil.rmtree(duplicate_path)
                            print(f"Deleted {duplicate_path}.")
                        except Exception as e:
                            print(f"An error occurred while deleting {duplicate_path}: {e}")
                    else:
                        print(f"The path '{duplicate_path}' does not exist.")
                    break
                elif choice == 'n':
                    print("Skipped deletion.")
                    break
                else:
                    print("Invalid choice. Please enter '1', '2', or 'n'.")
        except Exception as e:
            print(f"An error occurred while processing the line '{line}': {e}")

    print("Fixing complete.")
    input("Hit Enter to return to the menu...")


def main():
    while True:
        clear_console()
        print("What would you like to do?")
        print("1. Sort Songs Into Band Folders")
        print("2. Fix Bad Songs")
        print("h. Help")
        print("e. Exit")

        choice = input("Enter your choice (1, 2, 3, or h): ").strip().lower()
        
        if choice == '1':
            sort_songs_into_band_folders()
        elif choice == '2':
            fix_bad_songs()
        elif choice == 'e':
            print("Goodbye!")
            break
        elif choice == 'h':
            show_help()
        else:
            print("Invalid choice. Please enter '1', '2', '3', or 'h'.")
            input("Hit Enter to continue...")

if __name__ == "__main__":
    main()
