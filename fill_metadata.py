import csv

##Input and Output File Names
INPUT_FILE = "mukunda/18072015_Mukunda_Raw.csv"
OUTPUT_FILE = "mukunda/18072015_Mukunda_Processed.csv"

##Required Dictionaries
url_dict = {"//www.google.com":"s","//www.google.co.in":"s", "youtube.com":"yt", "//mail.google.com":"gm"}
meta_dict = {}
count = 0

## Read meta-data from 'metadata.csv' file and create a dictionary (meta_dict)
with open('Metadata2.csv','rb') as metaf:
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
with open(OUTPUT_FILE,'wb') as genfw:
    genwriter = csv.writer(genfw, delimiter=",")
    genwriter.writerow(["Timestamp","Course Name","Module","Problem","Duration","Content Type","URL","Event Type","Event Data"])
    print "Analyzing data..."
    ##Open 'VedaJava.csv' file for reading Veda's logs.
    with open(INPUT_FILE,'rb') as dataf:
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
                else:
                    ##Identifying type_of URL
                    if(len(row[6])>0):
                        for key in url_dict.keys():
                            if key in row[6]:
                                row[2] = url_dict[key]
                                break
                            else:
                                row[2] = "other"
                ##Timestamp truncation to HH:MM
                row[0] = row[0][row[0].find(" ")+1:row[0].rfind(":")]
                ##Identify No.Of Occurances based on EventType
                print "-------------",row[7],row[8]
                if row[7].strip(' \t\r\n') == "Mouse":
                    print "Mouse ",row[7]
                    row[8] = row[8].strip(' \t\r\n').count("MOUSE3:")
                elif row[7].strip(' \t\r\n') == "Selected":
                    row[8] = "1"
                elif row[7].strip(' \t\r\n') == "Key":
                    row[8] = len(row[8])
                    print "Key ",row[8]
                genwriter.writerow(row)
            
print "Done !"
print "Created output.csv file !"
#print url_dict
#print url_dict.keys()

