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

    # Initialize a set to store dog names (faster lookup)
    dognames_set = set()

    # Try opening the dog names file and reading it
    try:
        with open(dogfile, 'r') as f:
            for line in f:
                dog_name = line.rstrip()  # Remove trailing newline characters
                if dog_name in dognames_set:
                    print(f"Warning: Duplicate dog name found - {dog_name}")
                else:
                    dognames_set.add(dog_name)
    except FileNotFoundError:
        print(f"Error: The file {dogfile} was not found.")
        return  # Exit if file is not found

    # Iterate through results_dic values to determine if labels are dogs
    for value in results_dic.values():
        pet_label_is_dog = 1 if value[0] in dognames_set else 0
        classifier_label_is_dog = 1 if value[1] in dognames_set else 0
        
        # Extend the results list with dog/not-dog classification
        value.extend([pet_label_is_dog, classifier_label_is_dog])
