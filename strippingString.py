word = " Hello who are you "
print(word.strip())
#lstrip() left side
#rstrip right
#strip('c') both left and right
#rstrip(' c') from both the right side and strip space

print(word.rstrip(' c'))

#exercise
s1 = "   ** MMU FCI **   "
# print ("0.'{}'".format(s1))
# print ("1.'{}'".format(s1.lstrip()))
# print ("2.'{}'".format(s1.rstrip()))
# print ("3.'{}'".format(s1.strip()))
print ("4.'{}'".format(s1.strip('*')))
print ("5.'{}'".format(s1.strip(' *')))
print ("6.'{}'".format(s1.strip('* ')))
print ("7.'{}'".format(s1.strip('* M')))