import pickle

def get_files_data(filename):
    with open(filename,"rb") as file:
        return pickle.loads(file.read())

def recreate_data(result_file,data): #data = {"name":"1.png","size":10000}
    with open(data["name"],"wb") as file:
        file.write(result_file.read(data["size"]))
    
while True:
    choice = input("1 decode 2 exit:")
    if choice == "1":
        result_file = input("Введіть файл для считування даних:")
        data_file = input("Введіть файл із даними:")
        files_data = get_files_data(data_file)
        print(files_data)
        with open(result_file,"rb") as file:
            for data in files_data:
                recreate_data(file,data)

            
    if choice == "2":
        break



