def sum_params(*args):
    print(args)
    return sum(args)

print(sum_params(1,2,3,4,5))


def student(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key} : {value}")

student(name="Satu",age=16,roll_no=846521)