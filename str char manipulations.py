#ALERIA, MADEL S.
#Str char Manipulation (2)

def chow_string (str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(chow_string ('hello_philippines!'))

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('hello_philippines'))