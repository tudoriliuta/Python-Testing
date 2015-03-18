n=0
k=3
m=1
id_validation_database=[["Conan","1234"],["Samuel","3402"],["Saturn","9930"],["Eclipse","4902"],["Sidan","3320"],["Economica","4930"]]

name=input("USER NAME: ")
pin=input("ID: ")


if [name,pin] in id_validation_database:
    print ("Access granted!")
    n=1
else:
    print ("Access denied!")
    n=n-1


if n==-1:
    print ("Terminal Locked!")
   

if n==1:
    print ("Mainframe interface initiating...")
    n=2

if n==2:
    print ("Welcome "+name)
    print ("You have "+str(m)+ " unread messages")
    print ("Logs registered :" +str(k))
    command=input("Command interface: k - read logs, m - read messages")

    if command=="k" and k>0:
           print ("...")
           print ("Data was corrupted! Please contact the system administrator")
        
    elif command=="k" and k==0:
           print ("There are no logs available")
    elif command=="m" and m==0:
           print ("There are no more messages available")
    elif command=="m" and m>0:
           print ("Welcome to your imbox "+name)
           print ("/n")
           print ("Dear "+name+""",\n My name is Dr. John Samuel Krienger """)
           message=input("This is the end of the message. D - to delete, R - to reply")
           if message=="D":
                  m=0
           elif message=="R":
                  print ("Address is no longer operational - Connection could not be established!")
                 
           else:
               print ("Command unrecognised")
               
                  
                  
    
    
    
    
