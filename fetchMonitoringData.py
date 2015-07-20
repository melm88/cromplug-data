import urllib
import json
import csv
from operator import itemgetter

###############################################
## TO BE FILLED BEFORE RUNNING THE PROGRAM  ###
###############################################
FILE_NAME = "Mukunda"
DATE_FIELD = "18/07/2015"  ## DD/MM/YYYY
USER_ID = "mukunda-PC"     ## System Name
EMAIL_ID = "mukundareddy94@gmail.com"
###############################################


########################################################
## CHECK for getpydata
def preparePykeylog():
  url = "https://activity-log-tmt.appspot.com/getpydata"
  temp_params = {'user':USER_ID}
  params = urllib.urlencode(temp_params)
  response = urllib.urlopen(url, params)
  tempdict = json.loads(response.read())
  majordict = tempdict['data']
  firstdict = majordict[0]
  return majordict
########################################################


#########################################################
## CHECK for getforekey
def prepareForekeylog():
  url = "https://activity-log-tmt.appspot.com/getforekey"
  temp_params = {'username':USER_ID}
  params = urllib.urlencode(temp_params)
  response = urllib.urlopen(url, params)
  tempdict = json.loads(response.read())
  majordict = tempdict['data']
  return majordict
#########################################################


###########################################################
## CHECK for getdigistate
def getDigilog(): 
  url = "https://activity-log-tmt.appspot.com/getdigistate"
  temp_params = {'user':USER_ID}
  params = urllib.urlencode(temp_params)
  response = urllib.urlopen(url, params)
  tempdict = json.loads(response.read())
  #print tempdict
  #majordict = tempdict['action']
  #print majordict
  return tempdict
###########################################################


############################################################
## CHECK for getchromedata
def getChromelog():
  url = "https://activity-log-tmt.appspot.com/getchromedata"
  temp_params = {'useremail':EMAIL_ID}
  params = urllib.urlencode(temp_params)
  response = urllib.urlopen(url, params)
  tempdict = json.loads(response.read())
  majordict = tempdict['data']
  return majordict
############################################################


############################################################
##   WRITING TO FILE                                     ###
############################################################

def ValConvert(val):
  if type(val).__name__ == 'unicode':
    return val.encode('utf8')
  elif type(val).__name__ == 'str':
    return val
  else:
    return str(val)

## Writing data from CHROME to a file
def writeChromelog(majordict):
  with open(FILE_NAME+'_chrome.csv','wb') as writef:
    writer = csv.writer(writef, delimiter=',')
    arr = ["TimeStamp", "Course Name", "Module", "Problem", "Duration", "Content Type", "Url", "eventtype", "eventdata"]
    writer.writerow(arr)
    megalist = []
    for row in majordict:
      if DATE_FIELD in row['eventtime']:
        temparr = []
        temparr.append(row['eventtime'])
        temparr.append("")
        temparr.append("")
        temparr.append("")
        temparr.append("")
        temparr.append("")
        temparr.append(row['url'])
        temparr.append(row['eventtype'])
        temparr.append(ValConvert(row['eventdata']))
        temparr.append(row['email'])
        megalist.append(temparr)
    writer.writerows(sorted(megalist, key=itemgetter(0)))


## Writing data from PYKEYLOG to a file
def writePykeylog(majordict):
  with open(FILE_NAME+'_pykeylog.csv','wb') as writef:
    writer = csv.writer(writef, delimiter=',')
    arr = ["TimeStamp", "Username", "Windowtitle", "Log Data"]
    writer.writerow(arr)
    megalist = []
    for row in majordict:
      if DATE_FIELD in row['timeStamp']:
        temparr = []
        temparr.append(row['timeStamp'])
        temparr.append(row['username'])
        temparr.append(row['windowtitle'])
        temparr.append(row['datas'])
        megalist.append(temparr)
    writer.writerows(sorted(megalist, key=itemgetter(0)))

## Writing data from FOREKEYLOG to a file
def writeForelog(majordict):
  with open(FILE_NAME+'_forekeylog.csv','wb') as writef:
    writer = csv.writer(writef, delimiter=',')
    arr = ["StartTime", "EndTime", "AppTitle", "App Duration", "App Path"]
    writer.writerow(arr)
    megalist = []
    temp_split = DATE_FIELD.split("/")
    check_date = temp_split[2]+"/"+temp_split[1]+"/"+temp_split[0]
    for row in majordict:
      if check_date in row['starttime'][:row['starttime'].find('.')]:
        temparr = []
        temparr.append(row['starttime'][:row['starttime'].find('.')])
        temparr.append(row['endtime'][:row['endtime'].find('.')])
        temparr.append(row['apptitle'])
        temparr.append(row['appduration'])
        temparr.append(row['apppath'])
        megalist.append(temparr)
    writer.writerows(sorted(megalist, key=itemgetter(0)))


## Writing data from DIGISTATE to a file
def writeDigilog(tempdict):
  with open(FILE_NAME+'_digistatelog.csv','wb') as writef:
    writer = csv.writer(writef, delimiter=',')
    arr = ["TimeStamp", "Action"]
    writer.writerow(arr)
    actions = tempdict['action']
    timestamps = tempdict['timestamp']
    megalist = []
    temp_split = DATE_FIELD.split("/")
    check_date = temp_split[2]+"-"+temp_split[1]+"-"+temp_split[0]
    for x in range(len(actions)):
      if check_date in timestamps[x]:
        temparr = []
        temparr.append(timestamps[x])
        temparr.append(actions[x])
        megalist.append(temparr)
    writer.writerows(sorted(megalist, key=itemgetter(0)))
    

def startPoint():
  print "Preparing..."
  writeChromelog(getChromelog())
  print "Created Chrome_Log"
  writePykeylog(preparePykeylog())
  print "Created Pykey_Log"
  writeForelog(prepareForekeylog())
  print "Created Forekey_Log"
  writeDigilog(getDigilog())
  print "Created DigiProc_Log"
  print "Created [ALL] CSV files !!"

#Run main() on direct RUN
if __name__ == '__main__':
    startPoint()
    
   
