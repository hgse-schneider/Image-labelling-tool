# Image-labelling-tool
A python tool to label images for training supervised machine learning models. 

# Dependencies
* Python 3.3+ with numpy, matplotlib, pandas, os, random, and readline libraries

# Relevant Folders
* ```unlabelled_images```: directory that contains a labelled sub-directory for each tracked subject in the recorded video footage from the Makerspace. Each sub-directory contains images of the subject taken from frames of a video.
     
     *Local File Structure:*
     
        <unlabelled_images>/
        ├── <subject1>/
        │   ├── <subject1_image1>.jpeg
        │   ├── <subject1_image2>.jpeg
        │   ├── ...
        ├── <subject2>/
        │   ├── <subject2_image1>.jpeg
        │   └── <subject2_image2>.jpeg
        └── ...
* ```labelled_csv_files```: directory that contains all labelled csv files (in progress and completed)

# Usage

To use this image labelling tool, first navigate to the directory containing this github repository in your terminal. Run the python script ```face_recognition.py``` via the following command:
```
python face_recognition.py
```

You will be prompted with the following question:
```
Do you have a previous csv with partially labeled faces? [y/n] 
```

If you are labelling a new directory of images, type ```n```. If you are finishing the labelling process in a directory that still contains unlabeled subdirectories, type ```y``` and enter the name of the associated partially-labelled .csv file.

Next, a random image of the subject taken from their respective subdirectory in the file structure will pop up and in your terminal, you will be prompted with the field ```name:```. If you are unable to recognize the subject in the image, simply click ```Enter``` and leave the ```name:``` field blank. If you press ```Enter``` three times (that is, skip through three image of the subject), the script will assume you do not recognize the current subject and move on to the next subject. 

Otherwise, enter the name of the subject in the image. This entered name will then be propagated as the assigned label for all images in the given subdirectory. If you had previously entered the name of a given subject before, simply type the first few letters (at least one) of the label and press ```Tab``` to cycle through all past labels, clicking ```Enter``` when the desired name pops up.

After each subdirectory has been visited, the tool will save all labels in a .csv file (that you will be prompted to name) in the ```labelled_csv_files``` directory.
