import pybullet as p 
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)
planeID = p.loadURDF("plane.urdf")

startPos = [0, 0, 1]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
boxID = p.loadURDF("r2d2.urdf", startPos, startOrientation)
# set the center of mass frame (loadURDF sets base linke frame
for i in range(1000):
    p.stepSimulation()
    time.sleep(1./24)
    
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos, cubeOrn)
p.disconnect()


