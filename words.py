#coding: utf-8
import Tkinter
import MySQLdb
import sqlite3
import random
import re
#import pandas as pd

curIdx = 0
answer = []
isShowAnswer = 0
what = ["mean", "prononce", "word"]

def initWidget():
    global mainWin
    mainWin = Tkinter.Tk()
    mainWin.title("Come on, channy")
    mainWin.attributes('-alpha', 0)
    
    global isShowAnswer
    isShowAnswer = Tkinter.IntVar()
    isShowAnswer.set(0)
    global isTestWhat
    isTestWhat = Tkinter.StringVar()
    isTestWhat.set(what[0])
    global isGivenWhat
    isGivenWhat = Tkinter.StringVar()
    isGivenWhat.set(what[1])

    showAnsBtn = Tkinter.Checkbutton(mainWin, text="show answer", variable=isShowAnswer, command=showAnswer, onvalue=1, offvalue=0).pack()

    Tkinter.Label(mainWin, text="test what:").pack()
    Tkinter.OptionMenu(mainWin, isTestWhat, what[0], what[1], what[2]).pack()

    Tkinter.Label(mainWin, text="given what:").pack()
    Tkinter.OptionMenu(mainWin, isGivenWhat, what[2], what[1], what[0]).pack()
    Tkinter.Button(mainWin, text="Read File", command=readFile).pack()
    Tkinter.Label(mainWin, text="Select the meaning of Word:").pack()

    global wordLabel
    wordLabel = Tkinter.Label(mainWin, text="word")
    wordLabel.pack()
    global selectAns
    selectAns = Tkinter.IntVar()
    selectAns.set(0)

    for i in range(0, 4):
        answer.append(Tkinter.Radiobutton(mainWin, text="A", variable=selectAns, command=showAnswer, value=i+1))
        answer[i].pack()
    global totalWordLabel
    totalWordLabel = Tkinter.Label(mainWin, text="")
    totalWordLabel.pack()
    Tkinter.Button(mainWin, text="About", command=about).pack() 
    Tkinter.Button(mainWin, text="Delete this word", command=deleteWord).pack(fill="x")
    showWord()

def deleteDB():
    db = sqlite3.connect("words.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS WORDS") 
    db.close() 

def readFile():
    wordFile = open('words.txt')
    try:
        words = wordFile.read().decode('utf-8').splitlines()
    finally:
        wordFile.close()
 
    db = sqlite3.connect("test.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS WORDS")
    cursor.execute("CREATE TABLE WORDS(ORIGINWORD CHAR(20) NOT NULL, PRONONCE CHAR(20), MEANING CHAR(20), NONE CHAR(10), FRIQUENCY INT)")
  
    insertSql = ""
    for word in words: 
        words = word.split(' ')
        lenOfWords = len(words)
        if (lenOfWords < 3):
            continue
        wordSplit = re.split('[(,)]', words[0]) 
        if (len(wordSplit) == 1):
            insertSql = "INSERT INTO WORDS(ORIGINWORD, PRONONCE, MEANING, NONE, FRIQUENCY) values ('%s', '%s', '%s', '%s', 0)"%(words[0], words[0], words[2], words[1])
        else:
            insertSql = "INSERT INTO WORDS(ORIGINWORD, PRONONCE, MEANING, NONE, FRIQUENCY) values ('%s', '%s', '%s', '%s', 0)"%(wordSplit[1], wordSplit[0], words[2], words[1])
        cursor.execute(insertSql)
    db.commit()
    db.close() 

def readDb():
    db = sqlite3.connect("test.db")
    cursor = db.cursor()  
    cursor.execute("SELECT * FROM WORDS")
    words = cursor.fetchall()
    db.close() 
    return words

def deleteWord(): 
    db = sqlite3.connect("test.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM WORDS WHERE ORIGINWORD = %s"%(words[curIdx][0]))
    db.close()

def about():
    aboutWin = Tkinter.Tk()
    Tkinter.Label(aboutWin, text="Come on").pack()
    aboutWin.title("About") 

def showAnswer():
    answer[curIdx]['fg'] = 'green'
    totalWordLabel['fg'] = 'red'
    wordLabel.after(5000, showWord)

def showWord():
    global curIdx
    totalWordLabel['text'] = ""
    selectAns.set(0) 
    answer[curIdx]['fg'] = 'black'
    words = readDb()
    lenOfWords = len(words)
    idxs = random.sample(range(0, lenOfWords), 4)
    curIdx = random.randint(0, 3)
    totalWordLabel['text'] = words[idxs[0]]
    totalWordLabel['fg'] = totalWordLabel['bg']
    
    wordIdx = 0
    ansIdx = 0 #test mean
    if (isGivenWhat.get() == "mean"):
        wordIdx = 2
    elif (isGivenWhat.get() == "prononce"):
        wordIdx = 1
    if (isTestWhat.get() == "mean"):
        ansIdx = 2
    elif (isTestWhat.get() == "prononce"):
        ansIdx = 1

    wordLabel['text'] = words[idxs[0]][wordIdx]
    answer[curIdx]['text'] = words[idxs[0]][ansIdx]
    for i in range(0, 4):
        if (curIdx == i):
            continue
        answer[i]['text'] = words[idxs[i + 1 if(i < curIdx) else i]][ansIdx]
    if (isShowAnswer.get() == 1):
        showAnswer() 

if __name__ == "__main__":
    initWidget()
    mainWin.mainloop()     

