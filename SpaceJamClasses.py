from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class Planet(ShowBase):

    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.loader = loader
        self.render = render

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        #planets
        self.planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet1.reparentTo(self.render)
        self.planet1.setPos(150, 5000, 67)
        self.planet1.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 1.jpg")
        self.planet1.setTexture(tex, 1)

        self.planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet2.reparentTo(self.render)
        self.planet2.setPos(7314, 1274, 976)
        self.planet2.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 2.jpg")  
        self.planet2.setTexture(tex, 1)

        self.planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet3.reparentTo(self.render)
        self.planet3.setPos(11985, 1274, 1112)
        self.planet3.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 3.png")
        self.planet3.setTexture(tex, 1)

        self.planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet4.reparentTo(self.render)
        self.planet4.setPos(9067, 1274, 2378)
        self.planet4.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 4.jpg")
        self.planet4.setTexture(tex, 1)

        self.planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet5.reparentTo(self.render)
        self.planet5.setPos(1382, 1274, 4567)
        self.planet5.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 5.jpg")
        self.planet5.setTexture(tex, 1)

        self.planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet6.reparentTo(self.render)
        self.planet6.setPos(4502, 1274, 6478) 
        self.planet6.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 6.png")
        self.planet6.setTexture(tex, 1)

class Universe:
    def __init__(self, loader, render, modelPath: str, texPath: str, posVec: Vec3, scaleVec: float):

        self.universe = loader.loadModel(modelPath)
        self.universe.reparentTo(render)
        self.universe.setPos(posVec)
        self.universe.setScale(scaleVec)
        self.universe.setName("Universe")

        self.loader = loader
        self.render = render

        tex = loader.loadTexture(texPath)
        self.universe.setTexture(tex, 1)

        self.universe = loader.loadModel("./Assets/Universe/Universe.x")
        self.universe.reparentTo(render)
        self.universe.setScale(15000)
        tex = loader.loadTexture("./Assets/Universe/space-galaxy.jpg")
        self.universe.setTexture(tex, 1)

class Spaceship:# / player
    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.spaceship = loader.loadModel(modelPath)
        self.spaceship.reparentTo(parentNode)
        self.spaceship.setPos(posVec)
        self.spaceship.setScale(scaleVec)

        self.loader = loader
        self.render = render

        self.spaceship.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.spaceship.setTexture(tex, 1)


        self.spaceship = self.loader.loadModel(".\Assets\Khan\Khan.x")
        self.spaceship.reparentTo(self.render)
        self.spaceship.setPos(0, 0, 0) 
        self.spaceship.setScale(10)
        tex = self.loader.loadTexture(".\Assets\Khan\Khan.jpg")
        self.spaceship.setTexture(tex, 1)

        

    def Thrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyThrust, 'Forward-thrust')
        else: self.taskManager.remove('Forward-thrust')

    def ApplyThrust(self,task):
        rate = 3
        trajectoy =self.render.getRelativeVector(self.modelNode,Vec3.forward())
        trajectoy.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectoy * rate)
        return Task.cont
        
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'LeftTurn')
        else: self.taskManager.remove('LeftTurn')

    def ApplyLeftTurn(self,task):
        # half a degree every Frame
        rate = .5
        self.modelNode.setH(self.modelNode.gegetHtPos() +  rate)
        return Task.cont
        
    def RightTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightTurn, 'RightTurn')
        else:self.taskManager.remove('RightTurn')

    def ApplyRightTurn(self, task):
        # half a degree every Frame
        rate = -0.5  
        self.modelNode.setH(self.modelNode.getH() + rate)  
        return Task.cont
        
    def MoveUp(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyMoveUp, 'MoveUp')
        else: self.taskManager.remove('MoveUp')

    def ApplyMoveUp(self, task):
        # half a degree every Frame
        rate = 0.5  
        self.modelNode.setZ(self.modelNode.getZ() + rate)  
        return Task.cont
        
    def MoveDown(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyMoveDown, 'MoveDown')
        else: self.taskManager.remove('MoveDown')

    def ApplyMoveDown(self, task):
        # half a degree every Frame
        rate = -0.5  
        self.modelNode.setZ(self.modelNode.getZ() + rate) 
        return Task.cont
        
    def RotateLeft(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRotateLeft, 'RotateLeft')
        else: self.taskManager.remove('RotateLeft')

    def ApplyRotateLeft(self, task):
        # half a degree every Frame
        rate = 0.5  
        self.modelNode.setP(self.modelNode.getP() + rate)  
        return Task.cont

    def RotateRight(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRotateRight, 'RotateRight')
        else:self.taskManager.remove('RotateRight')

    def ApplyRotateRight(self, task):
        # half a degree every Frame
        rate = -0.5  
        self.modelNode.setP(self.modelNode.getP() + rate) 
        return Task.cont

    def setKeyBindings(self):  #all key Bindings for Spaceship move
        # s
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])

        #  keys for  left and right
        self.accept('arrow_left', self.LeftTurn, [1])
        self.accept('arrow_left-up', self.LeftTurn, [0])
        self.accept('arrow_right', self.RightTurn, [1])
        self.accept('arrow_right-up', self.RightTurn, [0])

        #  keys for  up and down
        self.accept('arrow_up', self.MoveUp, [1])
        self.accept('arrow_up-up', self.MoveUp, [0])
        self.accept('arrow_down', self.MoveDown, [1])
        self.accept('arrow_down-up', self.MoveDown, [0])

        #  keys for rotating left and right
        self.accept('a', self.RotateLeft, [1])
        self.accept('a-up', self.RotateLeft, [0])
        self.accept('d', self.RotateRight, [1])
        self.accept('d-up', self.RotateRight, [0])
      
class SpaceStation:
    def __init__(self, loader, render, modelPath: str, texPath: str, posVec: Vec3, scaleVec: float):

        self.station = loader.loadModel(modelPath)
        self.station.reparentTo(render)
        self.station.setPos(posVec)
        self.station.setScale(scaleVec)
        self.station.setName("SpaceStation")

        self.loader = loader
        self.render = render

        tex = loader.loadTexture(texPath)
        self.station.setTexture(tex, 1)
        
        self.station = loader.loadModel("./Assets/SpaceStation1B/spaceStation.x")
        self.station.reparentTo(render)
        self.station.setPos(1000, 5000, 80)
        self.station.setScale(50)
        tex = loader.loadTexture("./Assets/SpaceStation1B/SpaceStation1_Dif2.png")
        self.station.setTexture(tex, 1)


class DroneShowBase():
    # # of Drone
    droneCount = 0