import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import shutil

class Dataset:
    '''
    Dataset class

    This class is for loading dataset and preparation. Aims to make work easier, for dividing images to cloud and non-cloud folders.

    Usage
    =============
    ds = Dataset(folder="images/") # Note the compulsory '/' after path
    # To show 2 images as samples
    ds.show_samples()
    # To save images to cloud and non-cloud folder
    ds.show()

    Parameters
    ==============
    1. folder: (default="images/"), type=str

    Functions
    ==============
    1. read_images()
        Reads images into a list: self.images
    2. show_samples()
        Shows 2 images samples as matplotlib subplot
    3. show()
        Shows images one by one, press C/c to save to cloud folder and N/n to save to non-cloud folder.

    TODO
    ==============
    1. Make data preparation function

    '''
    def __init__(self, folder="images/"):
        self.path = folder
        self.files = [x for x in os.listdir(self.path) if x.endswith('.jpg') or x.endswith('.jpeg') or x.endswith('.png')]
        self.images = []

    def read_images(self):
        '''
        This function reads images from the folder path, and saves to a list (self.images)

        Parameters
        ==============
        None

        Returns
        ==============
        None
        '''

        # Iterate through all the files
        for file in self.files:
            file = self.path + file

            # Read Image
            img = cv2.imread(file, 1)

            if(img is None):
                print("Error reading file: {}, skipping...".format(file))
                continue

            # Append to the list
            self.images.append(img)

        print("Finished reading {} images".format(len(self.images)))

    def show_samples(self):
        '''
        This function shows 2 images as samples using matplotlib subplot.

        Parameters
        ==============
        None

        Returns
        ==============
        None
        '''

        # Call read images function
        self.read_images()

        # Make a subplot and plot both images
        fig, axs = plt.subplots(2)
        axs[0].axis("off")
        axs[1].axis("off")
        axs[0].imshow(cv2.cvtColor(self.images[0], cv2.COLOR_BGR2RGB))
        axs[1].imshow(cv2.cvtColor(self.images[1], cv2.COLOR_BGR2RGB))
        plt.show()

    def show(self):
        '''
        Shows all images one by one.
        Press c/C to save to cloud folder.
        Press n/N to save to non-cloud folder.

        Folders saved to: <folder_path>/cloud and <folder_path>/non-cloud

        For default case: images/cloud and images/non-cloud
        '''

        # Create sub-folders if they don't exist
        for folders in ["cloud", "non-cloud"]:
            if(os.path.exists(self.path + folders) is False):
                os.makedirs(self.path + folders)

        for index, img in enumerate(self.images):
            cv2.imshow("Image", img)
            k = cv2.waitKey(0)
            if(k == ord('C') or k == ord('c')):
                shutil.copyfile(self.path + self.files[index], self.path + "cloud/" + self.files[index])
            elif(k == ord('n') or k == ord('N')):
                shutil.copyfile(self.path + self.files[index], self.path + "/non-cloud/" + self.files[index])
            cv2.destroyAllWindows()
            print("Index: {} finished of {}".format(index+1, len(self.images)))

if __name__ == "__main__":
    ds = Dataset("images/")
    ds.show_samples()
    ds.show()
