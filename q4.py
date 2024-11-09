import random 


def main() :
    words = [
    "apple", "brave", "crave", "dance", "eagle", "flare", "grace", "heart", "ideal", "joint",
    "knack", "layer", "magic", "niche", "ozone", "prime", "quota", "range", "scope", "trend",
    "unite", "vivid", "whirl", "xenia", "youth", "zealot", "blaze", "chime", "drift", "earth",
    "frost", "glove", "hover", "ivory", "jolly", "kneel", "lodge", "maple", "north", "ocean",
    "peach", "quirk", "realm", "sheep", "trust", "usher", "vicar", "worth", "yield", "zebra" ] 

    index = random.randint(0,49) 
    to_be_guessed = words[index] 
    to_be_guessed = "ozone"

    guess = ""
    chance = 6 
    ans = ["-"]*5 
    while(chance >0) :
        
        while(len(guess) > 5  or len(guess) < 5)  : 
            guess = input("enter your 5 character guess : ") 
            if(len(guess) > 5  or len(guess) < 5) :
                print("invalid input , please enter again !!") 

        
        # resposne = {}
        c = 0 
        for i in range(5) :
            if(guess[i] == to_be_guessed[i]) :
                ans[i] = guess[i] 
                c += 1
        # print(ans)
        residue = [ ]
        dodge = ans.copy()
        # print(ans)
        for i in range(5) :
            if(ans[i]=="-") :
                target = to_be_guessed[i] 
                for j in range(5) :
                    if(guess[j]==target) :
                        if(dodge[j] != "-") :
                            continue 
                        else :
                            residue.append(target)  ## all that is unmatched + the other instance also exists and is  also unmatched 
                            # print(residue) 
                            dodge[j] = 1  
                            break  ## dodging in case of more than 1 same element 

        for i in range(5) :
            print(ans[i],end=" ") 
        
        print()
        if(c == 5) :
            print("congratulations you win !!")
            print("the secrett word was : ",to_be_guessed) 
            break
        else :
            print("other characters present : ",end=" ")     
            for i in range(len(residue)) :
                print(residue[i],end=" ") 
        
        ans = ["-"]*5
        guess = ""
        print()
        chance -= 1
        print("remaining chances :",chance)
    else :
        print("you run out of your chance , you lose ") 
        print("the secrett word was : ",to_be_guessed) 
        if(input("you wonna try again : ").lower() == "yes" ) :
            main() 


if(__name__ == "__main__") :
    main() 





        


    
                       


        



