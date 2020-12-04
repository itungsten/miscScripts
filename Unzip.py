import zipfile
import re
zipname = "newdir/"+"f.zip"
while True:
    if zipname != "newdir/73168.zip":
        ts1 = zipfile.ZipFile(zipname)
        res = re.search('[0-9]*',ts1.namelist()[0])
        print res.group()
        passwd = res.group()
        ts1.extractall("newdir",pwd=passwd)
        zipname = "newdir/"+ts1.namelist()[0]
    else:
        print "find"