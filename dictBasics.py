#Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.
def me():
    about = {
        "name": "Hiral",
        "age": 23,
        "country of birth": "India",
        "Favorite language": "Gujarati"
    }
    for key in about:
        print "My {} is {}".format(key, about[key])
me()