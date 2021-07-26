# Image-labelling-tool
A python tool to label images for training supervised machine learning models. 

# Dependencies
* Python 3.3+ with numpy, matplotlib, pandas, os, random, and readline libraries

# Relevant Folders
* unlabelled_images: directory that contains a labelled sub-directory for each tracked subject in the recorded video footage from the Makerspace. Each sub-directory contains images of the subject taken from frames of a video.
     
     Structure:
        <unlabelled_images>/
        
        ├── <subject1>/
        
        │   ├── <subject1_image1>.jpeg
        
        │   ├── <subject1_image2>.jpeg
        
        │   ├── ...
        
        ├── <subject2>/
        
        │   ├── <subject2_image1>.jpeg
        
        │   └── <subject2_image2>.jpeg
        
        └── ...
* labelled_csv_files: directory that contains all labelled csv files (in progress and completed)
