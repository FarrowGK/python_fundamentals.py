def stars1(arr):
    string = ""
    star = "*"
    endpoint = len(arr) + 1
    for position in range(0, endpoint):
        print string
        string = ""
        if position == endpoint - 1:
                break
        else:
            number = arr[position]
        for value in range(0, number):
            string += star


arr = [4, 6, 1, 3, 5, 7, 25]
stars1(arr)

def stars2(arr2):
    entered = ""
    star = "*"
    endpoint = len(arr2) + 1
    for position in range(0, endpoint):
        print entered
        entered = ""
        if position == endpoint - 1:
                break
        else:
            stop = arr2[position]
        if type(stop) == int:
            for value in range(0, stop):
                entered += star
        elif type(stop) == str:
            letter = stop[:1]
            for value in range(0, len(stop)):
                entered += letter
        else:
            print "Invalid data type"

arr2 = [4, "larry", 1, 3, "Shaq", 7, "Kobe"]
stars2(arr2)