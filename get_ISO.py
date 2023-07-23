# This file gets the list of all Isotopologues from the HITRAN database
# and stores them in a file called "iso_list.txt"

#####################
import pandas as pd #
#####################


def main():
    url="https://hitran.org/docs/iso-meta/"

    symbols = ['A','B','C','D','E','F','G','H','I']

    data=pd.read_html(url,header=0)

    iso = []
    qfile = []
    Formula = []

    for j in range(len(data)):
        list=data[j].values.tolist()

        for i in range(len(list)):
            qfile.append(list[i][7])
            Formula.append(list[i][2])
            index = int(list[i][1])

            if (index > 10):
                index = symbols[(index%10)-1]

            iso.append(str(j+1) + str(index))

    f = open("iso_list.txt","w")
    print("%-4s %-8s %-16s %-16s" % ("No.","ISO_no","Molecule","Q_file"), file = f)

    for i in range(len(iso)):
        print("%-4d %-8s %-16s %-16s" % (i+1,iso[i],Formula[i],qfile[i]), file = f)
    
    f.close()
    

if __name__ == '__main__':
    main()

