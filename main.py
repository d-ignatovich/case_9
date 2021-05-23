'''Вы когда-нибудь мечтали управлять государством? У вас есть отличная возможность показать на что вы способы. Вы находитесь у власти в государстве ***. 
Принимая ежегодные решения вы будете либо оставаться у власти, либо будете свергнуты своим народом.
Покажите на что вы способны! Удачи!
'''

import random

print("Have you ever dreamed of running a state? You have a great opportunity to show how you are. You are in power in the state ***."+"\n"+ 
"By making annual decisions, you will either stay in power or be overthrown by your people."+"\n"+"Show what you are capable of! Good luck!"+"\n"+"You have certain parameters: land, treasury, wheat, people, troubles.")

def main():
    '''Parameters for starting the game and losing'''
    year = 1
    dict = {'territory': 1000, 'treasury': 1000, 'people': 1000, 'wheat': 5000, 'troubles': 0}
    end_ter = random.randint(0, 300)
    end_people = random.randint(0, 200)
    end_troub = random.randint(50, 100)
    end_wheat = random.randint(1, 3)
    
    for k, v in dict.items():
        print(k, ':', v, sep ='', end='  ')

    '''check_game(end_ter, end_people, end_troub, end_wheat, year)'''
    

def check_game(end_ter, end_people, end_troub, end_wheat, year):
    if dict['territory'] < end_ter:
        return print("Game over. You've lost territory. You ruled the state N"+ year)
    elif dict['treasury'] < 0:
        return print("Game over. The treasury is empty. You ruled the state N"+ year)
    elif dict['people'] < end_people:
        return print("Game over. Not enough people. You ruled the state N"+ year)
    elif dict['troubles'] > end_troub:
        return print("Game over. You were deposed. You ruled the state N"+ year)
    elif dict['wheat'] // dict['people'] < end_wheat:
        a = random.randint(0, 10)
        dict['troubles'] += a
        return print('Hunger. The level of troubles increased by', a)
    return year+1
    

main()
