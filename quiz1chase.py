import json

def readcurrency():
    new_list = []
   # print "currency.txt", filename
    with open("currency.txt", "r") as input_file:
        data = input_file.read().strip().split()
        dict_list = dict(zip(data[::2], data[1::2]))

    for x in dict_list.keys():
        append = x + " " + dict_list[x]
        new_list.append(append)
    
    for i in new_list:
        print(i, " ")




    
    

        


print(readcurrency())