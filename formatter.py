import csv

with open('MukundaLog.txt','rb') as readf:
    reader = csv.reader(readf)
    with open('mukunda/14072015_Mukunda_Raw.csv','wb') as writef:
        writer = csv.writer(writef, delimiter=",")
        count = 0
        for row in reader:
            if len(row) == 2:
                splitrow1 = row[0].split("\t")
                splitrow2 = row[1].split('\t')
                splitrow = []
                tempcount = 1
                for element in splitrow1:
                    if len(splitrow1) == tempcount:
                        splitrow.append(element+" "+splitrow2[0])
                        tempcount2 = 0
                        for ele in splitrow2:
                            tempcount2 = tempcount2 + 1
                            if tempcount2 == 1:
                                continue
                            else:
                                splitrow.append(ele)
                    else:
                        splitrow.append(element)
                    tempcount = tempcount + 1
            else:
                splitrow = row[0].split("\t")            
            count = count + 1
            writer.writerow(splitrow)
        print "Wrote "+str(count)+" lines !"
    print "Created file !"
