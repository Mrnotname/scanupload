#modul scanner

import urllib

def scanuploader(target,wordlist):
    buka = open(wordlist,'r')
    daftar = buka.read().split("\n")
    buka.close()

    for dir in daftar:
        alamat = target+"/"+dir
        
        bukaurl = urllib.urlopen(alamat) #return 'opener.open(url)'
        bacakodehtml = bukaurl.read()
        if bukaurl.getcode() == 200:
            if "input type=\"file\"" in bacakodehtml:
                print "\nDitemukan uploader pada:",alamat
        else:
            print "\033[91m \nTidak ada tempat upload!!!"
