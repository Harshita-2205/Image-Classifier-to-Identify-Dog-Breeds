from classifier import classifier
import os.path
def classify_images(images_dir, results_dic, model):
    """
    Creates the classifier labels with the classifier function, compares labels
    to pet labels, and adds the results to the results dictionary.
    
    Parameters:
      images_dir - The (string) folder path to the images
      results_dic - Dictionary with image filename as 'key' and pet image label as 'value'
      model - The CNN model architecture to use for classification ('resnet', 'alexnet', 'vgg')
    
    Returns:
      results_dic - Dictionary where key = image filename and value = [pet label, classifier label, match (1/0)]
    """
    # Iterate over each filename and pet label in the results_dic
    for filename, result in results_dic.items():
        pet_label = result[0]  # pet label should be the first element in the list
        # Ensure pet_label is a string and strip leading/trailing whitespaces
        pet_label = pet_label.strip() if isinstance(pet_label, str) else pet_label
        
        # Create full path to the image file
        full_image_path = os.path.join(images_dir, filename)
        
        # Get the classifier label using the classifier function
        classifier_label = classifier(full_image_path, model)
        
        # Process classifier label to match pet label format
        classifier_label = classifier_label.lower().strip()
        
        # Check if pet_label is in classifier_label
        match = 1 if pet_label in classifier_label else 0
        
        # Add entry to results_dic with pet_label, classifier_label, and match indicator
        results_dic[filename] = [pet_label, classifier_label, match]
    
    return results_dic
