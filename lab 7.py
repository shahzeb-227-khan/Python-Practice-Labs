#question 1:
sample = [(2, 3), (4, 7), (8, 11), (3, 6)]

index_1 = []
for tuple in sample:
    index_1.append(tuple[1])

min_value = min(index_1)
max_value = max(index_1)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

# question 2:

import math
dart_hits =((0,0),(10,10),(6,6),(7,8))
radius = 10
for x,y in dart_hits:
    distance = math.sqrt(x**2 + y**2)
    print(distance<radius)


# #question 3:
tuple1= ('anachronistically','counterintuitive')
print(len(tuple1[0]) - len(tuple1[1]))
#
tuple2 =('misinterpretation','misrepresentation')
print(tuple2[0]<tuple2[1])

tuple3 = ('ﬂoccinaucinihilipiliﬁcation')
print('e' not in tuple3)

tuple4 =('counterrevolution','counter','resolution')
sum = len(tuple4[1]) + len(tuple4[2])
print(len(tuple4[0]) == sum)




