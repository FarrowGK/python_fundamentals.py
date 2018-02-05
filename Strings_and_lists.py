words = "It's thanksgiving day. It's my birthday,too!"
array =[]
array = words.split()
print array
value = array.index("day.")
print value
array[value] = "month."
print array
print " ".join(array)

minmax = [2,54,-2,7,12,98]
print min(minmax)
print max(minmax)

firstlast = ["hello",2,54,-2,7,12,98,"world"]
lenfl = len(firstlast)
print firstlast[0]
print firstlast[lenfl - 1]

x = [19,2,54,-2,7,12,98,32,10,-3,6,100]
x.sort()
lenx = len(x)
split = lenx / 2
print split
print x
listx = x[split:]
listpush = x[0:split]
print listpush
print listx
x[0:split] = []
print x
lenx = len(x)
x.append(listpush)
print x






