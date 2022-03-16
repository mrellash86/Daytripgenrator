import random

def please_press_enter():
    press_enter = input(" Please press enter to generate your random trip."+ ' ')
    print(press_enter)
    print(print(f'You will be traveling to {random_destinations} by way of {random_transportation}.  When you arrive you will go to the {random_entertainment} and then eat dinner at {random_restaurants}.')
)


destinations = ['Houston', 'Atlanta', 'Las Vegas']
random_destinations = random.choice(destinations)
entertainment = ['Gunrange', 'Skating Ring', 'Massage Parlor', 'Art Gallery']
random_entertainment =  random.choice(entertainment)
transportation = ['car', 'bus', 'crusie', 'airplane']
random_transportation = random.choice(transportation)
restaurants = ['Perrys Steakhouse', 'Ruth Chris', 'Camp', 'Show and Tell']
random_restaurants = random.choice(restaurants)
    
def user_review():
    does_user_accept = input('Type yes if you accept your trip.  Type no to make changes.'+' ')
    print(does_user_accept)
    if(does_user_accept == "yes"):
        print("Enjoy your trip!!!")

    elif(does_user_accept == "no"):
        if_no = input(" To change destination type 1.  To change entertainment press 2.  To change transportation press 3.  To change restaurant press 4"+' ')
        print(if_no)
        if(if_no == '1'):
            random_destinations = random.choice(destinations)
            print(f"Your destination has changed too {random_destinations}")
        elif(if_no == '2'):
            random_entertainment = random.choice(entertainment)
            print(f"Your entertainment has changed too {random_entertainment}")
        elif(if_no == '3'):
            random_transportation = random.choice(transportation)
            print(f"Your transportation has changed too {random_transportation}") 
        if(if_no == '4'):
            random_restaurants = random.choice(restaurants)
            print(f"Your restaurant has changed too {random_restaurants}")  

        no = True 
        while no is True:
            #user_acceptance = input('Do you accept? Type yes or no.')
            if(does_user_accept == "yes"):
                no = False
                
                print('Enjoy your TRIP!!!')
                
            else:
                user_review()
                
                

please_press_enter() 
user_review()






