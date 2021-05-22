'''Вы когда-нибудь мечтали управлять государством? У вас есть отличная возможность показать на что вы способы. Вы находитесь у власти в государстве ***. 
Принимая ежегодные решения вы будете либо оставаться у власти, либо будете свергнуты своим народом.
Покажите на что вы способны! Удачи!
'''
print("Have you ever dreamed of running a state? You have a great opportunity to show how you are. You are in power in the state ***."+"\n"+ 
"By making annual decisions, you will either stay in power or be overthrown by your people."+"\n"+"Show what you are capable of! Good luck!"+"\n"+"You have certain parameters: land, treasury, wheat, people, troubles.")
def main():
    for key, value in dictionary:
        if land[value] < 300:
            return print("Game over. They ruled the state ***"+ year)
        elif population[value] < 200:
            return print("Game over. They ruled the state ***"+ year)
        elif the_level_of_turmoil[value] > 50:
            return print("Game over. They ruled the state ***"+ year)
        elif treasury[value] =="bankrupt":
            return print("Game over. They ruled the state ***"+ year)
        else:
            continue
main()
