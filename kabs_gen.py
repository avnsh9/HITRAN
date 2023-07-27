# This script generate cross section using HELIOS-K 

import data_down
import argparse
import json
import subprocess

def main(molecule):
    data_down.main(molecule)
    with open("parameters.json") as f:
        param = json.load(f)

    subprocess.run(['cp',f'{param["helios_k_executable"]}Hitran_species.dat','.'],cwd=param["kabs_out_folder"])
    with subprocess.Popen([f'{param["helios_k_executable"]}hitran','-M','01','-ISO','5','-in','HD18O'],cwd=param["kabs_out_folder"],stdout=subprocess.PIPE) as p:
        while True:
            text = p.stdout.read().decode("utf-8")
            print(text, end='', flush=True)
            if text == '' and p.poll() != None:
                break

    print('done')




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-M',type=str,help="Molecule for which cross section needs to be calculated. Please enter molecule name in the same format as given in iso_list.txt file")
    args = parser.parse_args()
    molecule = args.M
    main(molecule)