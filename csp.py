from constraint import *
import numpy as np


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def readfile(file):
    lines=[]
    dic_file=dict()
    with open(file) as f:
        for line in f:
            word=line.rstrip()
            lg_word=len(word)
            if lg_word in dic_file:
                dic_file[lg_word].append(word)
            else:
                dic_file[lg_word]=[word]
    return dic_file


def check_correct(instance, word):
    bien_place=0
    mal_place=0
    list_not_match1=[]
    list_not_match2=[]
    for i in range(len(instance)):
        if instance[i]==word[i]:
            bien_place+=1
        else:
            list_not_match1.append(instance[i])
            list_not_match2.append(word[i])
    for letter in list_not_match1:
        if letter in list_not_match2:
            list_not_match2.remove(letter)
            mal_place+=1
    return bien_place, mal_place

dictionnary=readfile('./dico.txt')
#print(dictionnary[4])

assert((check_correct("tarte","dette"))==(2,1))
assert((check_correct("bonjour","nobjour")==(5,2)))


"""def wordle_mind(word, dictionnary):

    n=len(word)
    pb=Problem()
    list_mot=np.array(dictionnary[n])
    list_domain=[set(list_mot[:,i]) for i in range(n)]
    # Creation d'une liste python cols de dimension n
    cols=range(n)

    #
    pb.addVariables(cols, alphabet)"""


n=4
pb=Problem()
list_mot=np.array(dictionnary[n])
print(list_mot[0][1])
list_domain=[set(list_mot[:,i]) for i in range(n)]
