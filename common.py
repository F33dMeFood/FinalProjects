'''
Created on Dec 2, 2017

@author: ITAUser
'''
def countingletters(filename, mychar):
    f = open(filename, 'r')
    count = 0;
    run = True
    while run:
        letter = f.read(1)
        letter = letter.lower()
        if letter == "":
            break
        else:
            if letter == mychar:
                count = count + 1
    print(count)
    

countingletters(filename="constitution.txt", mychar="a")
countingletters(filename="constitution.txt", mychar="b")
letters = list['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for letter in letters:
    currentcount = countingletters("constitution.txt", letter)
    countlist.append(currentcount)
print(countlist)
dracula = max(countlist)
print(dracula)
indexletter = countlist.[indexlist]



