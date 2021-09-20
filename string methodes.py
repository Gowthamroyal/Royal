Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> st = "Gowtham Royal"
>>> st
'Gowtham Royal'
>>> st.islower()
False
>>> st.isnumeric()
False
>>> st.isalnum()
False
>>> st.isascii()
True
>>> st.isalpha()
False
>>> st
'Gowtham Royal'
>>> st.isdecimal()
False
>>> st.isdigit()
False
>>> st.isidentifier
<built-in method isidentifier of str object at 0x000002739565B030>
>>> st.isidentifier()
False
>>> st.isprintable()
True
>>> st.isspace()
False
>>> st.istitle()
True
>>> st.isupper()
False
>>> st.capitalize()
'Gowtham royal'
>>> st.
SyntaxError: invalid syntax
>>> st.casefold()
'gowtham royal'
>>> st
'Gowtham Royal'
>>> st.center()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    st.center()
TypeError: center expected at least 1 argument, got 0
>>> st1="mycaptain makes python easy way"
>>> st1
'mycaptain makes python easy way'
>>> st1.center()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    st1.center()
TypeError: center expected at least 1 argument, got 0
>>> st2="gowtham is captain"
>>> st2
'gowtham is captain'
>>> st2.center()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    st2.center()
TypeError: center expected at least 1 argument, got 0
>>> st.count(o)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    st.count(o)
NameError: name 'o' is not defined
>>> st
'Gowtham Royal'
>>> st.count('a')
2
>>> st.encode()
b'Gowtham Royal'
>>> st.endswith('t')
False
>>> st.endswith('l')
True
>>> st.expandtabs()
'Gowtham Royal'
>>> st.find('m')
6
>>> st.rfind('a')
11
>>> st.rindex('a')
11
>>> st
'Gowtham Royal'
>>> st.rindex('o')
9
>>> st.rpartition('royal')
('', '', 'Gowtham Royal')
>>> st.rpartition('Royal')
('Gowtham ', 'Royal', '')
>>> st
'Gowtham Royal'
>>> st.rsplit()
['Gowtham', 'Royal']
>>> st.rstrip()
'Gowtham Royal'
>>> st.split()
['Gowtham', 'Royal']
>>> st.splitlines()
['Gowtham Royal']
>>> st.startswith('w')
False
>>> st.startswith('G')
True
>>> st.swapcase()
'gOWTHAM rOYAL'
>>> st.title
<built-in method title of str object at 0x000002739565B030>
>>> st.title()
'Gowtham Royal'
>>> st.upper()
'GOWTHAM ROYAL'
>>> st.translate()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    st.translate()
TypeError: str.translate() takes exactly one argument (0 given)
>>> st.translate('w')
'Gowtham Royal'
>>> st
'Gowtham Royal'
>>> 