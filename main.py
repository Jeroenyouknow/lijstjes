from os.path import exists
import time
import os

def check_user(file,user):
    if exists(file):
        answer = input("U heeft een lijstje wilt u deze openen?\n"
                       "Y/N\n"
                       "> ").lower()
        if answer == 'y':
            print("Uw bestand wordt geopend...")
            time.sleep(1)
            open_file(file,user)
        else:
            print("Uw bestand wordt niet geopend!\n"
                  "Fijne dag!")
            exit()
    else:
        answer = input("U heeft geen lijstje wilt u deze openen?\n"
                       "Y/N\n"
                       "> ").lower()
        if answer == 'y':
            print("Wij gaan deze aanmaken voor u...")
            time.sleep(1)
            create_file(file,user)
        else:
            print("Wij zullen geen bestand aan maken voor u\n"
                  "Fijne dag!")
            exit()

def open_file(file,user):
    fl = open(file, "a")
    answer = input("Wilt u iets aan het lijstje veranderen?\n"
                   "Y/N\n"
                   "> ").lower()
    if answer == "y":
        change_file(file,fl)
    else:
        print("Wij gaan niks veranderen aan uw lijstje\n"
              "Wij wensen u een fijne dag verder!")
        exit()

def change_file(file,fl):
    answer = input("\n"
                   "aWat wilt u doen met uw lijstje?\n"
                   "Als u uw lijstje wilt zien kies dan: 1\n"
                   "Als u iets wilt toevoegen aan uw lijstje kies dan: 2\n"
                   "Als u uw lijstje wilt legen kies dan: 3\n"
                   "Als u uw lijstje wilt verwijderen kies dan: 4\n"
                   "Als u dit programma wilt aflsuiten kies dan : 5\n"
                   "> ")
    if answer == "1":
        fl = open(file)
        txt = fl.read()
        print("In uw lijstje staat: \n" + txt)
    if answer == "2":
        txt = input("Wat wilt u toevoegen aan uw lijstje?\n"
                    "> ")
        if txt == "":
            print("u heeft niks ingevuld er wordt niks toegevoegd aan uw lijstje")
            time.sleep(1)
            change_file(file,fl)
        else:
            statement = input("U wilt het volgende gaan toevoegen: " + txt + "\n"
                 "Wilt u dit toevoegen?  Y/N\n"
                  "> ").lower()
            if statement == "y":
                fl.write(txt + "\n")
                print("De tekst is toegevoegd\n"
                      "Wij wensen u een fijne dag verder!")
                time.sleep(1)
                exit()
            else:
                print("De tekst is niet toegevoegd")
                time.sleep(1)
                change_file(file,fl)
    if answer == "3":
        fl = open(file,"w")
        print("Uw lijstje is geleegd")
        time.sleep(1)
        fl = open(file, "a")
        change_file(file,fl)
    if answer == "4":
        os.remove(file)
        print("Het lijstje is verwijderd\n"
              "Wij wensen u een fijne dag verder!")
        exit()
    if answer == "5":
        print("Het programma wordt afgesloten\n"
              "Wij wensen u een fijne dag verder!")
        exit()
    else:
        time.sleep(1)
        change_file(file,fl)

def create_file(file,user):
    fl = open(file, "w")
    print("\n"
          "Uw lijstje is aangemaakt\n"
          "U kan de volgende keer inloggen met uw naam\n"
          "Wij wensen u een fijne dag verder!")
    exit()






def main():
    user = input("Geef uw gebruikersnaam op:\n"
                 "> ").lower()
    file =  user + "_lijst.txt"
    if user == "":
        print("U heeft geen gebruikersnaam ingevuld!")
        time.sleep(1)
        main()
    else:
        check_user(file,user)
if __name__ == '__main__':

    main()

