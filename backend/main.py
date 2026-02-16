import random
NOMBRE_MIN = 1
NOMBRE_MAX= 10
NB_QUESTION = 4 


def poser_question(nb_q):

    a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN,NOMBRE_MAX)

    question1  = int(input(f"{nb_q} Calculez : {a} + {b} = "))
    response = int(a+b)    

    if question1 == response :

        print(f'Bravo vous avez eu juste.')

        return True
    
    return False

nb_point= 0

for i in range(0,NB_QUESTION):

    if poser_question(f'Qestion {i+1} :'):
        nb_point += 1

        print()   
    print(f"Votre score est de {nb_point}/{NB_QUESTION} points.") 

 
