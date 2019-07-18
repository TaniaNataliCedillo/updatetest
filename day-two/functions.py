#create a fuction that determines cost if disney trip
#adult tickets cost $100 per day
#child ticktes cost $90 per day

#1 adult and 2 childrens for 2 days
#.   $100      $180
# $280 total per day
# $560

# determine total cost of adults
# determine total cost of children
# add them to get daily cost
# multiply by number of days for total cost
def totalcost(adults,children,days):
    oneadult_ticketscost =100
    onechildren_ticketcost=90
    totaladult_cost= adults*oneadult_ticketscost
    totalchildrencost= children*onechildren_ticketcost
    total= (totaladult_cost+totalchildrencost)*days 
    return total
print (totalcost(4,2,2))


def greet(player): 
    if player =="Tania":
        return "Welcome , Tania"
    else: 
        return " Hey" + player

name1= input("Enter player 1's name:")
print (greet(name1))
name2= input("Enter player 2's name:")
print (greet(name2))

def greetOptional(player="user")
    return ("welcome to the game,")+ player
    
greetoptional("tania")
print (greetoptional())


#scope
HermAge= 17

def have_a_birthday()
    global
    HermAge= 25
    HermAge+= 1
    print("Happy Birthday Herm !! You are now" +str(HermAge))
    return HermAge
    
have_a_birthday()
    

    
    
    
    



