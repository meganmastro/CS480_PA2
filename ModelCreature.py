"""
:author: Megan Mastrorilli
:version: 2021.2.1
"""

from Component import Component
from Point import Point
import ColorType as Ct

# import Face component classes
from DisplayableSphere import DisplayableSphere
from DisplayableCube import DisplayableCube
from DisplayableLimb import *


class ModelCreature(Component):
    """
    Define our linkage model
    """

    ##### TODO 2: Model the Creature
    # Build the class(es) of objects that could utilize your built geometric object/combination classes. E.g., you could define
    # three instances of the cyclinder trunk class and link them together to be the "limb" class of your creature. 

    components = None
    contextParent = None

    def __init__(self, parent, position, display_obj=None):
        super().__init__(position, display_obj)
        self.components = []
        self.contextParent = parent

### BODY / FACE
        body = Component(Point((0.5, 1, 0)), DisplayableSphere(self.contextParent, 1, [1.0, 1.0, 1.0]))
        body.setDefaultColor(Ct.DARKGREEN)

        eye = Component(Point((0, 0.15, 0.65)), DisplayableSphere(self.contextParent, 1, [0.5, 0.5, 0.5]))
        eye.setDefaultColor(Ct.SILVER)
        pupil = Component(Point((0, 0, 0.35)), DisplayableSphere(self.contextParent, 1, [0.2, 0.2, 0.2]))
        pupil.setDefaultColor(Ct.BLUE)
        leftTooth = Component(Point((-0.11, -0.5, 0.7)), DisplayableCube(self.contextParent, 1, [0.2, 0.2, 0.2]))
        leftTooth.setDefaultColor(Ct.SILVER)
        rightTooth = Component(Point((0.11, -0.5, 0.7)), DisplayableCube(self.contextParent, 1, [0.2, 0.2, 0.2]))
        rightTooth.setDefaultColor(Ct.SILVER)

### LEFT LEG
        leftThigh = Component(Point((0.2, 0.1, 0)), DisplayableLegLimb(self.contextParent, 1, [0.5, 0.5, 0.5], ))
        leftThigh.setDefaultColor(Ct.DARKGREEN)
        leftCalf = Component(Point((0, -0.5, 0)), DisplayableLegLimb(self.contextParent, 1, [0.5, 0.5, 0.5], ))
        leftCalf.setDefaultColor(Ct.GREEN)
        lFoot = Component(Point((0, -0.6, 0.2)), DisplayableSphere(self.contextParent, 1, [0.1, 0.1, 0.25]))
        lFoot.setDefaultColor(Ct.NAVY)

### RIGHT LEG
        rightThigh = Component(Point((0.8, 0.1, 0)), DisplayableLegLimb(self.contextParent, 1, [0.5, 0.5, 0.5]))
        rightThigh.setDefaultColor(Ct.DARKGREEN)
        rightCalf = Component(Point((0, -0.5, 0)), DisplayableLegLimb(self.contextParent, 1, [0.5, 0.5, 0.5]))
        rightCalf.setDefaultColor(Ct.GREEN)
        rFoot = Component(Point((0, -0.6, 0.2)), DisplayableSphere(self.contextParent, 1, [0.1, 0.1, 0.25]))
        rFoot.setDefaultColor(Ct.NAVY)

### TOP LEFT ARM
        # #using single arm class
        # tlArm = Component(Point((0, 0, 0)), DisplayableArm(self.contextParent, 0.5, [1,1,1])) 
        # tlArm.setDefaultColor(Ct.BLUE)

        #using segmented arm classes
        tlBicep = Component(Point((0, 0.2, 0)), DisplayableBicepLimb(self.contextParent, 0.5, [1,1,1])) # [0.3, 0.3, 0.3]))
        tlBicep.setDefaultColor(Ct.DARKGREEN)
        tlForearm = Component(Point((0, 0, 0)), DisplayableLeftForearmLimb(self.contextParent, 0.5, [1,1,1]))
        tlForearm.setDefaultColor(Ct.DARKGREEN)

### TOP RIGHT ARM
        #using segmented arm classes
        trBicep = Component(Point((0, 0.2, 0)), DisplayableBicepLimb(self.contextParent, 0.5, [1,1,1])) # [0.3, 0.3, 0.3]))
        trBicep.setDefaultColor(Ct.DARKGREEN)
        trBicep.setDefaultAngle(180, body.vAxis)
        trForearm = Component(Point((0, 0, 0)), DisplayableRightForearmLimb(self.contextParent, 0.5, [1,1,1]))
        trForearm.setDefaultColor(Ct.DARKGREEN)

### BOTTOM LEFT ARM
        blBicep = Component(Point((0, -0.2, 0)), DisplayableBicepLimb(self.contextParent, 0.3, [1,1,1]))
        blBicep.setDefaultColor(Ct.GREEN)
        blForearm = Component(Point((0, 0.1, 0)), DisplayableLeftForearmLimb(self.contextParent, 0.3, [1,1,1]))
        blForearm.setDefaultColor(Ct.GREEN)

### BOTTOM RIGHT ARM
        brBicep = Component(Point((0, -0.2, 0)), DisplayableBicepLimb(self.contextParent, 0.3, [1,1,1])) # [0.3, 0.3, 0.3]))
        brBicep.setDefaultColor(Ct.GREEN)
        brBicep.setDefaultAngle(180, body.vAxis)
        brForearm = Component(Point((0, 0.1, 0)), DisplayableRightForearmLimb(self.contextParent, 0.3, [1,1,1]))
        brForearm.setDefaultColor(Ct.GREEN)


        self.addChild(body)
        body.addChild(eye)
        eye.addChild(pupil)
        body.addChild(leftTooth)
        body.addChild(rightTooth)

        self.addChild(leftThigh)
        leftThigh.addChild(leftCalf)
        leftCalf.addChild(lFoot)

        self.addChild(rightThigh)
        rightThigh.addChild(rightCalf)
        rightCalf.addChild(rFoot)

        body.addChild(tlBicep)
        tlBicep.addChild(tlForearm)
        body.addChild(blBicep)
        blBicep.addChild(blForearm)

        body.addChild(trBicep)
        trBicep.addChild(trForearm)
        body.addChild(brBicep)
        brBicep.addChild(brForearm)


        self.components = [body, eye, pupil, leftTooth, rightTooth, leftThigh, leftCalf, rightThigh, rightCalf, 
                            lFoot, rFoot,
                            tlBicep, tlForearm, blBicep, blForearm, trBicep, trForearm, brBicep, brForearm] # , mouth]

