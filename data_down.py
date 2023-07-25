# First download hitran-api module using pip before using this script
# Download API from github which is more up to date rather than pip
# This script download user requested line list and partition function corresponding to that

#####################
from hapi import *  #
import numpy as np  #
import os           #
import json         #
import get_ISO
#####################
def assign_db():
        with open("parameters.json") as f:
            param = json.load(f)

        db_begin(param["database_folder"])
        
def main():

    # Check if iso_list.txt file exist or not
    # if not then create it using get_ISO.py

    avail = os.path.isfile("iso_list.txt")
    print(avail)
    if (avail == 0):
        print("iso_list.txt file is not available \nRunning get_ISO.py to generate iso_list.txt\n")
        get_ISO.main()

    
    # getting database folder from parameters file
    
    
    assign_db()

    # Downloading line list data

    def download_ll(molecule):
        GI, ISO_I, Mol = np.loadtxt("iso_list.txt", usecols=(0,1,3), unpack=True)

    

if __name__ == '__main__':
    main()