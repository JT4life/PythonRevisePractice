#int with min 4 width
print("'{:4d}'".format(23)) #'  23'

#pad with 0
print("'{:04d}'".format(23)) #0023

#2 decimal point float value
print('{:.2f}'.format(45.6))
print('%.2f' % (45.6))

#Thousand separator.
print('{:,.2f}'.format (12345.6)) # 12,345.60

#left align
print("'{:4}'".format('ab'))
print("'{:<4}'".format('ab'))
print("%-4s" % ('ab'))

# right aligned
print("'{:>4}'".format('ab'))    # '  ab'
print("%4s" % ('ab'))    # '  ab'

# centeraligned, pad with '_'
print("'{:_^4}'".format('ab'))  # '_ab_'

