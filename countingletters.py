'''
Created on Nov 18, 2017

@author: ITAUser
'''
#create a function that accepts the filename and character
#open the text file
#read the file
#split the file
#count the letters
#print result

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
countingletters(filename="constitution.txt", mychar = "a")
countingletters("constitution.txt", "a")
        #READ one character from the file
        #Make the char lowercase by using the function char.lower()
        #If the character exists, note that if the character does not exist,
        #char == is True
        #If the character is equal to variable mychar
        #Update count by increament by 1
        #Finish the loop, output the result
        






