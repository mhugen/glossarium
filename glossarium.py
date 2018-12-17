# Glossarium

import os, time
from os import listdir
from os.path import isfile, join
import random

def main():
	print("""\n\n----- Glossarium -----
1. Take a test
2. Add to a test
3. Create a test
4. Delete a test
5. Quit
----------------------------""")
	val = int(input("What would you like to do? "))
	return val

def writeTofile(test, add):
    with open(test, 'a') as file:
        file.write(add)

def take():
    mypath = os.path.dirname(os.path.realpath(__file__))
    filesInDir = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    filesInDir.remove('glossarium.py')
    filesInDir.remove('README.md')

    if len(filesInDir) > 0:
        print('\nAvailable Tests\n')
        for test in filesInDir:
            print(test[:-4])

        takeTest = str(input("\nWhich test would you like to take? "))+'.txt'

        with open(takeTest, 'r') as file:
            testData = file.read().splitlines()

        questions = []
        answers = []
        for line in testData:
            lineSplit = line.split(';')
            questions.append(lineSplit[0])
            answers.append(lineSplit[1])

        taken = []
        print("Test starting. Exit 'exit', Answer 'answer'.")
        while True:
            askIdx = random.randint(0,len(questions)-1)

            if len(taken)==len(questions):
                print('\nNo more questions in test. Goodbye.')
                break

            elif askIdx not in taken:
                taken.append(askIdx)
                print('\nQuestion: '+questions[askIdx])
                ans = str(input('Answer: '))

                if ans == 'exit':
                    break
                
                elif ans =='answer':
                    print('The answer is: ')
                    print('\n'+answers[askIdx])

                elif ans == answers[askIdx]:
                    print('Correct answer.')
                    
                else:
                    ans2 = str(input('Wrong answer, try again: '))

                    if ans2 == answers[askIdx]:
                        print('Correct answer.')
                    else:
                        print('Wrong answer again. You need to study more.')
                        print('The correct answer is: ')
                        print('\n'+answers[askIdx])

            else:
                continue
    else:
        print("\nThere seem to be no tests available.")

def add():
    mypath = os.path.dirname(os.path.realpath(__file__))
    filesInDir = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    filesInDir.remove('glossarium.py')
    filesInDir.remove('README.md')

    if len(filesInDir) > 0:
        print('\nAvailable Tests\n')
        for test in filesInDir:
            print(test[:-4])

        addTotest = str(input("\nWhich test would you like to add to? "))+'.txt'
        print("\nNow add questions and answers. Exit by 'exit'.")

        while True:
            print('\n')

            q = str(input("Question: "))
            if q == 'exit':
                break

            a = str(input("Answer: "))
            if a=='exit':
                break

            entry = q+';'+a+'\n'
            writeTofile(addTotest,entry)
    else:
        print("\nThere seem to be no tests available.")

def create():
    name = str(input("\nName your test: "))+'.txt'
    writeTofile(name,'')
    print("\nNow add questions and answers. Exit by 'exit' as question.")

    while True:
        print('\n')

        q = str(input("Question: "))
        if q == 'exit':
            break

        a = str(input("Answer: "))
        if a=='exit':
            break

        entry = q+';'+a+'\n'
        writeTofile(name,entry)        

def delete():
    mypath = os.path.dirname(os.path.realpath(__file__))
    filesInDir = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    filesInDir.remove('glossarium.py')
    filesInDir.remove('README.md')

    if len(filesInDir) > 0:
        print('\nAvailable Tests\n')
        for test in filesInDir:
            print(test[:-4])

        delTest = str(input("\nWhich test do you want to delete: "))+'.txt'
        os.remove(delTest)

    else:
        print("\nThere seem to be no tests available.")

while True:

    val= main()

    if val == 1:
        take()

    if val == 2:
        add()

    if val == 3:
        create()

    if val == 4:
        delete()

    if val == 5:
        break