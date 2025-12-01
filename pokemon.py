QUESTION3="Quel est votre nom de dresseur cet essai ?"
dresseur=input(QUESTION3)
print("Bienvenue" + dresseur + ",est-tu prêt à tenter ta chance ?")


class Pokemon:
    def __init__(self,name,nv,TauxSpawn,TauxCapture):
        self.name = name
        self.nv = nv
        self.TauxSpawn = TauxSpawn
        self.TauxCapture = TauxCapture
    def spawn(self):
        print(" Un " + self.name + " de niveau " + self.nv + " sauvage apparait !")
#code spawn 2 pokémon
import random
def generate_number():
    rattata = 0
    roucool = 1
    nidoran = 2
    mew = 3
    rand = random.random()
    print(rand)
    if rand < 0.35:
        return rattata
    elif rand < 0.70:  # 0.35 + 0.35
        return roucool
    elif rand < 0.95:  # 0.70 + 0.25
        return nidoran
    else:
        return mew
#code niveau
if generate_number() == 0:
    import random
    NvPokemonSauvage = random.randint(2,10)
elif generate_number() == 1:
    import random
    NvPokemonSauvage = random.randint(5,15)
elif generate_number() == 2:
    import random
    NvPokemonSauvage = random.randint(8,15)
elif generate_number() == 3:
    import random
    NvPokemonSauvage = random.randint(20,50)


p1 = Pokemon("rattata","nvrat","35","TauxCaptureRat")
p2 = Pokemon("roucool","nvrouc","35","TauxCaptureBird")
p3 = Pokemon("nidoran","nvnido","25","TauxCaptureLapin")
p4 = Pokemon("mew","nvmew","5","TauxCaptureMew")

pokemonList = [p1, p2, p3, p4]
quelPOKEMON = generate_number()
spawn1 = pokemonList[quelPOKEMON]
print(" Un " + spawn1.name + " de niveau " + spawn1.nv + " sauvage apparait !")

TAUXCAPTURERAT=80
TAUXCAPTUREBIRD=75
TAUXCAPTURELAPIN=45
TAUXCAPTUREMEW=10

class Ball:
    def __init__(self,name,nbrBallInvMax,BonusCapture):
        self.name = name
        self.nbrBallInvMax = nbrBallInvMax
        self.BonusCapture = BonusCapture



b1= Ball("pokeball","50","1")
b2= Ball("superball","25","2")
b3= Ball("hyperball","10","3")

QUESTION1="Que voulez-vous faire ? F=fuire C=Capturer"
QUESTION2="Quelle pokeball voulez-vous utiliser ? P=pokeball, S=superball, H= hyperball"

action1=input(QUESTION1)

typeball=input(QUESTION2)
if typeball=="P":
    Ball=b1
if typeball=="S":
    Ball=b2
if typeball=="H":
    Ball=b3
elif typeball!="P" or "S" or "H":
    print("veuillez entrer une valeur de pokeball possible")

TauxCapture=Pokemon.TauxCapture
NvPokemonSauvage=Pokemon.nv
FacteurBall=int(Ball.BonusCapture)
ChanceCapture=((TauxCapture * NvPokemonSauvage) * (FacteurBall))/100


if action1=="F":
    print("Vous avez fui le pokemon sauvage")
if action1=="C":
    print("Vous lancer la pokeball au pokemon sauvage")
    import random
    ChanceDresseur=random.randint(1,100)
    if ChanceCapture<=ChanceDresseur:
        print("Félicitation, vous avez capturé un" + Pokemon.name)
    else:
        print("Dommage, le pokemon est sorti de la pokeball")
        QUESTION4="Voulez-vous réessayer de capturer ou fuir ? C=Capturer F=Fuir"
        repeat=action1=input(QUESTION4)

