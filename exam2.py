#     #!! EXAM Variant N2

#   #1
# class palindrom:
#     def __init__(self, word):
#         self.w=word
#     def info(self):
#         a=self.w[::-1]
#         if a==self.w:
#             return 'Palindrom'
#         else:
#             return 'Palindrom emas'

# word=palindrom('aziza')
# print(word.info())

#   #2
# class LP:
#     def __init__(self, l:list):
#         self.lst=l
#     def info(self):
#         a=[]
#         for i in self.lst:
#             if i%2==0:
#                 a.append(0)
#             else:
#                 a.append(i)
#         return a
#     def info2(self):
#         b=[]
#         for j in self.lst:
#             if j%2!=0:
#                 b.append(j)
#                 if len(b)==0:
#                     return 'Hammasi toq son'

# l=LP([2, 5, 7, 6, 13])
# print(l.info2())

#   #3
# class DA:
#     def __init__(self, num):
#         self.n=num
#     def info(self):
#         c=[]
#         for i in range(2, self.n):
#             if self.n%i==0:
#                 c.append(i)
#         return c
#     def info2(self):
#         s=[]
#         for j in range(2, self.n):
#             if self.n%j==0:
#                 s.append(j)
#                 if len(s)==0:
#                     a='Bu tub son'
#                 else:
#                     a='Bu tub son emas'
#         return a

# num1=DA(37)
# print(num1.info())
# print(num1.info2())
          
#   #4
# class DS:
#     def __init__(self, num):
#         self.n=num
#     def info(self):
#         a=[]
#         for i in self.n:
#             a.append(i)
#         return sorted(a)
#     def info2(self):
#         if self.n[0]==self.n[1]:
#             b=self.n.pop[0]
#             if self.n[0]==self.n[1]:

# num=DS(15)
# print(num.info())

#   #5
# class STA:
#     def __init__(self, set, tuple):
#         self.s={set}
#         self.t=(tuple)
#     # def info(self):
#     def info2(self):
#         a=max(len(self.t))
#         return a    
#     def info3(self):
#         if self.t.isdigit():
#             return 'Tuple faqat sonlardan iborat'
#         else:
#             return 'Tuple soz va raqamlar bilan aralash'

# set1, tuple1=map(input().split())
# set1, set2=STA({12, 'a', 4596}, ('matn', 'python', 1369))      
# print(set1.info())
# print(set1.info2())
# print(set1.info3())
# print(tuple1.info())
# print(tuple1.info2())
# print(tuple1.info3())
