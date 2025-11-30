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
