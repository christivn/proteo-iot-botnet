import os, time
import os.path
os.system("clear")
acsii = """
                                                                 
""$$$$$$$$\                             $$\                               $$$$$$$\                                    
\__$$  __|                            $$ |                              $$  __$$\                                   
   $$ | $$$$$$\  $$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\        $$ |  $$ | $$$$$$\   $$$$$$\  $$$$$$\$$$$\  
   $$ |$$  __$$\ \____$$\ $$  _____|\_$$  _|  $$  __$$\ $$  __$$\       $$$$$$$\ |$$  __$$\  \____$$\ $$  _$$  _$$\ 
   $$ |$$ |  \__|$$$$$$$ |$$ /        $$ |    $$ /  $$ |$$ |  \__|      $$  __$$\ $$$$$$$$ | $$$$$$$ |$$ / $$ / $$ |
   $$ |$$ |     $$  __$$ |$$ |        $$ |$$\ $$ |  $$ |$$ |            $$ |  $$ |$$   ____|$$  __$$ |$$ | $$ | $$ |
   $$ |$$ |     \$$$$$$$ |\$$$$$$$\   \$$$$  |\$$$$$$  |$$ |            $$$$$$$  |\$$$$$$$\ \$$$$$$$ |$$ | $$ | $$ |
   \__|\__|      \_______| \_______|   \____/  \______/ \__|            \_______/  \_______| \_______|\__| \__| \__|
                                                                                                                    
                                                                                                                    
                                         """

print(acsii)
c = input("Would you like to use a [s]ingle asn or [m]ultiple ASNs ")
if c == "m":
    print("Input filename")
    fn = input(">>>>> ")
    fc = sum(1 for line in open(fn))
    os.system('clear')
    print(acsii)
    a = "You are scanning " + str(fc) + " ASNs."
    print(a)
elif c == "s":
    print("whats the ASN:")
    asn = input(">>>>> ")
    fn = "ig.txt"
    fi = open(fn, "w")
    fi.write(asn)
    fi.close()
    os.system('clear')
    print(acsii)
    print("You are scanning 1 ASNs.")
else:
    print("Invalid option '" + c +"'")
    time.sleep(1)
    os.system("python3 main.py")
os.system('ulimit -n 999999')
asns = open(fn, "r")
line = asns.readline()
while line: 
    filen = line + '.txt'
    os.system('wget https://api.hackertarget.com/aslookup/?q=' + line + ' -O ' + filen + " >/dev/null 2>&1")
    line = asns.readline()
    with open(filen, 'r+') as f: #open in read / write mode
        f.readline() #read the first line and throw it out
        data = f.read() #read the rest
        f.seek(0) #set the cursor to the top of the file
        f.write(data) #write the data back
        f.truncate() #set the file size to the current size
    f.close()
    os.system("cat " + filen + " >> list.lst")
    #put here
asns.close()
zmapc = open("list.lst", "r")
count = 0
num_lines = sum(1 for line in open(filen))
zmapc.close()
print(str(num_lines) + " ip ranges found")
