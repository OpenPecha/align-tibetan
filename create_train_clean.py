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
    numbers = []
    for number in string.split(','):
        numbers.append(int(number))
    return numbers
    

for line in ladder_file:
    if len(line.split(':')) == 3:
        skt,tib,score = line.split(':')
        if re.search("[0-9]",skt) and re.search("[0-9]",tib):
            skt_nums = clean_num(skt)
            tib_nums = clean_num(tib)
            for num in skt_nums:
                output += sktfile[num] + " "
            output += "\t"
            for num in tib_nums:
                output += tibfile[num] + " "
            output += "\n"
print(output)
# with open(short_f1 + "_" + short_f2 + ".train", 'w') as file:
#     file.write(output)
