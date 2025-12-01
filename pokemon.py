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


class Ball:
    def __init__(self,name,nbrBallInv,BonusCapture):
        self.name = name
        self.nbrBallInv = nbrBallInv
        self.BonusCapture = BonusCapture

b1= Ball("pokeball","50","1")
b2= Ball("superball","25","1.25")
b3= Ball("hyperball","10","1.5")

QUESTION1="Que voulez-vous faire ? F=fuire C=Capturer"
QUESTION2="Quelle pokeball voulez-vous utiliser ? P=pokeball, S=superball, H= hyperball"

action=input(QUESTION1)

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
FacteurBall=Ball.BonusCapture
ChanceCapture=(TauxCapture * NvPokemonSauvage) * (FacteurBall)

if action=="F":
    print("Vous avez fui le pokemon sauvage")
if action=="C":
    print("Vous lancer la pokeball au pokemon sauvage")