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
        print("Un" + self.name + "de niveau" + self.nv + "sauvage apparait !")



p1 = Pokemon("rattata","nvrat","35","TauxCaptureRat")
p2 = Pokemon("roucool","nvrouc","35","TauxCaptureBird")
p3 = Pokemon("nidoran","nvnido","25","TauxCaptureLapin")
p4 = Pokemon("mew","nvmew","5","TauxCaptureMew")

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
b2= Ball("superball","25","1.25")
b3= Ball("hyperball","10","1.5")

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

TauxCapture=5.0 #Pokemon.TauxCapture
NvPokemonSauvage=15#Pokemon.nc
FacteurBall=Ball.BonusCapture
ChanceCapture=(TauxCapture * NvPokemonSauvage) * (FacteurBall)

if action1=="F":
    print("Vous avez fui le pokemon sauvage")
if action1=="C":
    print("Vous lancer la pokeball au pokemon sauvage")
    if ChanceCapture>=TauxCapture:
        print("Félicitation, vous avez capturé un" + Pokemon.name)
    else:
        print("Dommage, le pokemon est sorti de la pokeball")
        QUESTION4="Voulez-vous réessayer de capturer ou fuir ? C=Capturer F=Fuir"
        repeat=action1=input(QUESTION4)