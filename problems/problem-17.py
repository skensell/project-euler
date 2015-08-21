#17. If all the numbers from 1 to 1000 were written out in words, how many letters would be needed?

#First how many letters are in 1-99?

num_letters = {1: 3,
               2:3,
               3:5,
               4:4,
               5:4,
               6:3,
               7:5,
               8:5,
               9:4,
               10:3,
               11:6,
               12:6,
               13:8,
               14:8,
               15:7,
               16:7,
               17:9,
               18:8,
               19:8,
               20:6,
               30:6,
               40:5,
               50:5,
               60:5,
               70:7,
               80:6,
               90:6}

sum=0
for i in range(1,1001):
    if i < 100:
        if i in num_letters:
            sum += num_letters[i]
        else:
            sum += num_letters[int(str(i)[0] + '0')] + num_letters[i%10]
    elif i==1000:
        sum += 11
    else:  #i has 3 digits
        sum += num_letters[int(str(i)[0])] + 7
        if i%100 != 0:
            sum += 3
            i=i%100
            if i in num_letters:
                sum += num_letters[i]
            else:
                sum += num_letters[int(str(i)[0] + '0')] + num_letters[i%10]


print sum
