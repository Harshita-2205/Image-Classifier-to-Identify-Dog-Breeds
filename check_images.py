# Imports python modules
from time import time
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Start time for program runtime
    start_time = time()
    
    # Get input arguments
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Create the results dictionary
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    # Classify images and add results to the dictionary
    # Updated function call in main
    results_dic = classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)

    # Adjust results for dog classifications
    # Call the adjust_results4_isadog function in the main() function
    adjust_results4_isadog(results_dic, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    # Calculate results statistics
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)
    print("\n")

    # Print summary results and errors (if any)
    # Call to print_results() in main function
    print_results(results_dic, results_stats, in_arg.arch, print_incorrect_dogs=True, print_incorrect_breed=True)

    
    # Measure total program runtime by collecting end time
    end_time = time()
    
    # Calculate and print the runtime in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          f"{int(tot_time // 3600)}:{int((tot_time % 3600) // 60)}:{int(tot_time % 60)}")

# Call to main function to run the program
if __name__ == "__main__":
    main()
