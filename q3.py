import pickle 
import json     

def menu() :
    print("1.insert a new entry ")
    print("2.delete and entry")
    print("3.find all matches with a partial name ")
    print("4.find an entry with a given phone number or email address . ")
    print("5.exit")

def main() :
    f = open("addrbook.txt","a+") 
    d = f.readline() 
    #### the order of dictionary inserton  should be actual dicitonary , email dictionary  and at last ti should be the phone dicitonary 
    # d,e,p = {},{},{}  
    # d = data[0] 
    # email = data[1] 
    # phone = data[2] 

    ####### alternatively lets checkmate using 3 file for  each dictionary 
    e = open("e.txt","a+") 
    email = e.readline() 
    
    p = open("p.txt","a+") 
    phone = p.readline()
    


    menu() 
    op = input("what do you wish to do : ") 
    if(op == 1  ) :  
        n = input("enter name to add to the address book : ") 
        if(d.get(n,None) == None) :
            e = input("please neter your email id : ") 
            p = input("please neter your phone number : ") 
            a = input("please neter your address : ") 
            d[n] = {"email":e,"phone":p,"add":a} 
            email[e] = n
            phone[p] = n 

        else :
            if(type(d[n]) == list) :   ### more than 2 entries already with the samae name 
                e = input("please neter your email id : ") 
                p = input("please neter your phone number : ") 
                a = input("please neter your address : ") 
                d[n].append({"email":e,"phone":p,"add":a})
                email[e] = n
                phone[p] = n 
            else :  ## there is only ne entry with the same name till now  , so we save that data in prev
                prev = d[n] 
                d[n] = [prev] 
                e = input("please neter your email id : ") 
                p = input("please neter your phone number : ") 
                a = input("please neter your address : ") 
                d[n].append({"email":e,"phone":p,"add":a})
                email[e] = n
                phone[p] = n 

    elif(op == 2) :
        n = input("enter the name too delete  : ") 
        if(d.get(n,None) ==None) :
            print("no entry for this name till now , nothing to delte !! ") 
        else :
            ## it is not necessay to dlete data form email and phoen dicitonary as it emaila nd phon enumbers are unique to every indiviasual s thebprogram is only allowinfg  one emaila nd phone per person and deleting this emaila nd phone data for an indivisual that noo only one record that is there are no two people with the sma name , then we can dlete that else that is if there are more than data persons information with the same name and dlete all of then  then tgere will be loss of information which is not good 
            if(type(d[n]) == list) :
                print("please identy which record to delete based on phone number and email ") ## only phone number should also be enough 
                for rec in d[n] : 
                    print("email : ",rec["email"] , " phone : ",rec["phone"]) 
                    if(input("is this the perosn u want ot dlete : ").lower() == "yes") :
                        del email[rec["email"]] 
                        del phone[rec["phone"]] 
                        del rec  
            else :
                del email[d[n]["email"]] 
                del phone[d[n]["phone"]] 
                del d[n] 
                
    elif(op==3) :
        n = input("enter a partial name : ")  
        l = len(n) 
        for i in d.keys() :
            if( i[0:l] == n) :
                if(type(d[i]) == list) :
                    for r in d[i] :
                        print("name : ",i) 
                        print("email",r["email"] ) 
                        print("phone",r["phone"] ) 
                        print("add",r["add"] ) 

                else :
                    print("name : ",i) 
                    print("email",d[i]["email"] ) 
                    print("phone",d[i]["phone"] ) 
                    print("add",d[i]["add"] ) 

    elif(op==4) :
        print("what would u like to search with : ") 
        op = input() 
        if(op.lower() == "email") :
            e = input("enter the email : ") 
            i = email[e] 
            if(type(d[i]) == list) :
                for r in d[i] :
                    print("name : ",i) 
                    print("email",r["email"] ) 
                    print("phone",r["phone"] ) 
                    print("add",r["add"] ) 

            else :
                print("name : ",i) 
                print("email",d[i]["email"] ) 
                print("phone",d[i]["phone"] ) 
                print("add",d[i]["add"] ) 
        elif(op.lower() == "phone") :
            e = input("enter the phone : ") 
            i = phone[e] 
            if(type(d[i]) == list) :
                for r in d[i] :
                    print("name : ",i) 
                    print("email",r["email"] ) 
                    print("phone",r["phone"] ) 
                    print("add",r["add"] ) 

            else :
                print("name : ",i) 
                print("email",d[i]["email"] ) 
                print("phone",d[i]["phone"] ) 
                print("add",d[i]["add"] ) 
        else :
            print("enter a valid response : ")

    else :
        f.truncate(0) 
        f.writeline(d) 
        e.truncate(0) 
        e.writeline(email) 
        p.truncate(0) 
        p.writeline(phone) 


        







    
    e.close()
    p.close() 
    f.close() 