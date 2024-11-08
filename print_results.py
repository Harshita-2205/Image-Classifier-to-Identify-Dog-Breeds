def print_results(results_dic, results_stats_dic, model, print_incorrect_dogs=True, print_incorrect_breed=True):
    """
    Prints a summary of the results, including overall counts and statistics.
    Optionally prints misclassified dogs and breeds.
    
    Parameters:
        results_dic (dict): Dictionary containing results of image classifications.
        results_stats_dic (dict): Dictionary containing calculated results statistics.
        model (str): The CNN model architecture being used.
        print_incorrect_dogs (bool): Whether to print misclassified dogs (default: True).
        print_incorrect_breed (bool): Whether to print misclassified breeds (default: True).
    
    Returns:
        None
    """
    # Print model architecture
    print(f"Model Architecture: {model}")
    
    # Print overall counts
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of 'Not-a' Dog Images: {results_stats_dic['n_notdogs_img']}\n")
    
    # Print statistics
    print("Statistics:")
    for key, value in results_stats_dic.items():
        if key.startswith('pct_'):
            # Format statistic keys to match required output style
            print(f"{key.replace('_', ' ').title()}: {value:.2f}%")

    # Print misclassified dogs if requested
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\nMisclassified Dogs:")
        for key, value in results_dic.items():
            if sum(value[3:]) == 1:  # Indicates misclassified dog
                print(f"Pet label: {value[0]}, Classifier label: {value[1]}")

    # Print misclassified breeds if requested
    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\nMisclassified Breeds:")
        for key, value in results_dic.items():
            if sum(value[3:]) == 2 and value[2] == 0:  # Indicates misclassified breed
                print(f"Pet label: {value[0]}, Classifier label: {value[1]}")
