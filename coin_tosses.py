def coin_tosses(attempts):
    import random
    attempt = 0
    heads = 0
    tails = 0
    for attempt in range(0, attempts):
        attempt += 1
        flip = random.randint(0, 1)
        if flip == 1:
            heads += 1
            print "Throwing a coin...Its heads!... Got", heads, "head(s) so far and", tails, "tail(s) so far"
        else:
            tails += 1
            print "Throwing a coin...Its tails!... Got", heads, "head(s) so far and", tails, "tail(s) so far"


attempts = 5000
coin_tosses(attempts)