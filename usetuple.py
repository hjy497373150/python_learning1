t = ('胡晋源', 21, True, '湖北武汉')
print(t)
print(t[0])
print(t[3])
for member in t:
    print(member)
t = ('王大锤', 20, True, '云南昆明')
print(t)
person = list(t)
print(person)
person[0] = '李小龙'
person[1] = 25
print(person)
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
