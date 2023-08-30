""" Palindrome Check """
string=input('Enter the string: ')
string=string.lower()
compare_string=''

# compare_string=string[::-1]
# print(compare_string)

for i in string[::-1]:
    compare_string = compare_string + i

# print(compare_string)

if string==compare_string:
    print(f'String {string} is palindrome')
else:
    print(f'String {string} is not palindrome')