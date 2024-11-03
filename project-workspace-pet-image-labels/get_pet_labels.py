from os import listdir

def get_pet_labels(image_dir):
    # Retrieve filenames from the directory
    filename_list = listdir(image_dir)
    
    # Dictionary to store filename as key and label list as value
    results_dic = {}
    
    for filename in filename_list:
        # Process only .jpg files
        if filename.endswith(".jpg"):
            # Convert filename to lowercase and split by '_'
            low_filename = filename.lower()
            word_list = low_filename.split("_")
            
            # Create pet_name from words that are only alphabetic
            pet_name = ""
            for word in word_list:
                if word.isalpha():
                    pet_name += word + " "
            
            # Strip trailing whitespace
            pet_name = pet_name.strip()
            
            # Add filename and pet_name to results_dic if unique
            if filename not in results_dic:
                results_dic[filename] = [pet_name]
            else:
                print(f"Warning: Duplicate filename detected: {filename}")
    
    return results_dic
