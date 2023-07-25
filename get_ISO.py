# This file gets the list of all Isotopologues from the HITRAN database
# and stores them in a file called "iso_list.txt"
# Make sure pandas and lxml module are installed before using this script

#####################
import pandas as pd #
#####################


def main():
    url="https://hitran.org/docs/iso-meta/"

    symbols = ['A','B','C','D','E','F','G','H','I']

    data=pd.read_html(url,header=0)

    species_id = []
    global_id = []
    isotope_no = []
    qfile = []
    Formula = []

    for j in range(len(data)):
        list=data[j].values.tolist()

        for i in range(len(list)):
            qfile.append(list[i][7])
            Formula.append(list[i][2])
            isotope_no.append(list[i][1])
            global_id.append(str(j+1))
            index = int(list[i][1])

            if (index > 10):
                index = symbols[(index%10)-1]

            species_id.append(str(j+1) + str(index))

    f = open("iso_list.txt","w")
    print("%-10s %-12s %-12s %-16s %-16s" % ("Global_id", "Isotope_id", "Species_id","Molecule_name","Q_file"), file = f)

    for i in range(len(species_id)):
        print("%-10s %-12s %-12s %-16s %-16s" % (global_id[i], isotope_no[i] ,species_id[i], Formula[i], qfile[i]), file = f)
    
    f.close()
    

if __name__ == '__main__':
    main()

