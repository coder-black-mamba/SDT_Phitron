n = int(input())
l = input().split()
number_arry = [int(i) for i in l]
n_of_ops=0
# print(number_arry)


def check_all_even(arr):
    for i in range(len(arr)):
        if arr[i]%2!=0:
            return False
    return True

while True:
    if not check_all_even(number_arry):
        break
    else:
        n_of_ops+=1
        for i in range(len(number_arry)):
            number_arry[i]=number_arry[i]//2
print(n_of_ops)