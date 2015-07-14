import csv

meta_dict = {}
count = 0
## Read meta-data from 'metadata.csv' file and create a dictionary (meta_dict)
with open('Metadata.csv','rb') as metaf:
    metareader = csv.reader(metaf)
    for row in metareader:
        count = count + 1
        if count == 1:
            continue
        if len(row[0])>0:
            meta_dict[row[4]] = row
print "Generated META-DATA"

count = 0
##Create a file 'output.csv' to write results.
with open('output.csv','wb') as genfw:
    genwriter = csv.writer(genfw, delimiter=",")
    genwriter.writerow(["Timestamp","Course Name","Module","Problem","Duration","Content Type","URL","Event Type","Event Data"])
    print "Analyzing data..."
    ##Open 'VedaJava.csv' file for reading Veda's logs.
    with open('VedaJava.csv','rb') as dataf:
        datareader = csv.reader(dataf)
        for row in datareader:
            count = count + 1
            if count == 1:
                continue
            if len(row[0])>0:
                ##If URL from Veda's log matches the URL found in metadata (meta_dict)
                ##  then enter meta-data to the existing row array and write to file.
                ##Else write the same row array to file
                if row[6] in meta_dict:                    
                    row[1] = meta_dict[row[6]][0]
                    row[2] = meta_dict[row[6]][1]
                    row[5] = meta_dict[row[6]][3]
                    genwriter.writerow(row)
                else:
                    genwriter.writerow(row)               
print "Done !"
print "Created output.csv file !"
