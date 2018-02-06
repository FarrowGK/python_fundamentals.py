def oddeven(start, end):
    for count in range(start, end):
        dividend = count % 2
        if dividend == 0:
            print "Number is ", count, " This is an even number"
        else:
            print "Number is ", count, " This is an odd Number"
start = 1
end = 2000

oddeven(start, end)

def multiply(a, multiplier):
    container = []
    for value in range (0, len(a)):
        total =  a[value] * multiplier
        container.append(total)
    return container
a = [1, 2, 3]
multiplier = 5
multiply(a, multiplier)

def layered_multiples(arr):
    total = multiply(a, multiplier)
    print total
    for lengtharr in range(0, len(total)):
        holder = []
        value = total[lengtharr]
        print value
        arr.append(holder)
        for abcde in range(0, value):
            holder.append("1")
    print arr
arr = []
layered_multiples(arr)