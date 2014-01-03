"""EE312 2013f Project1, Python 3 style.
This project shows how being a productive programming language makes Python so
fun to work in. For those of you in or having taken EE312, this script will
probably make you wish you could just go through the rest of EE in Python
(hey at least I would get an A+).
"""

import re


# The meat of Project1.cpp in just 4 lines
def spellCheck(article, dictionary):
    dictionary = set([word.lower() for word in re.split("\n+", dictionary) if word])
    for word in re.findall("\w\w+", article.lower()):
        if word not in dictionary:
            print(word)

# Chase's C++ code (main.cpp), ported to python
def readFile(file_name):
    filedata = ""
    with open(file_name, 'r') as file_in:
        filedata = file_in.read()
    return filedata

def fruityTest():
    print("\n\n******* Starting Base Test #1 (fruity) *******\n")
    dictionary = "apple\nbanana\norange\npear\n"
    article = "I ate an apple and a pear\n"
    spellCheck(article, dictionary) # should print: ate, an, and 
    print("****DONE****\n")

def dogTest():
    print("\n\n******* Starting Base Test #2 (dogs) *******\n")
    dictionary = "Beagle\nBulldog\nCollie\nPoodle\nretriever\n"
    article = "bulldog dalmation beagle Retriever poodles"
    spellCheck(article, dictionary) # should print: dalmation poodles
    print("****DONE****\n")

def punctuationTests():
    print("\n\n******* Starting Base Test #3 (punctuation) *******\n")
    dictionary = "but\ncan\ncan't\ndo\ndon't\nthink\n" # the dictionary can contain punctuation
    article = "I think I can, but I can't. I think I do, but I don't"
    spellCheck(article, dictionary) # should print: don
    print("****DONE****\n")

def generalTest1():
    print("\n\n******* Starting General Test #1 *******\n")
    article = readFile("greek-finances.txt")
    dictionary = readFile("american-english.txt")
    spellCheck(article, dictionary)
    print("****DONE****\n")

def generalTest2():
    print("\n\n******* Starting General Test #2 *******\n")
    article = readFile("bobsledding.txt")
    dictionary = readFile("american-english.txt")
    spellCheck(article, dictionary)
    print("****DONE****\n")

if __name__ == "__main__":
    fruityTest()
    dogTest()
    punctuationTests()
    #generalTest1()
    #generalTest2()
