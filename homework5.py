import re
'''дз5'''
# a = '7(616)230-24-32\n7(713)808-98-79\n' \
#     '992(891)584-10-04\n992(34)787-35-87\n' \
#     '9(673)605-18-53\n996(010)206-44-19\n' \
#     '96(96)553-02-13\n996(7339)828-94-80\n' \
#     '96(971)806-77-23\n996(63)863-50-64\n'
# b = re.sub('996' , '7', a)
# print(b)

'''экстра дз'''

a = '7(616)230-24-32\n7(713)808-98-79\n' \
     '992(891)584-10-04\n992(34)787-35-87\n' \
     '9(673)605-18-53\n996(010)206-44-19\n' \
     '96(96)553-02-13\n996(7339)828-94-80\n' \
     '96(971)806-77-23\n996(63)863-50-64\n'

b =re.findall(r'996.[01-9]+.\d{3}.\d{2}.\d{2}',a)
print(b)