import sys
import os
import ffmpeg

def extract_screens_from_video(videofile_path, filename="", parts=25):
    print(f"Processing screens from video...")

    if os.path.exists(videofile_path):
        probe = ffmpeg.probe(videofile_path)
        # Filter for video streams only
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)

        if video_stream:
            time = float(video_stream['duration']) // 2
            width = video_stream['width']

            intervals = int(time) // parts
            interval_list = [(i * intervals, (i + 1) * intervals) for i in range(parts)]
            i = 0

            for item in interval_list:
                (
                    ffmpeg
                    .input(videofile_path, ss=item[1])
                    .filter('scale', width, -1)
                    .output(f'image{i}.jpg', vframes=1)
                    .run()
                )
                i += 1

            return time
        else:
            print("No video stream found in the file.")
            return ""
    else:
        print(f"Video file does not exist, skipping")
        return ""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Extract the filename from the first command-line argument
        file_to_check = sys.argv[1]
        if os.path.exists(file_to_check):
            extract_screens_from_video(file_to_check, '')
        else:
            print("File {file_to_check} does not exist.")
    else:
        video_to_process = 'g:/__video/some-videofile.mp4'
        user_response = input(f"Continue and process '{video_to_process}' for screenshots? (Yes/No): ").strip().lower()
        if user_response == 'yes':
            extract_screens_from_video(video_to_process, '')
        else:
            print('Script aborted.')
