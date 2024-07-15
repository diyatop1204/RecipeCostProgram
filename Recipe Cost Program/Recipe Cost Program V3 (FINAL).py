#Created on 31/10/2021
#Version Three (FINAL)
#Recipe Cost Program

#read file in
import csv 
a_dictionary={}
my_file=open("baking_data.csv", "r")

for line in my_file:
    data=[]
    key, value = line.split(":")
    data=value.split(",")
    a_dictionary[key]=data
    
    ingredients=list(a_dictionary.keys())
    measurement=line[0]
    cost=line[1]

#create welcome banner
def welcome():
    print("")
    print("|=============================================================|")
    print("|==**********WELCOME TO THE RECIPE COST CALCULATOR**********==|")
    print("|==******THIS CALCULATOR WILL HELP CALCULATE THE TOTAL******==|") 
    print("|==***COST OF YOUR RECIPE AS WELL AS THE COST PER SERVING***==|")
    print("|=============================================================|")
    print("")

welcome()
    

#ask for the recipe name and serving size
recipe_name=input("Please enter the name of the recipe you would like to bake today: ")
while recipe_name=="":
    recipe_name=input("Please enter the name of the recipe you would like to bake today: ")

serving=""
while True:
    try:
        serving=int(input("Please enter the amount of servings this recipe is for (eg. 2, 4, 6...): "))
        break
    except ValueError:
        print("**PLEASE ENTER A NUMNBER**")
        print("")

#print all ingredients on a seperate lines
print("")
print(*ingredients, sep= "\n")

#ask for how many ingredients will be needed
print("")
total_ing=""
while True:
    try:
        total_ing=int(input("How many ingredients will you need for this recipe? "))
        break
    except ValueError:
        print("**PLEASE ENTER A NUMBER**")
        print("")


user_ingredients={}
ing_red=""
def ingredients():
    #ask for an ingredient required for the recipe
    print("")
    ing_red=input("Please enter an ingredient you require for your recipe (from the list above): ")

    while ing_red=="" or ing_red not in a_dictionary:
        print("")
        ing_red=input("Please enter an ingredient you require for your recipe (from the list above): ")
        
        
    #search for the ingredient inputted in the dictionary
    if ing_red in a_dictionary:
        info=a_dictionary.get(ing_red)
        print("Ingredient: ", ing_red)
        print("Measurement (NZ): ", info[0])
        print("Cost ($NZD): ", info[1])
        
        #ask how much of the ingredient will be needed
        ing=""
        while True:
            try:
                ing=float(input("Please enter how much of this ingredient you will need: ")) 
                break
            except ValueError:
                print("**PLEASE ENTER AN AMOUNT**")       
            
        #adding a values to the dictionary for the users ingredients and the cost
        user_ingredients[ing_red]=[float(info[1])*ing]
           
#ask for each ingredient    
for i in range(total_ing): 
    ingredients()

#print ingredients that user requires on a seperate line
print("")
print("*THE COST PER SERVING WILL BE CALCULATED USING THE FOLLOWING INGREDIENTS*") 
for number, ing_red in enumerate(user_ingredients):
    print(number+1, ing_red)

def data_correct():
    
    def end():
        #creating a list for the costs and finding the sum
        val=list(user_ingredients.values())
        cost_values=[i[0] for i in val]
        total_cost=sum(cost_values)
        
        #printing total cost and cost per serving
        print("The total cost for making", recipe_name, "is: $", "{:.2f}".format(total_cost))
        print("The cost per serving is: $", "{:.2f}".format(total_cost/serving))         
    
    #ask if the ingredients are correct
    correct=""
    #correct=input("Are the ingredients listed above, correct? ")
    yes="yes" or "y" or "YES" or "Y"
    no="no" or "n" or "NO" or "N"
          
    while correct=="" or correct!=no: 
        print("")
        correct=input("Are the ingredients listed above, correct? (yes/no) ")
    
        #if ingredients are correct    
        if correct==yes:
            print("")
            end()  
            return
            
        #if ingredients are incorrect
        elif correct==no:
            ing_change=input("Which ingredient would you like to change? ") 
            
            while ing_change=="" or ing_change not in user_ingredients:
                print("")
                ing_change=input("Which ingredient would you like to change? ") 
                #ing_red=input("Please enter an ingredient you require for your recipe (from the list above): ")
                
            if ing_change in a_dictionary:
                new_ing=""
                while new_ing=="" or new_ing not in a_dictionary:
                    new_ing=input("Which ingredient would you like to change it to? ")
                    print("")
                
                #search for the ingredient inputted in the dictionary
                if new_ing in a_dictionary:
                    info=a_dictionary.get(new_ing)
                    print("Ingredient: ", new_ing)
                    print("Measurement (NZ): ", info[0])
                    print("Cost ($NZD): ", info[1])    
                    
                    #ask how much of the ingredient will be needed
                    ing=""
                    while True:
                        try:
                            ing=float(input("Please enter how much of this ingredient you will need: ")) 
                            break
                        except ValueError:
                            print("**PLEASE ENTER AN AMOUNT**")                    
                    
                    user_ingredients[new_ing]=[float(info[1])*ing]
                    del user_ingredients[ing_change]
                    print("")
                    
                    print("*THE COST PER SERVING WILL BE CALCULATED USING THE FOLLOWING INGREDIENTS*")                
                    print(*user_ingredients, sep= "\n")
                    print("")
                    
                    end()
    
        
if __name__=="__main__":
    data_correct()        
