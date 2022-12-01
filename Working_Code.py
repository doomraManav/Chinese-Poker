# 13 cards
# red , black , red , black
# diamonds, clubs, hearts, spades
# value of line 1 < line 2 < line 3

#get random input at https://www.random.org/playing-cards/

# diamonds : "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d", "Jd", "Qd", "Kd", "Ad"
# clubs : "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Qc", "Kc", "Ac"
# hearts : "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "Jh", "Qh", "Kh", "Ah"
# spades : "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s", "Js", "Qs", "Ks", "As"

import sys
import time
# function for getting the value of each card
def checkCard(card):
    diamonds = ["2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "10d", "Jd", "Qd", "Kd", "Ad"]
    clubs = ["2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Qc", "Kc", "Ac"]
    hearts = ["2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "Jh", "Qh", "Kh", "Ah"]
    spades = ["2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s", "Js", "Qs", "Ks", "As"]
    point = [None] * 13
    for i in range(len(card)):
        if (card[i] == diamonds[0]):
            point[i] = 2
        elif (card[i] == diamonds[1]):
            point[i] = 3
        elif (card[i] == diamonds[2]):
            point[i] = 4
        elif (card[i] == diamonds[3]):
            point[i] = 5
        elif (card[i] == diamonds[4]):
            point[i] = 6
        elif (card[i] == diamonds[5]):
            point[i] = 7
        elif (card[i] == diamonds[6]):
            point[i] = 8
        elif (card[i] == diamonds[7]):
            point[i] = 9
        elif (card[i] == diamonds[8]):
            point[i] = 10
        elif (card[i] == diamonds[9]):
            point[i] = 11
        elif (card[i] == diamonds[10]):
            point[i] = 12
        elif (card[i] == diamonds[11]):
            point[i] = 13
        elif (card[i] == diamonds[12]):
            point[i] = 14
        elif (card[i] == clubs[0]):
            point[i] = 2
        elif (card[i] == clubs[1]):
            point[i] = 3
        elif (card[i] == clubs[2]):
            point[i] = 4
        elif (card[i] == clubs[3]):
            point[i] = 5
        elif (card[i] == clubs[4]):
            point[i] = 6
        elif (card[i] == clubs[5]):
            point[i] = 7
        elif (card[i] == clubs[6]):
            point[i] = 8
        elif (card[i] == clubs[7]):
            point[i] = 9
        elif (card[i] == clubs[8]):
            point[i] = 10
        elif (card[i] == clubs[9]):
            point[i] = 11
        elif (card[i] == clubs[10]):
            point[i] = 12
        elif (card[i] == clubs[11]):
            point[i] = 13
        elif (card[i] == clubs[12]):
            point[i] = 14
        elif (card[i] == hearts[0]):
            point[i] = 2
        elif (card[i] == hearts[1]):
            point[i] = 3
        elif (card[i] == hearts[2]):
            point[i] = 4
        elif (card[i] == hearts[3]):
            point[i] = 5
        elif (card[i] == hearts[4]):
            point[i] = 6
        elif (card[i] == hearts[5]):
            point[i] = 7
        elif (card[i] == hearts[6]):
            point[i] = 8
        elif (card[i] == hearts[7]):
            point[i] = 9
        elif (card[i] == hearts[8]):
            point[i] = 10
        elif (card[i] == hearts[9]):
            point[i] = 11
        elif (card[i] == hearts[10]):
            point[i] = 12
        elif (card[i] == hearts[11]):
            point[i] = 13
        elif (card[i] == hearts[12]):
            point[i] = 14
        elif (card[i] == spades[0]):
            point[i] = 2
        elif (card[i] == spades[1]):
            point[i] = 3
        elif (card[i] == spades[2]):
            point[i] = 4
        elif (card[i] == spades[3]):
            point[i] = 5
        elif (card[i] == spades[4]):
            point[i] = 6
        elif (card[i] == spades[5]):
            point[i] = 7
        elif (card[i] == spades[6]):
            point[i] = 8
        elif (card[i] == spades[7]):
            point[i] = 9
        elif (card[i] == spades[8]):
            point[i] = 10
        elif (card[i] == spades[9]):
            point[i] = 11
        elif (card[i] == spades[10]):
            point[i] = 12
        elif (card[i] == spades[11]):
            point[i] = 13
        elif (card[i] == spades[12]):
            point[i] = 14
        else:
            print("error : invalid card")
            sys.exit()
    return point

# check Pair in card
def checkpair(point):
    pair = [None]
    i = len(point) - 1
    while i > 0:
        j = 0
        a = [None] * 2
        if point[i] == point[i-1]:
            a[j] = i
            a[j+1] = i-1
            pair = pair + a
            i = i - 2
            j = j + 2
        else:
            i = i - 1
    pair.pop(0)
    return pair

#check Three Of A Kind (not used)
def checkThreeOfaKind(point):
    j = 0
    pair = [None] * 12
    i = len(point) - 1
    while i > 0:
        if point[i] == point[i-1] and point[i-1] == point[i-2]:
            pair[j] = i
            pair[j+1] = i-1
            pair[j+2] = i-2
            i = i - 3
            j = j + 3
        else:
            i = i - 1

    return pair

#Check Straight
def checkstraight(point):
    j = 0
    straight = [None]
    i = len(point) - 1
    while i >= 0:
        prec = i - 5
        if (prec >= 0):
            tanda = True
            counter = [None] * 5
            p = 0
            while i >= prec and tanda:
                if (point[i]-1 == point[i - 1]):
                    counter[p] = i
                    p = p + 1
                    i = i - 1
                elif (point[i] == point[i - 1]):
                    i = i - 1
                    prec = prec - 1
                    if (prec <= 0):
                        counter[p] = i
                else:
                    i = i - 1
                    tanda = False
            if (counter[4] != None):
                straight = straight + counter
        else :
            i = i - 1
    straight.pop(0)
    return straight

# input card
def getCard():
    input_string = input("Enter all the cards you get separated by comma ")
    card = input_string.split(",")
    while (len(card) != 13):
        print("invalid number of card please input again")
        print("")
        input_string = input("Enter all the cards you get separated by comma ")
        card = input_string.split(",")
    return card
 
# find the position the card in top three
def findBiggest3(point):
    position = [0,0,0]
    prevpos1 = 0
    prevpos2 = 0
    prevbiggest1 = point[0]
    prevbiggest2 = point[0]
    biggest1 = point[0]
    biggest2 = point[0]
    biggest3 = point[0]
    
    for i in range(len(point)):
        if (biggest1 < point[i]):
            biggest1 = point[i]
            position[0] = i
            if (biggest2 < biggest1):
                prevbiggest1 = biggest2
                prevpos1 = position[1]
                biggest2 = biggest1
                position[1] = position[0]
                biggest1 = prevbiggest1
                position[0] = prevpos1
                if (biggest3 < biggest2):
                    if (biggest3 < biggest1):
                        prevbiggest1 = biggest3
                        prevpos1 = biggest3

                        biggest3 = biggest1
                        position[2] = position[0]
                        
                        biggest1 = prevbiggest1
                        position[0] = prevpos1
                        
                    prevbiggest2 = biggest3
                    prevpos2 = position[2]
                    
                    prevbiggest1 = biggest2
                    prevpos1 = position[1]
                    
                    biggest3 = biggest2
                    position[2] = position[1]
                    
                    biggest2 = prevbiggest2
                    position[1] = prevpos2
    return position

# find the position the card in top two
def findBiggest2(point):
    position = [0,0]
    prevpos1 = 0
    prevbiggest1 = point[0]
    biggest1 = point[0]
    biggest2 = point[0]
    
    for i in range(len(point)):
        
        if (biggest1 < point[i]):
        
            biggest1 = point[i]
            position[0] = i
        
            if (biggest2 < biggest1):
        
                prevbiggest1 = biggest2
                prevpos1 = position[1]
        
                biggest2 = biggest1
                position[1] = position[0]
        
                biggest1 = prevbiggest1
                position[0] = prevpos1
    return position

# find the position the card in top one
def findBiggest1(point):
    position = [0]
    prevbiggest1 = point[0]
    biggest1 = point[0]
    
    for i in range(len(point)):
        
        if (biggest1 < point[i]):
        
            biggest1 = point[i]
        
            position[0] = i
    return position
 
# Process of output Card
def Calculation(point, card):
    start = time.time()
    
    line1, line2, line3 = False, False, False
    Straight = checkstraight(point)
    check = 0
    
    while (Straight != []):
        i = 0
        counter = 0
        while counter < 5:
            print(card[Straight[i]], end=' ')
            card.pop(Straight[i])
            point.pop(Straight[i])
            Straight.pop(i)
            counter = counter + 1

        check = check + 1
        print("")

    if (check == 1):
        line3 = True
    elif (check == 2):
        line3 = True
        line2 = True

    if (line3 == False):
        Pair = checkpair(point)
        if (Pair != []):
            counter = 0
            while (Pair != []):
                i = 0
                j = 0
                while (j < 4 and Pair != []):
                    print(card[Pair[i]], end=' ')
                    card.pop(Pair[i])
                    point.pop(Pair[i])
                    Pair.pop(i)
                    j = j + 1
                    counter = counter + 1
                print("")
 
                if (counter <= 4 and counter > 0):
                    line3 = True
                elif (counter <= 8 and counter > 0):
                    line3 = True
                    line2 = True
                elif (counter <= 10):
                    line1 = True
                    line2 = True
                    line3 = True
 
            if (line3 == False):
                    position = findBiggest3(point)
                    print(card[position[0]])
                    print(card[position[1]])
                    print(card[position[2]])
                    card.pop(position[0])
                    card.pop(position[1]-1)
                    card.pop(position[2]-2)
            elif (line2 == False):
                    position = findBiggest2(point)
                    print(card[position[0]])
                    print(card[position[1]])
                    card.pop(position[0])
                    card.pop(position[1]-1)
            elif (line1 == False):
                position = findBiggest1(point)
                print(card[position[0]])
                card.pop(position[0])
        elif (line2 == False):
            Pair = checkpair(point)
            if (Pair != []):
                counter = 0
                while (Pair != []):
                    i = 0
                    j = 0
                    while (j < 4 and Pair != []):
                        print(card[Pair[i]], end=' ')
                        card.pop(Pair[i])
                        point.pop(Pair[i])
                        Pair.pop(i)                            
                        j = j + 1
                        counter = counter + 1
                    
                    print("")
                if (counter <= 4 and counter > 0):
                    line2 = True
                elif (counter <= 8 and counter > 0):
                    line2 = True
                    line1 = True                       
        
            if (line2 == False):
                    position = findBiggest2(point)
                    print(card[position[0]])
                    print(card[position[1]])
                    card.pop(position[0])
                    card.pop(position[1]-1)                            
            elif (line1 == False):
                    position = findBiggest1(point)
                    print(card[position[0]])
                    card.pop(position[0])
        else:
            Pair = checkpair(point)
            if (Pair != []):
                counter = 0
                while (Pair != []):
                    i = 0
                    j = 0
                    while (j < 4 and Pair != []):
                        print(card[Pair[i]], end=' ')
                        card.pop(Pair[i])
                        point.pop(Pair[i])
                        Pair.pop(i)
                        j = j + 1
                        counter = counter + 1
                    print("")
                    
                if (counter <= 4 and counter > 0):
                    line1 = True
            if (line1 == False):
                position = findBiggest1(point)
                print(card[position[0]])
                card.pop(position[0])
    
        end = time.time()
        print("Unvaluable card (you can put it what ever line you want) :")
        while (card != []):
            print(card[0], end=' ')
            card.pop(0)
            
    print("")
    print("Executed time : ", end - start)
 
# print the highest card that possible on line 1, 2, 3 (not used)
def printPosition(card, position):
    print("line 1 : ", card[position[0]])
    print("line 2 : ", card[position[1]])
    print("line 3 : ", card[position[2]])

def main():
    global card 
    global point
    card = getCard()
    point = checkCard(card)
    print(point)
    print(card)
    print("Your Card Combination is : ")
    Calculation(point, card)
main()

