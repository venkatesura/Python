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
>>> 
