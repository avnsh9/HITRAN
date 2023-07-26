# First download hitran-api module using pip before using this script
# Download API from github which is more up to date rather than pip
# This script download user requested line list and partition function corresponding to that

#####################
from hapi import *  #
import numpy as np  #
import os           #
import json         #
import get_ISO      #
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

    molecule="HD180"
    

    def mol_params(molecule):
        GI, ISO_I, Mol, nu_min, nu_max= np.loadtxt("iso_list.txt", usecols=(0,1,3,5,6), unpack=True, dtype=str)
        g = GI[Mol == molecule]
        i = ISO_I[Mol == molecule]
        min = nu_min[Mol == molecule]
        max = nu_max[Mol == molecule]
        return g,i,min,max
         

    def download_ll(molecule, g, i , min, max):
        fetch(molecule, g, i , min, max)
        
    g,i,min,max = mol_params(molecule)
    print(g,i,min,max)
    # download_ll(molecule,int(g),int(i),float(min),float(max))
         
        


    

if __name__ == '__main__':
    main()