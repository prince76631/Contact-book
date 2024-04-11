
name_store = []
phone_store  = []

def contact_book():
    print('1. Add contact ')
    print('2. Search contact ')
    print('3. Show list ')
    print('4. Remove ')
    print('5. Edit ')
    print('6. Exit ')
    choice = input("\nenter your choice : ")

    
    def add_contact():
     if choice == "1": 
            name = input("\nenter your name : ")
            phone  = input("enter your number  : ")

            if name != "" and phone != "":
                print("\nAdded Successfully : ")
                name_store.append(name)
                phone_store.append(phone) 
            else:
               print("\nName and Number is must : ") 
    add_contact()   


    while True:
     choice = input("\nenter your choice : ") 
     add_contact() 
     
     


     def search_contact():
        if choice == "2":
           name = input("\nenter your name : ")
           phone  = input("enter your number  : ")

           if name in name_store and phone in phone_store:
               if name_store.index(name) == phone_store.index(phone):
                  print('\nHere is your searched contact: ', name, phone )
               else:
                 print("\nIndex value does not match : ")
           else:
               print("\nNot found : ")              
     search_contact()   

     

     def show_list():
        if choice == '3':
           print("Your welcome in the contact list : ")
           print(name_store)
           print(phone_store)             
     show_list() 
        

    
     def delete_name():
        if choice == "4":
           name = input("\nenter your name : ")
           phone  = input("enter your number : ")

           if name in name_store and phone in phone_store:
             if name_store.index(name) == phone_store.index(phone) :
              name_store.remove(name)
              phone_store.remove(phone)
              print("\nSuccessfully Removed ")
             else:
               print("\nindex value does not match : ")  

           else:
              print("\ncontact does not match")  
     delete_name()  
        


     def update_contact():
        if choice == '5':
           name   = input("\nenter your name  : ")
           phone  = input("enter your number  : ")
           
           if name in name_store and phone in phone_store:
              if name_store.index(name) == phone_store.index(phone):
                 update_name = input("\nEdit Contact Name : ")
                 update_phone  = input("Edit Number : ")
                 name_store.remove(name)
                 name_store.append(update_name)
                 phone_store.remove(phone)
                 phone_store.append(update_phone)
                 print("\nUpdated Successfully ")
              else:
                 print("\n Contact does not match")  
           else:
              print("\nDoes Not Exist")        
     update_contact()  


     if choice == "6":
        print("Exited...")
        break
     

     if choice <= "0" or choice >="7":
        print(" Wrong selection ! ")
      
contact_book()



