from lib2to3.pytree import convert

from matplotlib.colors import colorConverter


def compareStartandEnds(word): #create a code that compares the starts and end of the string
    word  = (str)(word)
    
    if (len(word) == 1):
        return True
    
    elif word[0] == word[len(word) - 1]:
        return(True)
    else:
        return False
test1 = "bababbb" # end in the same letter
test2 = "ab"# does not 
compareStartandEnds(test1)

print(compareStartandEnds(test1))
print(compareStartandEnds(test2))
print(compareStartandEnds(5))
print(compareStartandEnds('b'))
print(compareStartandEnds('a'))