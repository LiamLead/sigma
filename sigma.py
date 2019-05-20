number = int(input("Number: "))


def one_to_n(num=10):
    i = 1
    sum_num = 0
    while i <= num:
        sum_num += i
        i += 1
    return sum_num

print(one_to_n(number))
