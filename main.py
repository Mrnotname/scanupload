import urllib
import scan


print"\033[92m||=======================================||"
print"\033[93m||==========Tools scan upload============|| "
print"\033[93m||===========path upload shell===========||"
print"\033[91m||==========creat by MR.ID===============||"
print"\033[92m||=========TEAM PASUKAN TERMUX===========||"
print"\033[93m||============friend's team==============||"
print"\033[91m||=========B4CKD00R CR45H TEAM===========||"
print"\033[92m||=======================================||"

target = raw_input("\033[95m Masukkan url target: ")
if not target.startswith("http://"):
    target = "http://"+target
   
wordlist = raw_input("\033[95m Masukkan wordlistnya: ")

import scan
scan.scanuploader(target,wordlist)
