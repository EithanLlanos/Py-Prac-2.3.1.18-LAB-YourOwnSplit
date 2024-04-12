# Scenario
# You already know how split() works. Now we want you to prove it.

# Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

# it should accept exactly one argument - a string;
# it should return a list of words created from the string, divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# its name should be mysplit()
# Use the template in the editor. Test your code carefully.
####################################################################################################################################################

# Code
# def mysplit(strng):
#     #
#     # put your code here
#     #
# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

# Expected output
# ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
# ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
# []
# ['abc']
# []
####################################################################################################################################################


def mysplit(strng):
    list = []
    sw = False
    indx0 = -1
    for i in range(len(strng[:-1])):
        if strng[i] == " ":
            sw = True
        elif indx0 == -1:
            sw = False
            indx0 = i
        if (sw and indx0 !=-1):
            list.append(strng[indx0:i])
            sw = not sw
            indx0 = -1

    if len(strng) != 0:
        if(strng[-1]!=" "): 
            list.append(strng[indx0:])
        elif strng[indx0:-1]:
            list .append(strng[indx0:-1])

    return list

# def mysplit(strng):
#     listF=[]
#     word=""
#     for i,ch in enumerate(strng):
#         if ch!=" ":
#             word+=ch
#         elif word:
#             listF.append(word)
#             word=""
#     if word:
#         listF.append(word)
#     return listF 



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print(mysplit("     a"))
print(mysplit(" "))
