def different_place(lloc1, lloc2):
    places = [10, 20]
    places[0] = lloc1
    places[1] = lloc2
    print(places)
    places.reverse()
    print(places)


different_place(10, 20)

