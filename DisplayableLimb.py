'''
:author: Megan Mastrorilli
:version: 2021.1.1
'''
import os
import numpy as np
import string

try:
    import wx
    from wx import glcanvas
except ImportError:
    raise ImportError("Required dependency wxPython not present")

try:
    import OpenGL

    try:
        import OpenGL.GL as gl
        import OpenGL.GLU as glu
        import OpenGL.GLUT as glut  # this fails on OS X 11.x
    except ImportError:
        from ctypes import util

        orig_util_find_library = util.find_library


        def new_util_find_library(name):
            res = orig_util_find_library(name)
            if res:
                return res
            return '/System/Library/Frameworks/' + name + '.framework/' + name


        util.find_library = new_util_find_library
        import OpenGL.GL as gl
        import OpenGL.GLU as glu
        import OpenGL.GLUT as glut
except ImportError:
    raise ImportError("Required dependency PyOpenGL not present")

try:
    # From pip package "Pillow"
    from PIL import Image
except:
    print("Need to install PIL package. Pip package name is Pillow")
    raise ImportError

from Displayable import Displayable


class DisplayableLegLimb(Displayable):
    """
    Create a cylinder with two end-cap spheres
    """

    ##### TODO 1: Build Creature Parts
    # Build the class(es) of basic geometric objects/combination that could add up to be a part of your creature. 
    # E.g., you could write a cylinder class to be the trunk of your creature's limb. Or, you could 
    # write a two-sphere class to be the eye ball of your creature (one sphere for the eye ball and one sphere for the lens/iris).
    # The needed GLU functions for cylinder and sphere are mentioned in README.md

    callListHandle = 0  # long int. override the one in Displayable
    qd = None  # Quadric
    scale = None
    edgeLength = 1
    _bufferData = None

    def __init__(self, parent, edgeLength, scale=None):
        super().__init__(parent)
        parent.context.SetCurrent(parent)
        self.edgeLength = edgeLength
        if scale is None:
            scale = [1, 1, 1]
        self.scale = scale

    ##### BONUS 1: Texture your creature
    # Requirement: 1. Build the texture mapping that binds texture image to your objects. 

    def draw(self):
        gl.glCallList(self.callListHandle)

    def initialize(self):
        self.callListHandle = gl.glGenLists(1)
        self.qd = glu.gluNewQuadric()

        gl.glNewList(self.callListHandle, gl.GL_COMPILE)

        # master push - applies to all limb components
        gl.glPushMatrix() 
        gl.glScale(*self.scale)
        gl.glRotate(90, 1,0,0)

        glu.gluSphere(self.qd, 0.3, 30, 30)
        glu.gluCylinder(self.qd, 0.3, 0.3, 1, 30, 30)

        # translate limb other end cap sphere
        gl.glPushMatrix() 
        gl.glTranslate(0, 0, self.edgeLength)
        glu.gluSphere(self.qd, 0.3, 30, 30)
        gl.glPopMatrix()

        gl.glPopMatrix() # master pop
        gl.glEndList()


# class DisplayableArm(Displayable):
#     """
#     Create a cylinder with two end-cap spheres
#     """

#     callListHandle = 0  # long int. override the one in Displayable
#     qd = None  # Quadric
#     scale = None
#     edgeLength = 1
#     _bufferData = None

#     def __init__(self, parent, edgeLength, scale=None):
#         super().__init__(parent)
#         parent.context.SetCurrent(parent)
#         self.edgeLength = edgeLength
#         if scale is None:
#             scale = [1, 1, 1]
#         self.scale = scale

#     def draw(self):
#         gl.glCallList(self.callListHandle)

#     def initialize(self):
#         self.callListHandle = gl.glGenLists(1)
#         self.qd = glu.gluNewQuadric()

#         gl.glNewList(self.callListHandle, gl.GL_COMPILE)

#         # Bicep transform push
#         gl.glPushMatrix() 
#         gl.glScale(*self.scale)
#         gl.glTranslate(-1, 0.3, 0)
#         gl.glRotate(30, 0,0,1)
#         gl.glRotate(-90, 0,1,0)

#         glu.gluSphere(self.qd, 0.1, 30, 30)
#         glu.gluCylinder(self.qd, 0.1, 0.1, self.edgeLength, 30, 30)

#         gl.glPushMatrix() 
#         gl.glTranslate(0, 0, self.edgeLength)
#         glu.gluSphere(self.qd, 0.1, 30, 30)
#         gl.glPopMatrix()

#         gl.glPopMatrix() # Bicep transform pop

#         # Forearm transform pop
#         gl.glPushMatrix() 
#         gl.glScale(*self.scale)
#         gl.glTranslate(-(1+self.edgeLength), 0, 0)
#         gl.glRotate(70, 0,0,1)
#         gl.glRotate(-90, 0,1,0)

#         glu.gluSphere(self.qd, 0.1, 30, 30)
#         glu.gluCylinder(self.qd, 0.1, 0.1, self.edgeLength, 30, 30)

#         gl.glPushMatrix() 
#         gl.glTranslate(0, 0, self.edgeLength)
#         glu.gluSphere(self.qd, 0.1, 30, 30)
#         gl.glPopMatrix()

#         gl.glPopMatrix() # Forearm tranform pop
#         gl.glEndList()


class DisplayableBicepLimb(Displayable):
    """
    Create a cylinder with two end-cap spheres
    """

    callListHandle = 0  # long int. override the one in Displayable
    qd = None  # Quadric
    scale = None
    edgeLength = 1
    _bufferData = None

    def __init__(self, parent, edgeLength, scale=None): 
        super().__init__(parent)
        parent.context.SetCurrent(parent)
        self.edgeLength = edgeLength
        if scale is None:
            scale = [1, 1, 1]
        self.scale = scale

    def draw(self):
        gl.glCallList(self.callListHandle)

    def initialize(self):
        self.callListHandle = gl.glGenLists(1)
        self.qd = glu.gluNewQuadric()

        gl.glNewList(self.callListHandle, gl.GL_COMPILE)

        # master push - applies to all limb components
        gl.glPushMatrix() 
        gl.glScale(*self.scale)
        gl.glTranslate(-1, 0, 0)
        gl.glRotate(30, 0,0,1)
        gl.glRotate(-90, 0,1,0)

        glu.gluSphere(self.qd, 0.1, 30, 30)
        glu.gluCylinder(self.qd, 0.1, 0.1, self.edgeLength, 30, 30)

        # translate limb other end cap sphere
        gl.glPushMatrix() 
        gl.glTranslate(0, 0, self.edgeLength)
        glu.gluSphere(self.qd, 0.1, 30, 30)
        gl.glPopMatrix()

        gl.glPopMatrix() # master pop
        gl.glEndList()

class DisplayableLeftForearmLimb(Displayable):
    """
    Create a cylinder with two end-cap spheres
    """

    callListHandle = 0  # long int. override the one in Displayable
    qd = None  # Quadric
    scale = None
    edgeLength = 1
    _bufferData = None

    def __init__(self, parent, edgeLength, scale=None):
        super().__init__(parent)
        parent.context.SetCurrent(parent)
        self.edgeLength = edgeLength
        if scale is None:
            scale = [1, 1, 1]
        self.scale = scale

    def draw(self):
        gl.glCallList(self.callListHandle)

    def initialize(self):
        self.callListHandle = gl.glGenLists(1)
        self.qd = glu.gluNewQuadric()

        gl.glNewList(self.callListHandle, gl.GL_COMPILE)

        # master push - applies to all limb components
        gl.glPushMatrix() 
        gl.glScale(*self.scale)
        gl.glTranslate(-(1+self.edgeLength), -0.3, 0)
        gl.glRotate(70, 0,0,1)
        gl.glRotate(-90, 0,1,0)

        glu.gluSphere(self.qd, 0.1, 30, 30)
        glu.gluCylinder(self.qd, 0.1, 0.1, self.edgeLength, 30, 30)

        # translate limb other end cap sphere
        gl.glPushMatrix() 
        gl.glTranslate(0, 0, self.edgeLength)
        glu.gluSphere(self.qd, 0.1, 30, 30)
        gl.glPopMatrix()

        gl.glPopMatrix() # master pop
        gl.glEndList()


class DisplayableRightForearmLimb(Displayable):
    """
    Create a cylinder with two end-cap spheres
    """

    callListHandle = 0  # long int. override the one in Displayable
    qd = None  # Quadric
    scale = None
    edgeLength = 1
    _bufferData = None

    def __init__(self, parent, edgeLength, scale=None):
        super().__init__(parent)
        parent.context.SetCurrent(parent)
        self.edgeLength = edgeLength
        if scale is None:
            scale = [1, 1, 1]
        self.scale = scale

    def draw(self):
        gl.glCallList(self.callListHandle)

    def initialize(self):
        self.callListHandle = gl.glGenLists(1)
        self.qd = glu.gluNewQuadric()

        gl.glNewList(self.callListHandle, gl.GL_COMPILE)

        # master push - applies to all limb components
        gl.glPushMatrix() 
        gl.glScale(*self.scale)
        gl.glTranslate(-(1+self.edgeLength), -0.3, 0)
        gl.glRotate(-110, 0,0,1)
        gl.glRotate(90, 0,1,0)

        glu.gluSphere(self.qd, 0.1, 30, 30)
        glu.gluCylinder(self.qd, 0.1, 0.1, self.edgeLength, 30, 30)

        # translate limb other end cap sphere
        gl.glPushMatrix() 
        gl.glTranslate(0, 0, self.edgeLength)
        glu.gluSphere(self.qd, 0.1, 30, 30)
        gl.glPopMatrix()

        gl.glPopMatrix() # master pop
        gl.glEndList()
