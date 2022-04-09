from constraint import *
import numpy as np

def readfile(file):
    lines=[]
    dic_file=dict()
    with open(file) as f:
        for line in f:
            #print(line.rstrip())
            word=list(line.rstrip())#.split('')
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



def dict_to_liste_solution(solution , n):
    l=[]
    for i in range(n):
        l.append(solution["x"+str(i)])
    return l

dictionnary=readfile('./dico.txt')
#print(dictionnary[4])

assert((check_correct("tarte","dette"))==(2,1))
assert((check_correct("bonjour","nobjour")==(5,2)))


def wordle_mind(word, dictionnary):

    n=len(word)
    pb=Problem()
    list_mot=np.array(dictionnary[n])
    list_domain=[set(list_mot[:,i]) for i in range(n)]
    # Creation d'une liste python cols de dimension n

    while solution!=word:
    #
        for i in range(n):
            name_variable="x"+str(i)
            pb.addVariables(name_variable,list_domain[i])

        index=0
        solution=dict_to_liste_solution(solutions[index], n)
        while solution not in dictionnary:
            index+=1
            solution=dict_to_liste_solution(solutions[index], n)

        bien_place, mal_place = check_correct(solution, word)

        count_bien, count_mal=bien_place, mal_place
        list_index=[]
        list_mal=[]
        while count_bien>0:
            list_index.append(find_bien_place(solution, n, bien_place, list_index, word)))
            count_bien-=1


    return pass


def find_bien_place(solution, n, bien_place, list_index, word):
    for i in range(n):
        if i not in list_index:
            avant=solution[i]
            solution[i]="_"
            bien_place_new,_ =check_correct(solution, word)
            if bien_place_new<bien_place:
                solution[i]=avant
                return i
    print("Erreur : func_find_bien_place")




n=2
pb=Problem()
list_mot=np.array(dictionnary[n])
#print(list_mot[0][1])
list_domain=[list(set(list_mot[:,i])) for i in range(n)]
print(list_domain)
for i in range(n):
    print(len(list_domain[i]))
print(dictionnary[2])
