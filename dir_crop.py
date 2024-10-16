from PIL import Image
import os
import sys
from optparse import OptionParser

def process_images(input_directory, output_directory="", target_width=768, target_height=512, **kwargs):

    """ Processes a directory for all its images, and makes sure they all have the same dimensions

    Arguments:
        input (str)     - Folder to scan
        output (str)    - Folder to save processed images in, defaults to input
        width (int)     - image width
        height (int)    - image height
    """
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get a list of all files in the input directory
    image_files = [f for f in os.listdir(input_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in image_files:
        input_path = os.path.join(input_directory, image_file)
        output_path = os.path.join(output_directory, image_file)

        # Open the image
        with Image.open(input_path) as img:
            # Get the original image dimensions
            original_width, original_height = img.size

            # Calculate cropping dimensions to maintain aspect ratio and center the crop
            left = max(0, (original_width - target_width) // 2)
            top = max(0, (original_height - target_height) // 2)
            right = min(original_width, left + target_width)
            bottom = min(original_height, top + target_height)

            # Crop the image
            cropped_img = img.crop((left, top, right, bottom))

            # Save the cropped image
            cropped_img.save(output_path)

if __name__ == "__main__":

    # positional parameters
    if len(sys.argv) > 1:
        if sys.argv[1] != '-i':
            if len(sys.argv) > 2:
                input_directory = sys.argv[1]
                output_directory = sys.argv[2]
                process_images(input_directory, output_directory)
            elif len(sys.argv) > 1:
                input_directory = sys.argv[1]
                process_images(input_directory, input_directory)
            raise SystemExit

    # named parameters
    parser = OptionParser()
    parser.add_option("-i", "--input",
                      dest="input_directory",
                      help="Folder to crop images",
                      type="string",
                      action="store"
                      )
    parser.add_option("-o", "--output",
                      dest="output_directory",
                      help="Folder to save cropped images, defaults to input folder",
                      type="string",
                      action="store"
                      )
    parser.add_option("-x", "--width",
                      dest="target_width",
                      help="Default width for images",
                      default="768",
                      type="int",
                      action="store"
                      )
    parser.add_option("-y", "--height",
                      dest="target_height",
                      help="Default height for images",
                      default="512",
                      type="int",
                      action="store"
                      )
    (options, args) = parser.parse_args()

    def bailout():
        parser.print_help()
        print("\n" + 'Example:' + "\n" + 'python dir_crop.py input_dir output_dir' + "\n" + 'python dir_crop.py -i path -o path -x 512 -y 512' + "\n")
        raise SystemExit

    if not options.input_directory:
        bailout()

    if options.output_directory == None:
        options.output_directory = options.input_directory

    process_images(**options.__dict__)

