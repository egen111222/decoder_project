# R  read читати як текст readlines читати яки список рядків
# W write записати
# A write записати

# RB read читати як текст readlines читати яки список рядків
# WB write записати
# AB write записати
import os
import pickle
import json


'''
data = [1,2,1,3,2,4,5,345,34,534,534,534,54,{"1":[1,3,2,4,3,5,{"15":155}]}]
# Кодувати dumps
# Декодувати loads
result_data = pickle.dumps(data)
print(result_data)

with open(FILENAME,"rb") as file:
    print(pickle.loads(file.read()))
'''
# Кодувати dumps
# Декодувати loads
import jsonpickle

files_data = []

def get_file_data(filename):
    with open(filename,"rb") as file:
        return {"name":filename,"size":len(file.read())}

'''
[{"1.png","size":200},
 {"2.png","size":300},
 {"3.png","size":400},
 {"4.png","size":500},
 {"5.png","size":600}]
'''

def write_filedata(result_file,file):
    with open(file["name"],"rb") as data:
        result_file.write(data.read())
        
def save_file_data(filename,files_data):
    with open(filename,"wb") as data_file:
        data_file.write(pickle.dumps(files_data))
        
while True:
    choice = input("""1 додати файл
2 переглянути файли
3 очистити список файлів
4 записати дані до файлу
q вийти із програми:""")
    if choice == "1":
        files_data.append(get_file_data(input("Введіть назву файлу або повну адресу:")))
    if choice == "2":
        print(files_data)
    if choice =="3":
        file_data.clear()
    if choice == "4":
        new_file = input("Введіть назву результуючого файлу:")
        with open(new_file,"wb") as result_file:
            for file in files_data:
                write_filedata(result_file,file)
        save_file_data("db.txt",files_data)
        print("ЗАПИСАНО УСПІШНО ДАНІ У db.txt")       
    if choice == "q":
        break



