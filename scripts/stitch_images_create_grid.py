from PIL import Image
import os

temp_screens = [
    "image0.jpg", "image1.jpg", "image2.jpg", "image3.jpg", 
    "image4.jpg", "image5.jpg", "image6.jpg", "image7.jpg", 
    "image8.jpg", "image9.jpg", "image10.jpg", "image11.jpg",
    "image12.jpg", "image13.jpg", "image14.jpg", "image15.jpg",
    "image16.jpg", "image17.jpg", "image18.jpg", "image19.jpg",
    "image20.jpg", "image21.jpg", "image22.jpg", "image23.jpg", "image24.jpg",
]
def check_if_all_files_exist(files):
    all_exist = all(os.path.exists(file) for file in files)
    return all_exist

def stitch_images_create_grid(video_folder, video_name):
    print(f"- Stitching extracted images together as a grid...")

    if check_if_all_files_exist(temp_screens):
        images = [Image.open(filename) for filename in temp_screens]
        width, height = images[0].size

        # Calculate the dimensions of the output image
        num_images = len(images)
        num_rows = (num_images + 4) // 5  # Three images per row
        output_width = width * 5
        output_height = height * num_rows

        # Create a new image with the calculated dimensions
        result_image = Image.new("RGB", (output_width, output_height))

        # Paste each image into the result image
        for i, img in enumerate(images):
            row = i // 5
            col = i % 5
            x_offset = col * width
            y_offset = row * height
            result_image.paste(img, (x_offset, y_offset))

        # Save the result image as a JPG file
        result_image.save(os.path.join(video_folder, video_name) + '.jpg', "JPEG")
    else:
        print(f"- Error, missing files for stitcher... skipping...")

if __name__ == "__main__":
    print(f"Function looks for images in executed folder, and creates .jpg in folder of videofile.")
