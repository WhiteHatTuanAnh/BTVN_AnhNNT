string_input = "ThiS is String with Upper and lower case Letters"

def order_dic(dic):
    ordered_dic={}
    key_ls=sorted(dic.keys())
    for key in key_ls:
        ordered_dic[key]=dic[key]
    return ordered_dic

string_lower = string_input.lower()

count = {}
for character in string_lower :
    if character != " " :
        count[character] = count.get( character, 0) + 1

order_dic(count)

for key, value in order_dic(count).items():
    print("{0} {1}".format(key, value))
