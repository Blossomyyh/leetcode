"""
english word array

corner case
    k<length

"""

def eng1(s):
    string = " ".join(s[:-1])
    string += " and " + s[-1]
    print(string)
eng1(['A','B','C','D'])

def eng2(s, k):
    string = " ".join(s[:-k])
    string += " and "+ str(k)+ " more"
    print(string)
eng2(['A','B','C','D'], 3)



def english_words_array1(s_list):
    if not s_list:
        return
    if len(s_list) == 1:
        return s_list[0]
    return ' '.join(s_list[:-1]) + ' and ' + s_list[-1]

print(english_words_array1(['A','B','C','D']))

def english_words_array2(s_list, num):
    if not s_list:
        return
    if len(s_list) <= num:
        return ' '.join(s_list[:-1]) + ' and ' + s_list[-1]
    else:
        return ' '.join(s_list[:num]) + ' and {} more'.format(len(s_list) - num)

print(english_words_array2(['A','B','C', 'D'], 2))