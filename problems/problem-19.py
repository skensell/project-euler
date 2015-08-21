#19. How many Sundays fell on the first of the month during the twentieth century?

#Jan 1 1901 (Tuesday) to Dec 31 2000
#Leap years occur on years divisible by 4, except not on centuries unless the century is divisible by 400 (i.e. we do get an extra day in December 2000).
import time

days_in_a_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def goodsundays():
    good_ones = 0
    day_of_the_week = 2
    year = 1901
    month = 0
    while year < 2001:
        if year % 4 ==0 and year != 2000:
            days_in_a_month[1] = 29
        else:
            days_in_a_month[1] = 28
        month=0
        while month < 12:
            if day_of_the_week == 0:
                good_ones += 1
            day_of_the_week = (day_of_the_week + days_in_a_month[month]) %7
            month += 1
        year +=1
    return  good_ones

#Takes .0005 seconds

t_0 = time.clock()
print goodsundays()
print time.clock()-t_0, 'seconds to complete'
