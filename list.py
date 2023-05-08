"""
# 1. Write a Python program to sum all the items
a=[1,2,3,4,5]
sum=0
for i in a:
    sum=sum+i
print(sum)

# 2. Write a Python program to multiply all the items in a list
a=[1,2,3,4,5]
sum=1
for i in a:
    sum=sum*i
print(sum)
# 3. Write a Python program to get the largest number from a list
a=[7,5,4,3,9,2]
print(max(a))
max = a[0]
for i in a:
    if i>max:
        max=i
print(max)
# 4. Write a Python program to get the smallest number from a list
a=[7,5,4,3,9,2]
min=a[0]
for i in a:
    if i<min:
        min=i
print(min)
# 5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
word=['kavi',"121",'aruna',"908"]
ch=0
for i in word:
    if(len(i)>2 and (i[0]==i[-1])):
        ch+=1;
print(ch)

# 6. Write a Python program to remove duplicates from a list
word=['kavi',"121",'aruna',"908","121"]
dup=set()
uniq=[]
for i in word:
    if i not in dup:
        uniq.append(i)
        dup.add(i)
ls=list(dup)
print(ls)
# Another method
dup=set(word)
ls=list(dup)
print(ls)
# 7. Write a Python program to check a list is empty or not
a=[1,2,3,4,5]
if(len(a)!=0):
    print("List is Not Empty")
else:
    print("List is Empty")
# 8. Write a Python program to clone or copy a list
a=[1,2,3,4,5,6]
new=[]
for i in a:
    new=a
print(new)
#Another Method
new1=a.copy()
print(new1)
# 9. Write a Python program to find the list of words that are longer than n from a given list of words
n=5
str="Find the List of Words that are Longer than n from a given List of Words"
new_list=[]
text=str.split(" ")
for i in text:
    if(len(i)>n):
        new_list.append(i)
print(new_list)

# 10. Write a Program that get two lists as input and check if they have at least one common member
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
a1 = set(a)
b1 = set(b)
a1.intersection_update(b1)
print(list(a1))
# 11. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. (enumerate)
a = [1, 2, 3, 4, 5, 6]
a.pop(5)
a.pop(4)
a.pop(0)
print(a)
# 12. Write a Python program to print the numbers of a specified list after removing even numbers from it
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in a:
    if i % 2 == 0:
        a.remove(i)
print(a)
#13. Write a Python program to shuffle and print a specified list (shuffle)
a=["Kavin",23,"Male",44,"MCA"]
new=set(a)
print(list(new))

# 14.Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30
l = list()
for i in range(1,30):
	l.append(i**2)
print(l[:5])
print(l[-5:])
"""