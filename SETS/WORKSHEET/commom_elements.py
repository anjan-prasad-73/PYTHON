my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]

common = set(my_favs) & set(friend_favs)
if common:
    print("Yes! '{}' is common.".format(common.pop()))
