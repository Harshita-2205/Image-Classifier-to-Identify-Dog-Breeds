# Imports the classifier function
from classifier import classifier

def classify_images(images_dir, petlabel_dic, model):
    """
    Creates the classifier labels with the classifier function, compares labels
    to pet labels, and adds the results to the results dictionary.
    
    Parameters:
      images_dir - The (string) folder path to the images
      petlabel_dic - Dictionary with image filename as 'key' and pet image label as 'value'
      model - The CNN model architecture to use for classification ('resnet', 'alexnet', 'vgg')
    
    Returns:
      results_dic - Dictionary where key = image filename and value = [pet label, classifier label, match (1/0)]
    """
    # Initialize results dictionary
    results_dic = {}
    
    # Iterate over each filename and pet label in the petlabel_dic
    for filename, pet_label in petlabel_dic.items():
        # Create full path to the image file
        full_image_path = images_dir + "/" + filename
        
        # Get the classifier label using the classifier function
        classifier_label = classifier(full_image_path, model)
        
        # Process classifier label to match pet label format
        classifier_label = classifier_label.lower().strip()
        
        # Check if pet_label is in classifier_label
        match = 1 if pet_label in classifier_label else 0
        
        # Add entry to results_dic with pet_label, classifier_label, and match indicator
        results_dic[filename] = [pet_label, classifier_label, match]
    
    return results_dic
