from panda3d.core import PandaNode, Loader , NodePath, CollisionNode, CollisionSphere, CollisionInvSphere, CollisionCapsule, Vec3

class PlacedObject(PandaNode):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, radius: float):
        super().__init__(nodeName)

        self.modelPath = loader.loadModel(modelPath)
        
        if not isinstance(self.modelPath, NodePath):
            raise AssertionError(f"PlacedObject loader.loadModel({modelPath}) did not return a proper PandaNode!")
        
        self.modelPath.reparentTo(parentNode)

class CollidableObject(PlacedObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, radius: float):
        super().__init__(loader, modelPath, parentNode, nodeName, posVec, radius)

        self.collisionNode = self.modelPath.attachNewNode(CollisionNode(nodeName + '_cNode'))

class InverseSphereCollideObject(CollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, colRadius: float):
        super().__init__(loader, modelPath, parentNode, nodeName, colPositionVec, colRadius)

        self.collisionNode.node().addSolid(CollisionCapsule(colPositionVec, colRadius))
        #self.collisionNode.show()

class CollisionCapsuleObject(CollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, ax: float, ay: float, az: float, bx: float, by: float, bz: float, r: float):
        super().__init__(loader, modelPath, parentNode, nodeName, Vec3(ax, ay, az), r)

        self.collisionNode.node().addSolid(CollisionCapsule(Vec3(ax, ay, az), Vec3(bx, by, bz), r))
        self.collisionNode.show()

class SphereCollideObject(CollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, center: Vec3, radius: float):
        super().__init__(loader, modelPath, parentNode, nodeName, center, radius)

        self.collisionNode = self.modelPath.attachNewNode(CollisionNode(nodeName + '_collision'))
        collisionSphere = CollisionSphere(center, radius)
        self.collisionNode.node().addSolid(collisionSphere)
        self.modelPath.setCollideMask(1)  # Collide with all objects
