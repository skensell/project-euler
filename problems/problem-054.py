from Poker import poker
from myToolbox import timed

#outputs:
#pe54() finished in 0.163635 seconds.
#376

@timed
def pe54():
    data = open('text/poker.txt')
    #hands = [[card for card in line.split()] for line in data]
    def one_wins(line):
        hand = line.strip().split()
        p1,p2 = hand[0:5],hand[5:]
        return 1 if poker([p1,p2]) == [p1] else 0
    return sum(map(one_wins,data))

print pe54()
