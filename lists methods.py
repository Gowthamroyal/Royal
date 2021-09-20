Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l1=[5,10,20,30]
>>> l1.index(10)
1
>>> l1.append(15)
>>> l1.append(15)
>>> l1
[5, 10, 20, 30, 15, 15]
>>> l1.extend([89,46])
>>> l1
[5, 10, 20, 30, 15, 15, 89, 46]
>>> l1.insert(3,99)
>>> l1
[5, 10, 20, 99, 30, 15, 15, 89, 46]
>>> l1.pop()
46
>>> l1
[5, 10, 20, 99, 30, 15, 15, 89]
>>> l1.remove(99)
>>> l1
[5, 10, 20, 30, 15, 15, 89]
>>> l1.count(15)
2
>>> l1.reverse()
>>> l1
[89, 15, 15, 30, 20, 10, 5]
>>> l1.sort()
>>> l1
[5, 10, 15, 15, 20, 30, 89]
>>> l1.clear()
>>> l1
[]
>>> 