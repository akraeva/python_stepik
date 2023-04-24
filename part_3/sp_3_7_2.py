str1 = input()
str2 = input()


def create_dic(key, value):
    result = {}
    for i in range(len(key)):
        result[key[i]] = value[i]
    return result


def spell(string, dic):
    result = ''
    for char in string:
        result = result + dic[char]
    return result


dic_code = create_dic(str1, str2)
dic_decode = create_dic(str2, str1)

str1 = input()
str2 = input()

print(spell(str1, dic_code))
print(spell(str2, dic_decode))
