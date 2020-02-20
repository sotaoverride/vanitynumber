import pandas as pd
from collections import defaultdict
import itertools

# hashTable[i] stores all characters
# that correspond to digit i in phone
hashTable = ["", "", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]


formedWords = []
#function to make phone number look pretty 

def makePretty(string):
    string=string.replace('--', '-')
    string=string.rstrip('-')
    return string

# function string to phone number


def stringToPhoneNumber(string):
    number = ""
    for c in string:
        for i in range(0, len(hashTable)):
            for j in range(0, len(hashTable[i])):
                if hashTable[i][j] in c.lower():
                    number += (str(i))
    return number

# function get all combinations


def getAllCombinations(stuff):
    combo_list = []
    for L in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            if L in range(2, len(stuff)):
                combo_list.append(subset)
    return combo_list
# function to get unique strings to a string (no chars overlap)


def getUniqueStringsTo(string, list1):

    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        str1 = ''.join(str(e) for e in list1[x])
        if(string not in str1):
            unique_list.append(str1)
    return unique_list

# Python program to print all
# sublist from a given list

# function to generate all the sub lists


def sub_lists(list1):

    # store all the sublists
    sublist = [[]]

    # first loop
    for i in range(len(list1) + 1):

        # second loop
        for j in range(i + 1, len(list1) + 1):

            # slice the subarray
            sub = list1[i:j]
            if len(sub) in range(3,len(list1)):
                sublist.append(sub)

    return sublist


def parse_dictionary(file_name):
    words_df = pd.read_csv(file_name, encoding='utf-8')
    
    words = words_df.WORDS.astype(str).tolist()
    return words

# A recursive function to print all
# possible words that can be obtained
# by input number[] of size n. The
# output words are one by one stored
# in output[]


def printWordsUtil(number, curr, output, n, words, orgNumber):
    if(curr == n):
        str1 = ''.join(str(e) for e in output)
        str5 = '-'+str1+'-'
        str2 = ''.join(str(e) for e in orgNumber)
        str3 = ''.join(str(e) for e in number)
        if str1 in words:
            print(makePretty(str2.replace(str3, str5)))
            formedWords.append(str2.replace(str3, str5))
            for i in range(0, len(formedWords)):
                if(str3 in formedWords[i]):
                    formedWords.append(formedWords[i].replace(str3, str5))
                    print(makePretty(formedWords[i].replace(str3, str5)))


        return

    # Try all 3 possible characters
    # for current digir in number[]
    # and recur for remaining digits
    for i in range(len(hashTable[number[curr]])):
        output.append(hashTable[number[curr]][i])
        printWordsUtil(number, curr + 1, output, n, words, orgNumber)
        output.pop()
        if(number[curr] == 0 or number[curr] == 1):
            return

# A wrapper over printWordsUtil().
# It creates an output array and
# calls printWordsUtil()


def printWords(number, n, words, orgNumber):
    printWordsUtil(number, 0, [], n, words, orgNumber)


# Driver function
if __name__ == '__main__':
    number=[1, 8, 0, 0, 7, 2, 4, 6, 8, 3, 7]
    ll=sub_lists(number)
    for i in range(len(ll)):
            n=len(ll[i])
            file_name=r'words.csv'
            words=parse_dictionary(file_name)
            map(str.lower,words)
            words = filter (lambda word: len (word) > 2, words)
            printWords(ll[i], n, words, number)
# This code is contributed by prajmsidc
