numbers = [1, 2, 3, 4, 5]
#print(numbers)
num = []
for i in numbers:
    num.append(i**2)
print(num)

#[<result> for <iterator> in <list>]
ip = list(range(20))
loop = [i**2 for i in range(6)]
print (loop)