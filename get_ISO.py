# This file gets the list of all Isotopologues from the HITRAN database
# and stores them in a file called "iso_list.txt"
# Make sure pandas and lxml module are installed before using this script

#####################
import pandas as pd #
#####################


def main():
    url="https://hitran.org/docs/iso-meta/"
    url_lbl = "https://hitran.org/lbl/2"

    symbols = ['A','B','C','D','E','F','G','H','I']

    data=pd.read_html(url,header=0)

    species_id = []
    global_id = []
    isotope_no = []
    qfile = []
    Formula = []
    nu_min = []
    nu_max = []

    for j in range(len(data)):

        if (j == 29 or j == 34 or j == 41 or j == 54):
            pass
        else:

            nu_url = url_lbl + '?' + f'{j+1}' + '=on' 
            nu_data=pd.read_html(nu_url,header=0)
            nu_data_list = nu_data[0].values.tolist()

        list=data[j].values.tolist()

        for i in range(len(list)):
            qfile.append(list[i][7])
            Formula.append(list[i][2])
            isotope_no.append(list[i][1])
            global_id.append(str(j+1))
            if (j == 29 or j == 34 or j == 41 or j == 54):
                nu_min.append("NA")
                nu_max.append("NA")

            else:

                nu_mi = str(nu_data_list[i][6]).replace('\xa0×\xa010', 'E')
                nu_min.append(nu_mi)
                nu_ma = str(nu_data_list[i][7]).replace('\xa0×\xa010', 'E')
                nu_max.append(nu_ma)
            
            index = int(list[i][1])

            if (index > 10):
                index = symbols[(index%10)-1]

            species_id.append(str(j+1) + str(index))

    f = open("iso_list.txt","w")
    print("%-10s %-12s %-12s %-16s %-16s %-16s %-16s" % ("Global_id", "Isotope_id", "Species_id","Molecule_name","Q_file", "nu_min", "nu_max"), file = f)

    for i in range(len(species_id)):
        print("%-10s %-12s %-12s %-16s %-16s %-16s %-16s" % (global_id[i], isotope_no[i] ,species_id[i], Formula[i], qfile[i], nu_min[i], nu_max[i]), file = f)
    
    f.close()
    

if __name__ == '__main__':
    main()

