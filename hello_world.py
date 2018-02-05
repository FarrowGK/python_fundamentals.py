print "HelloWorld!"
name = "Juan Pablo the Third"
print "My name is", name
print "My name is" + name
print name.count("a") 
#Counts the number of time the substring("a") occurs in a string
print name.endswith("a")
#returns true or false depending on whether or not the string ends with the chosen substring
print name.find("n")
#returns the index where the first occurence of the substring is
print name.isalnum()
#returns if it is greater than 0 and if it only contains numbers and letters. Will return false if there is spaces and special characters.
print name.split()
#splits each element of a string into a list item
#print string.join()
#combines all the strings in a data set contatinated
NWA = ["Dre", "Ice Cube", "Yella"]
#makes a list with values
print NWA
print NWA[1]
NWA.append("Ren")
#adds ren to the end of NWA
print NWA
print NWA[1:3]
#prints all values within that range not including the last one
