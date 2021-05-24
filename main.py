"""Case-study
Developers:   Ignatovich D. (70%),
              Miller A. (55%),
              Poylova E. (50%)
"""

import random


'''Parameters for starting the game and losing'''
year = 0
dictionary = {'territory': 1000, 'treasury': 1000, 'people': 1000, 'wheat': 5000, 'troubles': 0}
end_ter = random.randint(0, 300)
end_people = random.randint(0, 200)
end_troub = random.randint(50, 100)
end_wheat = random.randint(1, 3)


def print_dict(dictionary):
    for k, v in dictionary.items():
        print(k, ':', v, sep='', end='  ')
    print()
    

def check_game(dictionary, end_ter, end_people, end_troub, year):
    if dictionary['territory'] < end_ter:
        return print("Game over. You've lost territory. You ruled the state N", year)
    elif dictionary['treasury'] < 0:
        return print("Game over. The treasury is empty. You ruled the state N", year)
    elif dictionary['people'] < end_people:
        return print("Game over. Not enough people. You ruled the state N", year)
    elif dictionary['troubles'] > end_troub:
        return print("Game over. You were deposed. You ruled the state N", year)
    return events(dictionary, year)
    
def random_events(dictionary, ter):    
    rand = random.randint(1, 6)
    if rand == 1:
        print('The epidemic has begun! Do you want to allocate money for medicines? (yes/no)')
        answer = input()
        if answer == 'yes':
            dictionary['people'] -= random.randint(0, 100)
            dictionary['treasury'] -= random.randint(100, 900)
        if answer == 'no':
            dictionary['people'] -= random.randint(200, 900)
    elif rand == 2:
        print('The drought has begun! The harvest was lost')
        dictionary['wheat'] -= random.randint(1, ter)
    elif rand == 3:
        print('There was an influx of tourists!')
        dictionary['people'] += random.randint(100, 900)
        dictionary['treasury'] += random.randint(100, 900)
    elif rand == 4:
        print('A new oil field has been discovered!')
        dictionary["treasury"] += random.randint(100, 900)
    elif rand == 5:
        army = random.randint(100, 900)
        print('You were attacked by', army, 'people')
        if army > dictionary['people']:
            dictionary['people'] -= random.randint(100, 500)
        else:
            dictionary['people'] += random.randint(100, 500)
    elif rand == 6:
        print('Quiet environment')
    
    
def events(dictionary, year):
    year += 1
    print(year, 'Year of Government of the state N')
    print_dict(dictionary)

    print('How much territory to give for planting?')
    ter = int(input())
    dictionary['territory'] -= ter
    print_dict(dictionary)
    print('The harvest is over.')
    dictionary['territory'] += ter
    dictionary['wheat'] += ter * random.randint(1, 7)
    print_dict(dictionary)

    random_events(dictionary, ter)
    print_dict(dictionary)

    print('How much wheat to import? (1$ = 5 wheat)')
    wheat = int(input())
    dictionary['wheat'] += wheat
    dictionary['treasury'] -= wheat * 5
    print_dict(dictionary)

    print('How much wheat to give to the people?')
    wheat = int(input())
    if wheat / end_wheat < dictionary['people']:
        print('The people are starving')
        dictionary['troubles'] += random.randint(1, 5)
    dictionary['wheat'] -= wheat
    print_dict(dictionary)

    print('How much wheat to export? (5 wheat = 1$)')
    wheat = int(input())
    dictionary['wheat'] -= wheat
    dictionary['treasury'] += wheat // 5
    print_dict(dictionary)

    print('Set the amount of taxes this year')
    tax = int(input())
    if tax > random.randint(5, 20):
        print('The taxes are too high.The people are not happy.')
        dictionary['troubles'] += random.randint(1, 5)
    dictionary['treasury'] += tax * dictionary['people']
    print_dict(dictionary)
    check_game(dictionary, end_ter, end_people, end_troub, year)
    

def main():
    print("Have you ever dreamed of running a state? You have a great opportunity to show how you are. You are in power in the state ***."+"\n"+ 
"By making annual decisions, you will either stay in power or be overthrown by your people."+"\n"+"Show what you are capable of! Good luck!"+"\n"+"You have certain parameters: land, treasury, wheat, people, troubles.")
    print()
 
    events(dictionary, year)

main()
