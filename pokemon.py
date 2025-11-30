class Pokemon:
    def __init__(self,name,nv,TauxSpawn,TauxCapture):
        self.name = name
        self.nv = nv
    def spawn(self):
        print("Un" + self.name + "de niveau" + self.nv + "sauvage apparait !")

p1 = Pokemon("rattata","nvrat","TauxSpawnRat","TauxCaptureRat")

p2 = Pokemon("magicarp","nvm","TauxSpawnFish","TauxCaptureFish")

p3 = Pokemon("roucool","nvrouc","TauxSpawnBird","TauxCaptureBird")

p4 = Pokemon("nidoran","nvnido","TauxSpawnLapin","TauxCaptureLapin")

p5 = Pokemon("mew","nvmew","TauxSpawnMew","TauxCaptureMew")