import argparse

def get_input_args():
    """
    Retrieves and parses 3 command line arguments provided by the user:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
      
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - uses argparse to create and store command line arguments.
    Returns:
     parse_args() - data structure that stores the command line arguments object.
    """
    # Create a parser
    parser = argparse.ArgumentParser(description="Retrieve command line arguments for image classification program")

    # Add arguments with default values
    parser.add_argument('--dir', type=str, default='pet_images',
                        help='Path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg',
                        help='CNN model architecture to use for image classification')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='Text file containing dog names')

    # Return the parsed arguments
    return parser.parse_args()
