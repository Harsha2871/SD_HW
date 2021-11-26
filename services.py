import enchant
from word2number import w2n
import ImportFromGit

def words(s):
    l=[]
    k=0
    i=1
    for i in range(len(s)):
        if s[i].isupper() and i!=0:
            l.append(s[k:i])
            k=i
    l.append(s[k:])
    return l

def check_builtIn(identifier):
    flag=False
    try:
        if __builtins__.__dict__[identifier]:
            flag=True
    except:
        pass
    return flag

def checkNum(word):
    flag1=False
    try:
        if w2n.word_to_num(word):
            flag1=True
    except:
        pass
    return flag1
