import sys
import re
import re
f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'r')
ladder_file = open(sys.argv[3],'r')


output = ""
ladder = []
sktfile = [line.rstrip('\n').strip() for line in f1]
tibfile = [line.rstrip('\n').strip() for line in f2]
last_score = 0.5

def clean_num(string):
    string = re.sub("[^0-9, ]","",string)
    return int(string.split(',')[0])
    

for line in ladder_file:
    if len(line.split("\t")) == 3:
        skt,tib,score = line.split('\t')
        if re.search("[0-9]",skt) and re.search("[0-9]",tib):
            skt_num = clean_num(skt)
            tib_num = clean_num(tib)
            ladder.append([skt_num,tib_num,score])
        
        
    if ";" in line:
        m = re.search("([0-9., ]+);([0-9., ]+).*=\"([0-9.,]+)", line)
        if m:
            skt_num = int(m.group(1).split()[0].replace(".","").replace(",",""))-1
            tib_num = int(m.group(2).split()[0].replace(".","").replace(",",""))-1
            score = float(m.group(3))
            ladder.append([skt_num,tib_num,score])


    
    if len(line.split(':')) == 3:
        skt,tib,score = line.split(':')
        if re.search("[0-9]",skt) and re.search("[0-9]",tib):
            skt_num = clean_num(skt)
            tib_num = clean_num(tib)
            ladder.append([skt_num,tib_num,score])
last_skt = 0
last_tib = 0
for entry in ladder:
        output = output + ' '.join(sktfile[last_skt:entry[0]]) + "\t"
        output = output + ' '.join(tibfile[last_tib:entry[1]]) + "\n" 
        last_skt = entry[0]
        last_tib = entry[1]
output = output + ' '.join(sktfile[last_skt:-1]) + "\t"
output = output +  ' '.join(tibfile[last_tib:-1]) + "\n" # + str(entry[2]) 

short_f1 = re.sub("\.tsv.*","",sys.argv[1])
short_f2 = re.sub(".*/","",sys.argv[2])
short_f2 = re.sub("\.tsv.*","",short_f2)
print(output)
# with open(short_f1 + "_" + short_f2 + ".train", 'w') as file:
#     file.write(output)
