QUESTION3="Quel est votre nom de dresseur cet essai ?"
dresseur=input(QUESTION3)
print("Bienvenue" + dresseur + ",est-tu prêt à tenter ta chance ?")


class Pokemon:
    def __init__(self, name, nv, TauxSpawn, TauxCapture):
        self.name = name
        self.nv = nv
        self.TauxSpawn = TauxSpawn
        self.TauxCapture = TauxCapture
#code spawn 2 pokémon
import random
def generate_number():
    rand = random.random()
    if rand < 0.35:
        return 0
    elif rand < 0.70:  # 0.35 + 0.35
        return 1
    elif rand < 0.95:  # 0.70 + 0.25
        return 2
    else:
        return 3

# Créer les templates de Pokémon (nv sera défini au spawn)
p1 = Pokemon("rattata", None, 35, 80)
p2 = Pokemon("roucool", None, 35, 75)
p3 = Pokemon("nidoran", None, 25, 45)
p4 = Pokemon("mew", None, 5, 10)

pokemonList = [p1, p2, p3, p4]

# Choisir l'espèce à spawn
quelPOKEMON = generate_number()
spawn1 = pokemonList[quelPOKEMON]
if quelPOKEMON == 0:
    level = random.randint(2, 10)
elif quelPOKEMON == 1:
    level = random.randint(5, 15)
elif quelPOKEMON == 2:
    level = random.randint(8, 15)
else:
    level = random.randint(20, 50)

# Affecter le niveau à l'instance spawnée
spawn1.nv = level

print("Un " + spawn1.name + " de niveau " + str(spawn1.nv) + " sauvage apparait !")

TAUXCAPTURERAT=80
TAUXCAPTUREBIRD=75
TAUXCAPTURELAPIN=45
TAUXCAPTUREMEW=10

class Ball:
    def __init__(self, name, nbrBallInvMax, BonusCapture):
        self.name = name
        self.nbrBallInvMax = nbrBallInvMax
        self.BonusCapture = BonusCapture


b1 = Ball("pokeball", 50, 1)
b2 = Ball( "superball", 25, 2)
b3 = Ball("hyperball", 10, 3)

QUESTION1="Que voulez-vous faire ? F=Fuir C=Capturer: "
QUESTION2="Quelle pokeball voulez-vous utiliser ? P=pokeball, S=superball, H=hyperball: "

# Boucle pour redemander l'action si invalide
while True:
    action1 = input(QUESTION1)
    if action1.lower() in ["f", "c"]:
        break
    else:
        print(" Veuillez entrer F (Fuir) ou C (Capturer) !")

if action1.lower() == "f":
    print("Vous avez fui le pokemon sauvage !")
    exit()

# Boucle pour redemander la pokéball si invalide
while True:
    typeball = input(QUESTION2)
    if typeball.lower() in ["p", "s", "h"]:
        break
    else:
        print(" Veuillez entrer P (pokeball), S (superball) ou H (hyperball) !")

if typeball.lower() == "p":
    Ball = b1
elif typeball.lower() == "s":
    Ball = b2
elif typeball.lower() == "h":
    Ball = b3



TauxCapture = spawn1.TauxCapture
NvPokemonSauvage = spawn1.nv
FacteurBall = int(Ball.BonusCapture)
TauxSucces = (TauxCapture * FacteurBall) / (NvPokemonSauvage / 10) 
TauxSucces = min(TauxSucces, 100)  # Limiter à 100%

if action1.lower() == "c":
    print("Vous lancez la pokeball au pokemon sauvage !")
    ChanceDresseur = random.randint(1, 100)
    print(f"Votre tir: {ChanceDresseur}, Taux de succès: {TauxSucces:.1f}%")
    if ChanceDresseur <= TauxSucces:
        print(f" Félicitation ! Vous avez capturé un {spawn1.name} de niveau {spawn1.nv} !")
    else:
        print(f"Dommage, le {spawn1.name} est sorti de la pokeball et a fui...")
       

