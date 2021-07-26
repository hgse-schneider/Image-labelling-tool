import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
import random
import readline


# directory face labelled csv is saved into
savedir = 'labelled_csv_files'

# ask user if they are working from a previously labelled dataframe
prev_dataframe_bool = input("Do you have a previous csv with partially labeled faces? [y/n] ")

# if previous csv exists, user types in name of csv and file is retrieved
# set relevant variables (all_folder_names such that all unlabeled folders are stored 
# in a list to be iterated through later, all_labels contains all previous labels for autofill)
if prev_dataframe_bool == "y":
	csv_name = input("What is the name of the csv? ")
	all_data_df = pd.read_csv(savedir + "/" + csv_name, index_col = 0)
	filtered_df = all_data_df[all_data_df['label'].isnull()]
	folder_names_list = filtered_df['folder_name'].tolist()
	all_folder_names = list(set(folder_names_list))
	all_prev_labels = [item for item in all_data_df["label"].tolist() if type(item) == str]
	all_labels = list(set(all_prev_labels))

# otherwise create new dataframe from directory files
else:
	rootdir = 'unlabelled_images'
	paths = []
	folder_names = []
	# get all filepaths associated with images in directory
	for subdir, dirs, files in os.walk(rootdir):
	    for file in files:
	        if subdir != rootdir and file != '.DS_Store':
	            filepath = str(os.path.join(subdir, file))
	            paths.append(filepath)
	            folder_name = subdir.split("unlabelled_images/")[1]
	            folder_names.append(folder_name)

	# get dataframe with viable filepaths and the associated name of subject
	dataframe_dict = {}
	dataframe_dict['folder_name'] = folder_names
	dataframe_dict['filepath'] = paths
	all_data_df = pd.DataFrame.from_dict(dataframe_dict)

	# create dummy column with which we will populate later with labels
	all_data_df["label"] = ""

	# get all unique folder names (each folder contains images of one subject)
	all_folder_names = list(set(folder_names))

	# list of known labels constantly updated for autofill
	all_labels = []

# autocomplete function
def completer(text, state):
	options = [x for x in all_labels if x.startswith(text)] + [text]
	try:
		return options[state]
	except IndexError:
	    return None

readline.set_completer(completer)
readline.parse_and_bind("tab: menu-complete")

# iterate through all folders
for folder in all_folder_names:
	# use array to track displayed images
    used_images = []
    user_input = ""
    
    skip_count = 0

    # get all images in folder
    all_photos_in_folder = all_data_df[(all_data_df['folder_name']==folder)]['filepath'].tolist()
    
    # while user does not type anything (presses Enter) display random image from folder
    while not user_input:
        if skip_count == 3:
        	break

        skip_count += 1

        file = random.choice(all_photos_in_folder)
        used_images.append(file)
        if file in used_images:
        	file = random.choice(all_photos_in_folder)

        # display image
        print("file: ", file)
        img=plt.imread(file,0)
        imgplot = plt.imshow(img)
        plt.title(file)
        plt.ion()  #Turn the interactive mode on.
        plt.show()
        plt.pause(0.001)

        # get user input
        print("name: ")
        user_input = input()
    
    # propagate user label to rest of photos in folder
    all_data_df.loc[all_data_df.folder_name==folder, 'label'] = user_input

    # add label to list of known labels
    if user_input not in all_labels:
    	all_labels.append(user_input)

print(all_data_df)

if prev_dataframe_bool == "y":
	# update labeled faces in local drive
	all_data_df.to_csv(savedir + "/" + csv_name)
	saved_filepath = savedir + "/" + csv_name

else:
	# get name of csv file under which labeled faces will be saved
	labelled_csv_file_name = input("Under what name would you like to save the csv file containing the labeled images? ")

	# save labeled faces df to local drive
	all_data_df.to_csv(savedir + "/" + labelled_csv_file_name)
	saved_filepath = savedir + "/" + labelled_csv_file_name

# print confirmation and csv name
print('Saved dataframe at ', saved_filepath)


