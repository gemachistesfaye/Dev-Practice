# here is function code

 #this is simple greeting function only  use print for different passengers

def greet(name):
    return f"Hello {name}, welcome to Ethiopian Airlines!"
print(greet("Gemachis Tesfaye"))
print(greet("Donald Trump😁"))  
print(greet("Elon Musk🚀"))
print(greet("Barack Obama"))
print(greet("Bill Gates💻"))

print("          ")
# calculate ticket price after dscount
def calculate(price, discount):
    final_price=price-(price*discount/100)
    return final_price

print("The final price after discount is $", calculate(100,10))
print("The final price after discount is $", calculate(50.3,5))
print("The final price after discount is $", calculate(200,15))

print("          ")
def greet(name, message="welcome to Ethiopain Airlines!"):
    return f"Hello {name}, {message}"

print(greet("Gemachis Tesfaye"))   #output is Hello Gemachis Tesfaye, welcome to Ethiopain Airlines!
print(greet("Donald Trump😁", "we are happy to have you onboard!"))   #output is Hello Donald Trump😁, we are happy to have you onboard!
print(greet("Elon Musk🚀", "enjoy your flight with us!"))   #output is Hello Elon Musk🚀, enjoy your flight with us!

print("          ")
# function with arbitrary number of arguments
def passengers(*names):
    print("The passengers names are :")
    for i in names:
        print(f"-{i}")
passengers("Gemachis Tesfaye", "Sisaay Tasew", "Bonsa Tilahun")

print("          ")
# function with keyword arguments
def passenger(**info):
    print("Passenger Information")
    for key, value in info.items():
        print(f"{key}:{value}")
passenger(Name="Gemachis Tesfaye", Age=21, Seat="12A", From="Addis Ababa", To="London") 
passenger(Name="Sisaay Tasew", Age=22, Seat="17B", From="AbuSera", To="New York")
passenger(Name="Bonsa Tilahun", Age=23, Seat="10C", From="Abusera", To="Dubai")

