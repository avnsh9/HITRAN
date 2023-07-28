# This script generate cross section using HELIOS-K 

import data_down
import argparse
import json
import subprocess

def main(molecule):
    out,gg,ii = data_down.main(molecule)
    param_data_4 = f'Species Name = {gg}_{ii}_{molecule}\n'

    with open('para')
    with open("parameters.json") as f:
        param = json.load(f)

    subprocess.run(['cp',f'{param["helios_k_executable"]}Hitran_species.dat','.'],cwd=param["kabs_out_folder"])
    with subprocess.Popen([f'{param["helios_k_executable"]}hitran','-M',f'{gg}','-ISO',f'{ii}','-in',f'{molecule}'],cwd=param["kabs_out_folder"],stdout=subprocess.PIPE) as p:
        while True:
            text = p.stdout.read().decode("utf-8")
            print(text, end='', flush=True)
            if text == '' and p.poll() != None:
                break

    print('done till bin file part\n Now deleting .par file')

    

    subprocess.run(['rm',f'{out}'],cwd=param["kabs_out_folder"])

    print('file deleted !!!!')

    # Generating cross sections

    subprocess.run(['cp','auto.sh','pt800.txt',f'{param["kabs_out_folder"]}'])

    subprocess.run(['chmod','+x','auto.sh'],cwd=param["kabs_out_folder"])

    with subprocess.Popen('./auto.sh',cwd=param["kabs_out_folder"],stdout=subprocess.PIPE) as p:
        while True:
            text = p.stdout.read().decode("utf-8")
            print(text,end='',flush=True)
            # if(text == '' and p.poll() != None):
            #     break

    print('cross-section generation is done')






if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-M',type=str,help="Molecule for which cross section needs to be calculated. Please enter molecule name in the same format as given in iso_list.txt file")
    args = parser.parse_args()
    molecule = args.M
    main(molecule)