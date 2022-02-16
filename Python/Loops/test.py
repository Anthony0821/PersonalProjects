





def string_times(str, num):
    return(str * num)


def front_times(str, num):
    string = str
    if len(string) <=2 :
        return string * num
    else:
        front3 = string[0:3]
        return front3 * num

   
def array_count9(num):
    index = 0
    for i in num:
        while (i <= 4):
             if num[i] == 9:
                return True
        index += 1
        
        return False

def array123(nums):
    index  = 0
    count = 0
    while (index < len(nums)-2):
        temp = nums[index]
        if temp == 1:
            temp == nums[index + 1]
            if temp == 2:
                temp == nums[index +2]
                if temp == 3:
                    return True
            index += 1
        else:
            index += 1
    return False        

def string_match(word1, word2):
    shorter = min(len(word1), len(word2))
    count = 0
    
    for i in range(shorter - 1):
        
        Fl = word1[i : i+2]
        Sl = word2[i: i + 2]
        if Fl == Sl:
            count = count +1
        
    return count

def vowel_count(word):
    result = 0
    consinents ="BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
    for i in word:
        if i in consinents:
            result += 1
    
    return result

print(vowel_count("hello"))
        
