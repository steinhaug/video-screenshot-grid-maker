import sys
import os
import subprocess

def extract_screens_from_video(video_file, filename="", parts=25):
    try:
        print("- Extracting screenshots from video")

        # Run the new script as a subprocess
        movie_length = subprocess.run(['python', 'lib/process_video_extract_screens.py', video_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        # If you want to capture the output, you can access result.stdout and result.stderr
        # For example, print the captured output
        #print(result.stdout)
        #print(result.stderr)
        return movie_length

    except subprocess.CalledProcessError as e:
        print(f"Error running subprocess: {e}")
        print("Subprocess output (stdout):")
        print(e.stdout)
        print("Subprocess error output (stderr):")
        print(e.stderr)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Extract the filename from the first command-line argument
        file_to_check = sys.argv[1]
        if os.path.exists(file_to_check):
            extract_screens_from_video(file_to_check, '')
        else:
            print("File {file_to_check} does not exist.")
    else:
        video_to_process = 'e:/video/some-videofile.mp4'
        user_response = input(f"Continue and process '{video_to_process}' for screenshots? (Yes/No): ").strip().lower()
        if user_response == 'yes':
            extract_screens_from_video(video_to_process, '')
        else:
            print('Script aborted.')
