#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Morris Herbert
# DATE CREATED: Nov 21, 2019                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = dict()

    # Alternate approach using comprehension, works but skips "." and duplicate name detection
    # results_dic = {fileName: [fileName[:fileName.rfind('_')].replace('_', ' ').strip().lower()] for fileName in listdir(image_dir)}

    # @Debug: Note: limit to speed debugging, -1 not used
    limit = -1

    # process each file name and add to dict
    for fileName in listdir(image_dir):
        if fileName[0] == ".": #skip file names that start with .
            continue

        # create dog name as specified
        dog_name = fileName[:fileName.rfind('_')].replace('_', ' ').strip().lower()

        # check for dup files names (should not happen)
        if fileName not in results_dic:
            results_dic[fileName] = [dog_name]
        else:
            print("** Warning: Duplicate files exist in directory:", fileName)
        
        # @Debug: Limit process to speed debugging 
        limit = limit-1
        if limit == 0: break

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
