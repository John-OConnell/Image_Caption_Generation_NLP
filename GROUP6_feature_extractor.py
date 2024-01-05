# import necessary libraries
import os
import pickle
from keras.applications.vgg16 import VGG16 , preprocess_input
from keras.models import Model
from keras_preprocessing.image import load_img , img_to_array

# map to directory with image flies
IMAGE_DIR = '../data/flickr8k/images'

# load vgg16 model
cnn = VGG19()

# restructure the model
# the last layer (fully connected layer) is not needed
cnn = Model(inputs = cnn.inputs , outputs = cnn.layers[-2].output)

# extract features from image
features = {}
directory = IMAGE_DIR

# loop through all images in directory
for img_name in os.listdir(directory):
    # load the image from file
    img_path = directory + '/' + img_name
    image = load_img(img_path, target_size=(224, 224))

    # convert image pixels to numpy array
    image = img_to_array(image)

    # reshape data for model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    # preprocess image for vgg
    image = preprocess_input(image)

    # extract features
    feature = cnn.predict(image, verbose=0)

    # get image ID
    image_id = img_name.split('.')[0]

    # store feature
    features[image_id] = feature

# save features to a pickle file
file = open('features.pkl', 'wb')
pickle.dump(features, file)
file.close()
