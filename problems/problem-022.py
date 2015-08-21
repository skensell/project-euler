#22. Find the sum of the name values from names.txt
#takes .0227 seconds
import re
import time

t_0 = time.clock()
names_file = open("text/names.txt", "r+")
names_str = names_file.read();
names = re.findall(r'[A-Z]+[a-z]*',names_str.strip()) #.strip removes trailing whitespace from beginning and end
names_file.close()

names.sort()

#ord("A")=65 and ord("Z")=90

total=0
for i in range(len(names)):
    alph_val = 0
    for char in names[i]:
        alph_val += (ord(char)%64)
    total += alph_val*(i+1)


print total
print time.clock() - t_0, "seconds to complete"
