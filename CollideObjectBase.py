from panda3d.core import PandaNode, Loader , NodePath, CollisionNode, CollisionSphere, CollisionInvSphere, CollisionCapsule, Vec3

class PlacedObject(PandaNode):

    def __init__(self, Loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        self.modelPath: NodePath = Loader.LoadModel(modelPath)

        if not isinstance(self.modelNode, NodePath):
            raise AssertionError("PlacedObject Loader.LoadModel ("+ modelPath + ") did not return a proper PandaNodel!")
        
        self.ModelNode.reparentTo(parentNode)
        self.modelNode.setName(nodeName)


class CollidableObject(PlacedObject):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, colRadius: float):
        super().__init__(loader, modelPath, parentNode, nodeName)  # Provide dummy values for capsule parameters
        self.collisionNode.node().addSolid(CollisionCapsule(colPositionVec, colRadius))
        self.collisionNode.show()

class InverseSphereCollideObject(CollidableObject):

    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, colRadius: float):
        super().__init__(loader, modelPath, parentNode, nodeName, 0, 0, 0, 0, 0, 0, 0)  # Provide dummy values for capsule parameters
        self.collisionNode.node().addSolid(CollisionCapsule(colPositionVec, colRadius))
        self.collisionNode.show()