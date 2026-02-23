import csv
with open("Python Data Analysis\\passengers.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# OUTPUT

# {'Name': 'Gemachis Tesfaye', 'Age': '21', 'Seat': '12A', 'Destination': 'Adama'}
# {'Name': 'Sisaay Tasew', 'Age': '22', 'Seat': '17B', 'Destination': 'Mojo'}
# {'Name': 'Bonsa Tilahun', 'Age': '23', 'Seat': '10C', 'Destination': 'Bishoftu'}
# {'Name': 'Samuel Tilahun', 'Age': '21', 'Seat': '9B', 'Destination': 'Bishoftu'}
# {'Name': 'Daniel Alemyew', 'Age': '20', 'Seat': '15D', 'Destination': 'Dukem'}
# {'Name': 'Abebe Kebede', 'Age': '35', 'Seat': '22C', 'Destination': 'Hawassa'}
# {'Name': 'Chaltu Dadi', 'Age': '28', 'Seat': '05A', 'Destination': 'Bishoftu'}
# {'Name': 'Birhanu Lemma', 'Age': '41', 'Seat': '18F', 'Destination': 'Adama'}
# {'Name': 'Tigist Mamo', 'Age': '19', 'Seat': '03B', 'Destination': 'Ziway'}
# {'Name': 'Yonas Getachew', 'Age': '50', 'Seat': '25E', 'Destination': 'Shashemene'}
# {'Name': 'Fikirte Bekele', 'Age': '24', 'Seat': '07D', 'Destination': 'Hawasa'}
# {'Name': 'Solomon Hailu', 'Age': '30', 'Seat': '11A', 'Destination': 'Dire Dawa'}
# {'Name': 'Eleni Tesfaye', 'Age': '27', 'Seat': '14C', 'Destination': 'Gonder'}
# {'Name': 'Dawit Mekonnen', 'Age': '33', 'Seat': '08B', 'Destination': 'Bahir Dar'}
# {'Name': 'Sara Kassahun', 'Age': '26', 'Seat': '02F', 'Destination': 'Dessie'}
# {'Name': 'Kebede Worku', 'Age': '45', 'Seat': '20A', 'Destination': 'Jimma'}
# {'Name': 'Aster Ayele', 'Age': '29', 'Seat': '06E', 'Destination': 'Nekemte'}
# {'Name': 'Mulugeta Abebe', 'Age': '38', 'Seat': '16B', 'Destination': 'Arba Minch'}
# {'Name': 'Zewditu Lemma', 'Age': '25', 'Seat': '04D', 'Destination': 'Gambella'}
# {'Name': 'Tadesse Gebre', 'Age': '40', 'Seat': '19C', 'Destination': 'Mekelle'}

print("          ")

# reading csv file and storing data into a list of dictionary
passengers=[]
with open("Python Data Analysis\\passengers.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Age"]=int(row["Age"])  # convert Age value from string to integer
        passengers.append(row)  

print(passengers) 
#OUTPUT

# [{'Name': 'Gemachis Tesfaye', 'Age': 21, 'Seat': '12A', 'Destination': 'Adama'}, {'Name': 'Sisaay Tasew', 'Age': 22, 'Seat': '17B', 
#   'Destination': 'Mojo'}, {'Name': 'Bonsa Tilahun', 'Age': 23, 'Seat': '10C', 'Destination': 'Bishoftu'}, {'Name': 'Samuel Tilahun', 
#    'Age': 21, 'Seat': '9B', 'Destination': 'Bishoftu'}, {'Name': 'Daniel Alemyew', 'Age': 20, 'Seat': '15D', 'Destination': 'Dukem'}, 
#    {'Name': 'Abebe Kebede', 'Age': 35, 'Seat': '22C', 'Destination': 'Hawassa'}, {'Name': 'Chaltu Dadi', 'Age': 28, 'Seat': '05A', 
#    'Destination': 'Bishoftu'}, {'Name': 'Birhanu Lemma', 'Age': 41, 'Seat': '18F', 'Destination': 'Adama'}, {'Name': 'Tigist Mamo', 
#     'Age': 19, 'Seat': '03B', 'Destination': 'Ziway'}, {'Name': 'Yonas Getachew', 'Age': 50, 'Seat': '25E', 'Destination': 'Shashemene'}, 
#     {'Name': 'Fikirte Bekele', 'Age': 24, 'Seat': '07D', 'Destination': 'Hawasa'}, {'Name': 'Solomon Hailu', 'Age': 30, 'Seat': '11A', 
#     'Destination': 'Dire Dawa'}, {'Name': 'Eleni Tesfaye', 'Age': 27, 'Seat': '14C', 'Destination': 'Gonder'}, {'Name': 'Dawit Mekonnen', 
#     'Age': 33, 'Seat': '08B', 'Destination': 'Bahir Dar'}, {'Name': 'Sara Kassahun', 'Age': 26, 'Seat': '02F', 'Destination': 'Dessie'}, 
#     {'Name': 'Kebede Worku', 'Age': 45, 'Seat': '20A', 'Destination': 'Jimma'}, {'Name': 'Aster Ayele', 'Age': 29, 'Seat': '06E', 
#      'Destination': 'Nekemte'}, {'Name': 'Mulugeta Abebe', 'Age': 38, 'Seat': '16B', 'Destination': 'Arba Minch'}, {'Name': 'Zewditu Lemma', 
#      'Age': 25, 'Seat': '04D', 'Destination': 'Gambella'}, {'Name': 'Tadesse Gebre', 'Age': 40, 'Seat': '19C', 'Destination': 'Mekelle'}]

print(type(passengers)) # OUTPUT IS <class 'list'>
print("The total number of passengers are :", len(passengers))  # OUTPUT IS 20
print("first pessenger information", passengers[0]) # OUTPUT IS first pessenger information {'Name': 'Gemachis Tesfaye', 'Age': 21, 'Seat': '12A', 'Destination': 'Adama'}

print("")
ages =[n["Age"]for n in passengers]
av_age=sum(ages)/len(ages)
youngest=min (ages)
oldest=max(ages)

print("The average age of the passengers is :", av_age) # OUTPUT IS The average age of the passengers is : 30.0
print("The youngest passenger is :", youngest) # OUTPUT IS The youngest passenger is : 19
print("The oldest passenger is :", oldest) # OUTPUT IS The oldest passenger is : 50