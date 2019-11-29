Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'spam eggs'
'doesn\'t"
"doesn't"
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said."

SyntaxError: multiple statements found while compiling a single statement
>>> 'spam eggs'
'doesn\'t"
"doesn't"
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said."'spam eggs'
'doesn\'t"
"doesn't"
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said."
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 'spam eggs'
'spam eggs'
>>> 'doesn\'t'
"doesn't"
>>> "doesn't"
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\"they said."
'"Yes,"they said.'
>>> '"Isn\t," they said."
SyntaxError: EOL while scanning string literal
>>> '"Isn\t," they said.'
'"Isn\t," they said.'
>>> '"Isn\t," they said.'
'"Isn\t," they said.'
>>> print('"Isn\t," they said.')
"Isn	," they said.
>>> s='First line.\nSecond line.'
>>> s
'First line.\nSecond line.'
>>> print(s)
First line.
Second line.
>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name
>>> print("""\
Usage: thingy [OPTIONS]
-h
-H hostname
""")
Usage: thingy [OPTIONS]
-h
-H hostname

>>> 3*'un'+'ium'
'unununium'
>>> 'Py' 'thon'
'Python'
>>> text=('Put several strings within parantheses '
      'to have them joined together.')
>>> text
'Put several strings within parantheses to have them joined together.'
>>> prefix='Py'
>>> prefix 'thon'
SyntaxError: invalid syntax
>>> prefix + 'thon'
'Python'
>>> word='Python'
>>> word[0]
'P'
>>> word[5]
'n'
>>> word[-1]
'n'
>>> word[-2]
'o'
>>> word[-6]
'P'
>>> word[0:2]
'Py'
>>> word[2:5]
'tho'
>>> word[:2]+word[2:]
'Python'
>>> word[:4]+word[4:]
'Python'
>>> word[:2]
'Py'
>>> word[4:]
'on'
>>> word[-2]
'o'
>>> word[42]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    word[42]
IndexError: string index out of range
>>> word[4:42]
'on'
>>> word[0]='J'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    word[0]='J'
TypeError: 'str' object does not support item assignment
>>> word[2:]='py'
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    word[2:]='py'
TypeError: 'str' object does not support item assignment
>>> 
'J' + word[1:]
'Jython'
>>> word[:2]+'py'
'Pypy'
>>> s='supercalifragilisticexpialidocious'
>>> len(s)
34
>>> s=a
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s=a
NameError: name 'a' is not defined
>>> s='a'
>>> print(str.capitalize(a))
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(str.capitalize(a))
NameError: name 'a' is not defined
>>> print(a.capitalize())
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print(a.capitalize())
NameError: name 'a' is not defined
>>> a=str.capitalize('a')
>>> print(a)
A
>>> s='a'
>>> print(str.capitalize(s))
A
>>> 
