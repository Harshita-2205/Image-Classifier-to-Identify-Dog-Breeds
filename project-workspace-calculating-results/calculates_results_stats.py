def calculates_results_stats(results_dic):
    """
    Calculates the results statistics based on the results dictionary.
    
    Parameters:
        results_dic (dict): Dictionary containing results of image classifications.
    
    Returns:
        results_stats_dic (dict): Dictionary containing statistics (counts and percentages).
    """
    
    # Initialize the results statistics dictionary
    results_stats_dic = {}
    
    # Initialize counts
    n_images = len(results_dic)
    n_correct_dogs = 0
    n_dogs = 0
    n_correct_not_dogs = 0
    n_not_dogs = 0
    n_correct_breeds = 0
    
    # Iterate through results dictionary
    for key in results_dic:
        # Unpack results
        is_dog_image = results_dic[key][3]
        is_classified_dog = results_dic[key][4]
        labels_match = results_dic[key][2]
        
        # Count dogs
        if is_dog_image == 1:
            n_dogs += 1
            if labels_match == 1:  # Correctly classified breed
                n_correct_breeds += 1
            n_correct_dogs += is_classified_dog  # Increment if classified correctly as a dog

        # Count non-dogs
        else:
            n_not_dogs += 1
            n_correct_not_dogs += 1 if is_classified_dog == 0 else 0  # Correctly classified as not a dog
    
    # Calculate percentages
    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_dogs'] = n_dogs
    results_stats_dic['n_correct_not_dogs'] = n_correct_not_dogs
    results_stats_dic['n_not_dogs'] = n_not_dogs
    results_stats_dic['n_correct_breeds'] = n_correct_breeds

    # Calculate percentages
    results_stats_dic['pct_correct_dogs'] = (n_correct_dogs / n_dogs * 100) if n_dogs > 0 else 0
    results_stats_dic['pct_correct_not_dogs'] = (n_correct_not_dogs / n_not_dogs * 100) if n_not_dogs > 0 else 0
    results_stats_dic['pct_correct_breeds'] = (n_correct_breeds / n_dogs * 100) if n_dogs > 0 else 0

    return results_stats_dic
