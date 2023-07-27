# This script generate cross section using HELIOS-K 

import data_down
import argparse

def main(molecule):
    data_down.main(molecule)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-M',type=str,help="Molecule for which cross section needs to be calculated. Please enter molecule name in the same format as given in iso_list.txt file")
    args = parser.parse_args()
    molecule = args.M
    main(molecule)