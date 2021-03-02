# Question 1
def add_up(n=0):
    if n == 1:
        return 1
    return add_up(n-1)+n


x = add_up(16)
print(x)


# Question 2
list1 = [8, 15, 32, 42, 60, 75, 122, 132, 150, 180, 190]
for i in list1:
    if i % 4 == 0 and i < 120:
        print(i)


# Question 3
num1 = [5, 15, 20, 25, 30]


def reverseList(num1):
    for item in range(len(num1)//2):
        num1[item], num1[len(num1)-1-item] = num1[len(num1)-1-item], num1[item]
    return num1


num1 = reverseList(num1)
print('reverseList:{}'.format(num1))
