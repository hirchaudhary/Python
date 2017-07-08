
def listToDict():
    name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
    favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
    new_dict = {}
    merge = zip(name,favorite_animal)
    print merge
    new_dict = dict(merge)
    print new_dict
listToDict()