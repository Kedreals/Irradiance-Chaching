"""
Created on Sat Dec 30 2017

@author: kedreals
"""

import numpy as np
from BSDF import *

class Intersection :
    def __init__(self, pos = np.array([0.,0.,0.]), normal = np.array([0.,1.0,0.])):
        self.pos = pos
        self.n = normal
        self.color = np.array([1., 1., 1.])
        self.ell = 0.0
        self.m_BSDF = DiffuseBSDF

    def BSDF(self, lightIn, lightOut, n):
        return np.min([1., np.max([0., self.m_BSDF(lightIn, lightOut, n)])])