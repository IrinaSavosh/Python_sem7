from random import *
import json
karaoke_songs = []

def save():
   with open("karaoke_songs.json", "w", encoding = "utf-8") as fh:
      fh.write(json.dumps(karaoke_songs, ensure_ascii=False))
   print("Список песен сохранен в файле karaoke_songs.json")


def load():
   with open("karaoke_songs.json") as f:
    file_content = f.read()
    karaoke_songs = json.loads(file_content)
   print("Список песен загружен")   


try:
   with open("karaoke_songs.json", "r", encoding = "utf-8") as fh:
      karaoke_songs =json.load(fh)
   print("Список песен загружен") 
except:
   karaoke_songs.append("Город 312 - Останусь")
   karaoke_songs.append("Christina Aguilera - Hurt")
   karaoke_songs.append("Алсу - Зимний сон")
   karaoke_songs.append("Валерий Меладзе - Салют, Вера")


while True:
   command = input("Введите команду: ")
   if command == "1":
      print("Бот начал свою работу")
   elif command == "0":
      save()
      print("Бот остановил свою работу. Заходите еще, будем рады!")
      break
   elif command == "111":
      print("Вот текущий список песен:")
      print(karaoke_songs)
   elif command =="+":
      f = input("Введите исполнителя - название песни: ")
      karaoke_songs.append(f)
      print("Трек был успешно добавлен в каталог!")
   elif command == "911":
      print("1 - начало работы, \n111 - весь список песен, ")
      print("+ - добавление песни, \n- - удаление песни, \n? - случайный выбор песни")
      print("7 - сохранение в файл json, \n8 - загрузка из файла json, \n0 - окончание работы")
   elif command == "-":
      f = input("Введите название песни: ")
      try:
         karaoke_songs.remove(f)
         print("Песня удалена")
      except:
            print("Такого трека нет в списке")
   elif command == "?":
      rnd = randint(0, len(karaoke_songs)-1)
      print("Пойте " + karaoke_songs[rnd])
   elif command == "7":
      save()
   elif command == "8":
      load()
      
   else:
      print("Неопознанная команда. Просьба изучить мануал через 911")