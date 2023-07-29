# First download hitran-api module using pip before using this script
# Download API from github which is more up to date rather than pip
# This script download user requested line list and partition function corresponding to that

#####################
from hapi import *  #
import numpy as np  #
import os           #
import json         #
import get_ISO      #
import subprocess
#####################

molecule="H216O"
def assign_db():
        with open("parameters.json") as f:
            param = json.load(f)

        db_begin(param["database_folder"])
        
def main(molecule):

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

    
    

    def mol_params(molecule):
        GI, ISO_I, Mol, q_file, nu_min, nu_max= np.loadtxt("iso_list.txt", usecols=(0,1,3,4,5,6), unpack=True, dtype='str')
        g = GI[Mol == molecule]
        i = ISO_I[Mol == molecule]
        min = nu_min[Mol == molecule]
        max = nu_max[Mol == molecule]
        q = q_file[Mol == molecule]
        return g,i,min,max,q
         

    def download_ll(molecule, g, i , min, max):
        fetch(molecule, g, i , min, max)
        
    g,i,min,max,q = mol_params(molecule)

    download_ll(molecule,int(g[0]),int(i[0]),float(min[0]),float(max[0]))

    # convert downloaded data to .par format
    with open("parameters.json") as f:
        param = json.load(f)

    dd = g[0]
    ii = int(i[0])

    symbols = ['A','B','C','D','E','F','G','H','I']

    if (ii>10):
        ii = symbols[(ii%10)-1]
    if (int(g[0])<10):
         dd = f'0{g[0]}'
    file = f'{molecule}.data'
    out_file = f'{param["kabs_out_folder"]}{dd}_{molecule}.par'
    subprocess.run(['cp',file,out_file],cwd=param["database_folder"])

    # Download partition file
    url_q = f'https://hitran.org/data/Q/{q[0]}'
    subprocess.run(['wget',f'{url_q}'],cwd=param["kabs_out_folder"])

    return out_file,dd,ii



    

if __name__ == '__main__':
    main(molecule)