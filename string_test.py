#Traversing a string

str=" hello world"
for i in str:
  print(i)

#Replicating string
Str = "Hello Python"
A = 3*Str
print(A)

#membership operators on strings.
str = "Hello World"
print('H' in str)
print('H' not in str)
print('y' in str)
print('y' not in str)

#comparison operators on strings.
str1 = 'hello python'
str2 = 'hey user'

a = str1>str2
print (a)
b = str1<str2
print (b)

#slicing on strings.
str = "hello python"
print(str[:6])
print(str[2:4])
print(str[-5:-1])
