#rpccontacts_project/

#rpcontacts/
   # __init__.py
   # views.py
  #  database.py
  #  main.py
  #  model.py

   # import sys
    
   # from .views import Window

    
    

emptynameslist = [" "] * 1001
i = True
while i == True:
    username = input("Enter name: ")
    if username == "end":
        break
    usernamenumber = input("Enter position: ")
    print("Name is " + username + ", " + usernamenumber)
    emptynameslist [int(usernamenumber)] = username

print(emptynameslist)
#if not os.path.exists('Python Practice'):
