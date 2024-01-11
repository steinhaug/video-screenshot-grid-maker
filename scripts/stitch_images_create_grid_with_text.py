from PIL import Image, ImageDraw, ImageFont
import math
import os

def check_if_all_files_exist(files):
    all_exist = all(os.path.exists(file) for file in files)
    return all_exist

def stitch_images_create_grid(video_folder, video_name, temp_screens, txt1="", images_per_row=5):
    print(f"- Stitching extracted images together as a grid...")

    if check_if_all_files_exist(temp_screens):
        # Open all images
        images = [Image.open(filename) for filename in temp_screens]

        # Calculate the number of rows needed
        num_rows = math.ceil(len(images) / images_per_row)

        # Calculate total width and height without resizing
        total_width = images_per_row * images[0].width
        total_height = num_rows * images[0].height

        # Check if total width exceeds 5000 pixels
        if total_width > 5000:
            # Shrink the images by 50%
            new_width = images[0].width // 2
            new_height = images[0].height // 2

            images = [image.resize((new_width, new_height), Image.LANCZOS) for image in images]
            images_per_row = min(images_per_row, len(images))
            total_width = images_per_row * new_width
            total_height = num_rows * new_height

        # Create a new blank image
        output_image = Image.new("RGB", (total_width, total_height), color="white")

        # Paste each image onto the output image
        for i, image in enumerate(images):
            row = i // images_per_row
            col = i % images_per_row
            x_offset = col * image.width
            y_offset = row * image.height
            output_image.paste(image, (x_offset, y_offset))

        # Add text at the top of the image with a 50% transparent white background
        draw = ImageDraw.Draw(output_image)

        # Use a larger font size
        font_size = 3 * min(output_image.width, output_image.height) // 100
        font = ImageFont.truetype("arial.ttf", font_size)

        second_y = font_size * 1.25

        # First line of text
        file_name_text = video_name #"This is the name of the file"
        text_size = draw.textbbox((10, 10), file_name_text, font=font)
        extra_x = text_size[2] * 0.05
        extra_y = text_size[3] * 0.25

        background_rect = [(10, 10), (text_size[2] + extra_x, text_size[3] + extra_y)]
        draw.rectangle(background_rect, fill=(255, 255, 255, 128))
        draw.text((20, 10), file_name_text, font=font, fill="black")

        # Second line of text
        movie_info_text = txt1 #"Movie length: 1:00:00, movie type: mpg"
        text_size = draw.textbbox((10, second_y), movie_info_text, font=font)
        background_rect = [(10, second_y), (text_size[2] + extra_x, text_size[3] + extra_y)]
        draw.rectangle(background_rect, fill=(255, 255, 255, 128))
        draw.text((20, second_y), movie_info_text, font=font, fill="black")

        #output_image.save(output_filename)
        output_image.save(os.path.join(video_folder, video_name) + '.jpg', "JPEG")
        #print(f"Image grid with larger text and transparent background saved to {output_filename}")
    else:
        print(f"- Error, missing files for stitcher... skipping...")


if __name__ == "__main__":
    print(f"Function looks for images in executed folder, and creates .jpg in folder of videofile.")
