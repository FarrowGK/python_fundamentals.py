l = ["magical unicorns", 19, "hello", 98.98, "world"]
totalstring = []
runsum = []

for i in range(0, len(l)):
    if type(l[i]) == str:
        totalstring.append(l[i])
    elif type(l[i]) == int or float or long or complex:
        runsum.append(l[i])
    else:
        print "Invalid data type"
print totalstring
print runsum

runsum = sum(runsum)
print runsum

print " ".join(totalstring)
