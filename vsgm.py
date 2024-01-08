import os
from scripts.process_video_directory import process_video_files

def validate_drive(drive):
    # Check if the drive is missing the colon and backslash
    if len(drive) == 1 and drive.isalpha():
        return drive.upper() + ":\\"
    elif len(drive) == 2 and drive[1] == ":" and drive[0].isalpha():
        return drive.upper() + "\\"
    else:
        return drive

def list_directories(drive):
    directories = [d for d in os.listdir(drive) if os.path.isdir(os.path.join(drive, d))]
    return directories

def select_directory(directories):
    print("Available directories:")
    for i, directory in enumerate(directories, start=1):
        print(f"{i}. {directory}")

    while True:
        try:
            selection = int(input("Select a directory (enter the number): "))
            if 1 <= selection <= len(directories):
                return directories[selection - 1]
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    # Ask for a drive name
    drive_name = input("Enter a drive name (e.g., C): ")
    
    # Validate and format the drive name
    validated_drive = validate_drive(drive_name)

    # Check if the drive exists
    if os.path.exists(validated_drive) and os.path.isdir(validated_drive):
        # List all directories on the drive
        directories_on_drive = list_directories(validated_drive)

        if not directories_on_drive:
            print(f"No directories found on {validated_drive}.")
        else:
            selected_directory = select_directory(directories_on_drive)
            #print(f"Selected directory: {validated_drive}{selected_directory}")
            process_video_files(validated_drive + selected_directory)
    else:
        print(f"The drive '{validated_drive}' does not exist or is not a valid drive.")
