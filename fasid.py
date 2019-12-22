#Made for the sole purpose of GCI 2019
from fedora.client.fas2 import AccountSystem
print("Note that the data you are going to enter is really important in order to connect with the Fedora database. Please enter correct data")
user=input("Enter Your Username(To connect to Fedora):")
fas = AccountSystem(username=user)
z="Y"
while True:
    if not z=="Y":
        break
    try:
        a=input("Enter the username you want to look for:")
        x=fas.person_by_username(a)
        print("Email id associated with",a,"is: ",x['email'])
        z=input("Do you want to continue(Y or N):")
    except:
        print("The username entered is invalid!")
        z=input("Do you wish to continue(Y or N):")
