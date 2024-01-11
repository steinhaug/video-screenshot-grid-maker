import os
from PIL import Image
#from scripts.stitch_images_create_grid import stitch_images_create_grid
from scripts.stitch_images_create_grid_with_text import stitch_images_create_grid
#from scripts.process_video_extract_screens_subprocess import extract_screens_from_video
from scripts.process_video_extract_screens import extract_screens_from_video

temp_screens = [
    "image0.jpg", "image1.jpg", "image2.jpg", "image3.jpg", 
    "image4.jpg", "image5.jpg", "image6.jpg", "image7.jpg", 
    "image8.jpg", "image9.jpg", "image10.jpg", "image11.jpg",
    "image12.jpg", "image13.jpg", "image14.jpg", "image15.jpg",
    "image16.jpg", "image17.jpg", "image18.jpg", "image19.jpg",
    "image20.jpg", "image21.jpg", "image22.jpg", "image23.jpg", "image24.jpg",
]

def remove_extension(filename):
    # Remove the extension from the filename
    filename_without_extension = os.path.splitext(filename)[0]
    return filename_without_extension

def delete_files(filenames):
    for filename in filenames:
        if os.path.exists(filename):
            try:
                os.remove(filename)
                if os.path.exists(filename):
                    print(f"Error deleting {filename}: File still exists")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")

def format_time(minutes):
    if minutes >= 60:
        hours = int(minutes // 60)
        remaining_minutes = int(minutes % 60)
        if remaining_minutes == 0:
            return f"{hours} hour{'s' if hours > 1 else ''}"
        else:
            return f"{hours} hour{'s' if hours > 1 else ''} {remaining_minutes} minute{'s' if remaining_minutes > 1 else ''}"
    else:
        return f"{int(minutes)} minute{'s' if minutes > 1 else ''}"

def process_video_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
                file_path = os.path.join(root, file)
                filename = os.path.basename(file_path)

                print(f"Processing video {file}, located {root}")
                if not os.path.exists(os.path.join(root, remove_extension(filename)) + '.jpg'):
                    if not os.path.exists(file_path + '.delete'):
                        with open(file_path + '.delete', 'w') as file:
                            file.write('You can safely delete this file, it\'s temporary lock file while creating screens using Video ScreenShot Maker (VSSM).')
                        delete_files(temp_screens)
                        try:
                            movie_length = extract_screens_from_video(file_path, file, len(temp_screens))
                            stitch_images_create_grid(root, remove_extension(filename), temp_screens, f"Duration: {format_time(movie_length / 30)}", 5)
                            if os.path.exists(file_path + '.delete'):
                                os.remove(file_path + '.delete')
                        except Exception as e:
                            print(f"- Error processing {file}: {e}")
                    else:
                        print(f"- Skipping video, lock file found most likely problem with video in previous run.")
                else:
                    print(f"- Skipping video, screens already exists.")
    delete_files(temp_screens)

if __name__ == "__main__":
    directory_name = input("Enter a directory name: ").strip()
    if os.path.exists(directory_name) and os.path.isdir(directory_name):
        process_video_files(directory_name)
    else:
        print(f"The directory '{directory_name}' does not exist or is not a valid directory. Script aborted.")
