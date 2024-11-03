def print_results(results_dic, results_stats_dic, model, print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints a summary of the results, including overall counts and statistics.
    Optionally prints misclassified dogs and breeds.
    
    Parameters:
        results_dic (dict): Dictionary containing results of image classifications.
        results_stats_dic (dict): Dictionary containing calculated results statistics.
        model (str): The CNN model architecture being used.
        print_incorrect_dogs (bool): Whether to print misclassified dogs (default: False).
        print_incorrect_breed (bool): Whether to print misclassified breeds (default: False).
    
    Returns:
        None
    """
    # Print model architecture
    print(f"\nModel Architecture: {model}")
    
    # Print overall counts
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs']}")
    print(f"Number of 'Not-a' Dog Images: {results_stats_dic['n_not_dogs']}\n")
    
    # Print statistics
    print("Statistics:")
    for key in results_stats_dic:
        if key.startswith('pct_'):
            print(f"{key.replace('_', ' ').title()}: {results_stats_dic[key]:.2f}%")

    # Print misclassified dogs if requested
    if print_incorrect_dogs:
        n_correct_dogs = results_stats_dic['n_correct_dogs']
        n_correct_notdogs = results_stats_dic['n_correct_not_dogs']
        if n_correct_dogs + n_correct_notdogs != results_stats_dic['n_images']:
            print("\nMisclassified Dogs:")
            for key in results_dic:
                if sum(results_dic[key][3:]) == 1:  # Indicates misclassified dog
                    print(f"Pet label: {results_dic[key][0]}, Classifier label: {results_dic[key][1]}")

    # Print misclassified breeds if requested
    if print_incorrect_breed:
        n_correct_dogs = results_stats_dic['n_correct_dogs']
        n_correct_breeds = results_stats_dic['n_correct_breeds']
        if n_correct_dogs != n_correct_breeds:
            print("\nMisclassified Breeds:")
            for key in results_dic:
                if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:  # Indicates misclassified breed
                    print(f"Pet label: {results_dic[key][0]}, Classifier label: {results_dic[key][1]}")
