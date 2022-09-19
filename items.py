import random
import shutil

if __name__ == "__main__":
    #--------------------------
    #  phones = { - tworzenie słownika
      #   "John Doe": "11-22-33",
      #    "Justin Bieber": "55-33-11",
      # }
    #  phones["Britney Spears"] = "99-00-11" - dodawanie do słownika
    #  print (phones.keys()) - wypisywanie elementów słownika
    #  print (phones.values()) - wypisywanie elementów słownika
    #  print (phones.items()) - wypisywanie elementów słownika
    #  for item in phones.items(): - wypiswanie całego słownika
        #  print (item)
    #  for items in phones.items(): - pętla do wyświetlania słownika
      #   print (phones.items())
    #--------------------------
    #  values = (1, 2, 3, 4, 5, 6, 7) - zdefiniowa krotka
    #  print(values[2:]) - na krotce można wyświetlać dany element, zliczać, wskazywać miejsce na którym jest dany element
    #  values = (1, 2, 3, 4, 5) - to 5 elementowa to krotka, nawiasy otwarte oznaczają że to kropka
    #--------------------------
    #  values = [1, 2, 3, 4, 5] - to 5 elementowa to lista, nawiasy kwadraty oznaczają że to lista
    #  values.insert(2,42) - dodaje dany element na wskazanym miejscu
    #  print(values.count(4)) - zlicza ile razy występuje dany element
    #  print(values.index(4)) - pokazuje na, którym miejscu występuje dany element, jeśli jest kilka takich samych to zwróci miejsce pierwszego elementu
    #  print(values.index(4, 1, 5)) - pokazuje na, którym miejscu występuje dany element, szukamy go między 1 a 5 elementem listy
    #  values.reverse() - odwraca listę
    #  values.clear() - czyści listę
    #  values.pop() - wyświetla ostatni element listy i jednocześnie usuwa go z listy
    #  random.shuffle(values) - mieszanie elementów listy
    #  values.sort(reverse=True) - sortowanie elementów tablicy
    #  for value in values: - pętla do wyświetlania krotki lub listy
    #      print (value)
    #------------------------------------
    #  values = {1, 2, 3, 4, 5, 1, 1} - tworzenie seta
    #  print(values) - wyświetlanie elementów seta, wyświetli tylko unikalne
    #  tuple(values) - konwertowanie listy na krotkę
    #  set(values) - konwertowanie listy na set
    #  list(values) - konwertowanie seta na listę

    folders = [
       "folder1", "folder2"
    ]
    files = [
       "text1.txt", "text2.txt"
    ]
    for source, target in zip(files, folders):
        shutil.move(source, target)

