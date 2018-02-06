def dictionary_basics(info): 
    print "My name is", info.get("Name")
    print "My age is", info.get("Age")
    print "My of birth is", info.get("Country")
    print "My favorite language is", info.get("Language")

info = {
    "Name" : "Pablo Escobar",
    "Age" : "54",
    "Country" : "Colombia",
    "Language" : "Spanish ",
}

dictionary_basics(info)

