oddelovac = "=" * 62
sluzby = ("dostupne filmy", "detaily filmu", "doporuc film")
hodnoceni_uzivatelu = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}


def printDict(dicti: dict, tabs=0):
    for key, value in dicti.items():
        if type(value) == dict:
            print(tabs*'\t', f"{key.capitalize()}:", sep='')
            printDict(value, tabs+1)
        elif type(value) == tuple or type(value) == list:
            print(tabs*'\t', f"{key.capitalize()}: {', '.join(value)}", sep='')
        else:
            print(tabs*'\t', f"{key.capitalize()}: {value}", sep='')


# region Filmy
film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
              "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
              "Jeffrey DeMunn", "Larry Brandenburg"
              )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "93/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
              "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
              "John Marley", "Richard Conte"
              )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
              "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
              "Monique Gabriela", "Ron Dean", "Cillian Murphy"
              )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
              "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
              "David Bowie"
              )
}
# endregion

FILMY = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4
}

name = input("ZADEJ JMENO:")
if name in hodnoceni_uzivatelu.keys():
    print('v poradku'.upper())
    print(oddelovac)
    print("VITEJTE V NASEM FILMOVEM SLOVNIKU".center(62))
    print(oddelovac)
    print("dostupne filmy | detaily filmu | doporuc film".center(62))
    print(oddelovac)
else:
    print("Je mi líto, neexistujete.")
    exit()

service = ""
while not service in {"dostupne filmy", "detaily filmu", "doporuc film"}:
    service = input("VYBER SLUZBU:")
if service == "detaily filmu":
    print("NASE FILMY:", ', '.join(list(FILMY.keys())))
    service = ""
    while not service in set(FILMY.keys()):
        service = input("VYBER FILM:")
    printDict(FILMY[service])
elif service == "doporuc film":
    ratings = {}
    for movie in FILMY.keys():
        ratings[movie] = int(FILMY[movie]['HODNOCENI'][:-4])
    print(', '.join([movie for movie in FILMY if int(
        FILMY[movie]['HODNOCENI'][:-4]) == max(ratings.values())]))
else:
    print("DOSTUPNE FILMY:", ', '.join(list(FILMY.keys())))
