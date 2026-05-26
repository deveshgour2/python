list = []
for i in range(5):
    n= int(input("enter the value of lists:"))
    list .append(n)
def sum_of_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum
print("sum of list: ", sum_of_list(list))