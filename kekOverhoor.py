#!/usr/bin/python2
import random, parseWoordenLijst, argparse

def ask(dict, key):
    #TODO: implement ask()
    answer = raw_input(key+':')
    if answer == dict[key]:
        print 'goed\n'
    else:
        print 'FOUT!'
        print 'Het goede antwoord is: ' + dict[key] + '\n'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='filename parser')
    parser.add_argument('filename', help="Word list file")
    args = parser.parse_args()

    worddict = parseWoordenLijst.parse(args.filename) 
   
    for i in range(len(worddict)):
        askedWord = random.choice(worddict.keys())
        ask(worddict, askedWord)
        worddict.pop(askedWord, None)
