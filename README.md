# Image_Cation_Generation_NLP

Final Project - Group 6 - John O’Connell

The files included in this submission are:
	•	GROUP6_feature_extractor.ipynb - The VGG19 feature extractor, included as a notebook file to enable running each piece separately
	•	GROUP6_feature_extractor.py - The VGG19 feature extractor, included as a python file to run all at once
	•	features.pkl - A pickle file of the dictionary created by the feature extractor
	•	GROUP6_model_final.ipynb - The final model in notebook form. Can be run to replicate the results of this project
	•	GROUP6_model_all_in.ipynb - This file is the model with additional code added for data collection and demonstration purposes
	•	final_model.h5 - The final model used in the presentation and paper
	•	GROUP6_final_report

IMPORTANT:
In order to run the model successfully, you will need to download the Flickr8k dataset. The dataset can be found at the following link:
https://www.kaggle.com/datasets/adityajn105/flickr8k
Once downloaded, make sure the name of the directory containing the files is ‘flickr8k’. Place this ‘flickr8k’ directory in into a folder
named 'data', and place this 'data' folder into the same folder as the code. If done correctly, the ‘data’ directory should contain a 
subdirectory named 'flickr8k', and the 'flickr8k' subdirectory should contain two items - a file named ‘captions.txt’, and a subdirectory 
named ‘images’ which contains all the images of the dataset. 
