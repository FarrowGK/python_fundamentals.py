for count in range(0, 1000):
    mod = count % 2
    if mod != 0:
        print count
    else:
        pass
for count in range(0, 1000000):
    if count % 5 == 0:
        print count
    else:
        pass

a = [1,9,-3,2,1,11,47,45,19,81]
sum_a = sum(a)
print sum_a

len_a = len(a)
average = sum_a / len_a
print average

