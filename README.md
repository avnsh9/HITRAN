
# HITRAN_automate

This repo automate the process of cross section calculation using HITRAN line list (actual calculation is done using HELIOS-K)

This takes care of all the steps like line list download, download partition function, create binary files and running the HELIOS-K





## Things to do before use

### Libraries required
 - Python > 3.6
 - HELIOS-K must be installed and properly configured
 - Hitran-API (HAPI) >= 1.2.2.1 pip version is not recommended, use github version
 - Latest pandas
 - Latest numpy


### Set parameters
Use parameters.json file to set these parameters:
- database_folder : This is the folder where all your line lists will be downloaded
- kabs_out_folder : Set this to a folder where you want to take the output of your calculated cross sections

- helios_k_executable : Set this to the folder where your heliosk and hitran executables are located

## Things to know for current version:
- Whole line list is downloaded with numin and numax as available on HITRAN server
- 800 pressure,temperature grid points are being used to generate cross section
- Generated cross section is from 0.05 m-1 to 5000000 m-1


## Uses

python kabs_gen.py -M `<molecule>`

- Use molecule name as given in iso_list.txt file
- There are certain molecules whose corresponding files are not available on HITRAN server, they are mentioned with "NA" in iso_list file
- stdout of the running program is not piped, so you have to use htop in order to keep track of the progress
## Acknowledgements

 - [R.V. Kochanov, I.E. Gordon, L.S. Rothman, P. Wcislo, C. Hill, J.S. Wilzewski, HITRAN Application Programming Interface (HAPI): A comprehensive approach to working with spectroscopic data, J. Quant. Spectrosc. Radiat. Transfer 177, 15-30 (2016)](https://linkinghub.elsevier.com/retrieve/pii/S0022407315302466)
 

- [{{Grimm}, Simon L. and {Malik}, Matej and {Kitzmann}, Daniel and {Guzm{\'a}n-Mesa}, Andrea and {Hoeijmakers}, H. Jens and {Fisher}, Chloe and {Mendon{\c{c}}a}, Jo{\~a}o M. and {Yurchenko}, Sergey N. and {Tennyson}, Jonathan and {Alesina}, Fabien and {Buchschacher}, Nicolas and {Burnier}, Julien and {Segransan}, Damien and {Kurucz}, Robert L. and {Heng}, Kevin}](https://ui.adsabs.harvard.edu/abs/2021ApJS..253...30G)
