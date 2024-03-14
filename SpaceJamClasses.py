from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.task.Task import TaskManager
from typing import Callable 
from CollideObjectBase import *

class Planet(SphereCollideObject):
    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, Vec3 (0,0,0), 1.2)
        
         # Load the model

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        
        # Set texture
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        
        self.loader = loader
        self.render = render
        
        #planets
        
class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName,Vec3 (0, 0, 0), 1.2)
        
        # Load the model
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        # Set texture
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        # Set modelNode as the universe
        
        self.loader = loader
        self.render = render

       
class Spaceship(SphereCollideObject):# / player
    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float, taskManager: TaskManager, accept: Callable[[str, Callable], None]):
        super(Spaceship,self).__init__(loader, modelPath, parentNode, nodeName, Vec3 (0, 0, 0), 1)
        
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.taskManager = taskManager
        self.loader = loader
        self.render = render
        self.accept = accept

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        #self.modelNode.setP(100)

        self.setKeyBindings()

    def Thrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyThrust, 'Forward-thrust')
        else: 
            self.taskManager.remove('Forward-thrust')

    def ApplyThrust(self, task):
        rate = 5
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont
        
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'LeftTurn')
        else: 
            self.taskManager.remove('LeftTurn')

    def ApplyLeftTurn(self, task):
        # Half a degree every frame
        rate = 0.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
        
    def RightTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightTurn, 'RightTurn')
        else:
            self.taskManager.remove('RightTurn')

    def ApplyRightTurn(self, task):
        # Half a degree every frame
        rate = 0.5  
        self.modelNode.setH(self.modelNode.getH() - rate)  
        return Task.cont
        
    def PitchForwd(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyPitchForwd, 'PitchForwd')
        else: 
            self.taskManager.remove('PitchForwd')

    def ApplyPitchForwd(self, task):
        # Half a degree every frame
        rate = 0.5  
        self.modelNode.setP(self.modelNode.getP() + rate)  
        return Task.cont
        
    def PitchBack(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyPitchBack, 'PitchBack')
        else: 
            self.taskManager.remove('PitchBack')

    def ApplyPitchBack(self, task):
        # Half a degree every frame
        rate = 0.5  
        self.modelNode.setP(self.modelNode.getP() - rate) 
        return Task.cont
        
    def RollLeft(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRollLeft, 'RollLeft')
        else: 
            self.taskManager.remove('RollLeft')

    def ApplyRollLeft(self, task):
        # Half a degree every frame
        rate = 0.5  
        self.modelNode.setR(self.modelNode.getR() - rate)  
        return Task.cont

    def RollRight(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRollRight, 'RollRight')
        else:
            self.taskManager.remove('RollRight')

    def ApplyRollRight(self, task):
        # Half a degree every frame
        rate = 0.5  
        self.modelNode.setR(self.modelNode.getR() + rate) 
        return Task.cont

    def setKeyBindings(self):  
        # All key Bindings for Spaceship move
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])

        # Keys for left and right
        self.accept('arrow_left', self.LeftTurn, [1])
        self.accept('arrow_left-up', self.LeftTurn, [0])
        self.accept('arrow_right', self.RightTurn, [1])
        self.accept('arrow_right-up', self.RightTurn, [0])

        # Keys for up and down
        self.accept('arrow_up', self.PitchForwd, [1])
        self.accept('arrow_up-up', self.PitchForwd, [0])
        self.accept('arrow_down', self.PitchBack, [1])
        self.accept('arrow_down-up', self.PitchBack, [0])

        # Keys for rotating left and right
        self.accept('a', self.RollLeft, [1])
        self.accept('a-up', self.RollLeft, [0])
        self.accept('d', self.RollRight, [1])
        self.accept('d-up', self.RollRight, [0])
      
class SpaceStation(CollisionCapsuleObject):
    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float, radius: float):
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName,1, -1, 5, 1, -1, -5, 0)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.loader = loader
        self.render = render
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        
        #self.station = loader.loadModel("./Assets/SpaceStation1B/spaceStation.x")


class DroneShowBase():
    # # of Drone
    droneCount = 0