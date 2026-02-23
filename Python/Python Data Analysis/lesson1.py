airlines="Ethiopian Airlines"   ##string
passengers=170                   ##integer
from_city ="Addis Ababa"          ##string
to_city="Hawassa"               ##string
price="$50.3"                   ##float
date="August 27, 2025"          ##string
time="Morning"                  ##string
departure_time="2:25 LT"        ##string
arrival_time="3:05 LT"          ##string
is_flight_on_time=True          ##boolean

print(airlines, "have", passengers, "passengers that departure from", from_city, "into", to_city, 
      "the total price for this travel is" , price, "which flight is start Morning at" , departure_time, "and arrived at" , arrival_time, "is found = " ,is_flight_on_time)

## OUTPUT IS
# Ethiopian Airlines have 170 passengers that departure from Addis Ababa into Hawassa the total price for this travel is $50.3 which flight is start Morning at 2:25 LT and arrived at 3:05 LT is found =  True

print("          ")
print("                   ")

# next is list or commonly known as collecton of items

passengers_names=["Gemachis Tesfaye", "Sisaay Tasew", "Bonsa Horsa", "Samuel Tilahun", "Daniel Alemayehu"]
print(passengers_names[0])
print(passengers_names[1])
print(passengers_names[2])
print(passengers_names[3])
print(passengers_names[4])
print(passengers_names)
print(type(passengers_names))
print(len(passengers_names))
passengers_names.append("Abebe Guta")
print(passengers_names)
passengers_names.remove("Gemachis Tesfaye")
print(passengers_names)

print("          ")
print("                   ")

## below is practice of Dictionaries 

passengers_info={
    "Name": "Gemachis Tesfaye",
    "Age" : 21,
    "Seat": "12A",
    "From": "Addis Ababa",
    "To": "Hawassa",
}
print(passengers_info)
print(type(passengers_info))
print(len(passengers_info))
print(passengers_info["Name"])
print(passengers_info["Age"])
print(passengers_info["Seat"])
print(passengers_info["From"])
print(passengers_info["To"])

passengers_info["Age"]=22  ## update the age
passengers_info["Seat"]="14B"  ## update the seat
print(passengers_info)

passengers_info["Country"]="Ethiopian"  # added new key and their value
print(passengers_info)

del passengers_info["From"]  # removed From key from dictionary
print(passengers_info)

# next is list+dictionary  which is list of dictionary

print("          ")
print("                   ")

Passenger= [
    {"name": "Gemachis Tesfaye", "Age":21, "Seat":"12A", "Destination":"Adama"},
    {"name":"Sisaay Tasew", "Age": 22, "Seat":"17B", "Destination":"Mojo"},
    {"name":"Bonsa Tilahun", "Age":23, "Seat":"10C", "Destination": "Bishoftu"},
    {"name":"Samuel Tilahun", "Age": 21, "Seat":"9B", "Destination":"Bishoftu"},
    {"name":"Daniel Alemyew", "Age":20, "Seat": "15D", "Destination":"Dukem"}
]

print(Passenger[0])
print(Passenger[1])
print(Passenger[2])
print(Passenger[3])
print(Passenger[4])
print(Passenger)
print(type(Passenger))
print(len(Passenger))
print(Passenger[0]["name"])     ##accessing the value of name key from 1st dictionary
print(Passenger[4]["Age"])     ##accessing the value of Age key from 5th dictionary
print(Passenger[2]["Seat"])    ##accessing the value of Seat key from 3rd dictionary
print(" ")

for i in Passenger: print(i["name"], "is going into", i["Destination"])
for p in Passenger:
    if p["Age"]>21:
        print(p["name"] , "is above 21 years old")

Passenger.append({"name":"Abdi Guta", "Age":25, "Seat":"19B", "Destination":"Asella"})  #added new dictionary to the list
print(Passenger)
print(" ")
del Passenger[1]  # removed 2nd dictionary from the list which is named Sisaay Tasew
print(Passenger)
print("          ")
print(sorted(Passenger, key=lambda p:p["name"]))  # sorted the list of dictionary by their name in ascending order
print("")
print(sorted(Passenger, key=lambda a:a["name"], reverse=True))  # sorted the list of dictionary by their name in descending order
print("    ")
count=0
for n in Passenger:     
    if n["Age"]==21: count+=1   # count the number of passengers whose age is 21 years old
print("the number of passengers whosoe age is 21 years old is =", count)  # OUTPUT IS the number of passengers whosoe age is 21 years old is = 2

print("          ")

# added some loop 
for i in range(5):
    print("Hello, welcome to Python")  #print this statement 5 times

print(" Passengers going to Bishoftu are :")
for p in Passenger:
     if p["Destination"] =="Bishoftu":
        print("-", p["name"])

print("          ")

city_count={}
for p in Passenger:
  city=p["Destination"]
  if city in city_count:
      city_count[city]+=1
  else:
      city_count[city]=1
      print(city_count)    # OUTPUT IS {'Adama': 1, 'Mojo': 1, 'Bishoftu': 1, 'Dukem': 1, 'Asella': 1}


