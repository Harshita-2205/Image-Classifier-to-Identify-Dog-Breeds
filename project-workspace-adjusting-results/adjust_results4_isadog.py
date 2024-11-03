def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier 
    labels and pet image labels are 'a dog' or 'not a dog'.
    
    Parameters:
      results_dic - Dictionary with pet image filenames as keys 
                    and a list as value containing:
                    index 0 = pet image label
                    index 1 = classifier label
                    index 2 = 0/1 where 1 = labels match, 
                    0 = labels don't match
      dogfile - The filename of the file containing the dog names
    
    This function modifies results_dic in-place. It does not return anything.
    """

    # Initialize a dictionary to store dog names
    dognames_dic = {}

    # Open and read dog names from the provided file
    with open(dogfile, 'r') as f:
        for line in f:
            dog_name = line.rstrip()  # Remove trailing newline characters
            if dog_name in dognames_dic:
                print(f"Warning: Duplicate dog name found - {dog_name}")
            else:
                dognames_dic[dog_name] = 1  # Value is arbitrary, just to mark the name as present

    # Iterate through results_dic to determine if labels are dogs
    for key in results_dic:
        pet_label_is_dog = 1 if results_dic[key][0] in dognames_dic else 0
        classifier_label_is_dog = 1 if results_dic[key][1] in dognames_dic else 0
        
        # Extend the results list with dog/not-dog classification
        results_dic[key].extend([pet_label_is_dog, classifier_label_is_dog])
