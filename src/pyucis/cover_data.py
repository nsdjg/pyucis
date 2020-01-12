'''
Created on Jan 11, 2020

@author: ballance
'''

class CoverData():
    
    def __init__(self,
                 type,
                 flags):
        self.type = type
        self.flags = flags
        # TODO: determine default data based on flags
        self.data = 0
        self.goal = 0 # if UCIS_HAS_GOAL
        self.weight = 0 # if UCIS_HAS_WEIGHT
        self.limit = 0 # if UCIS_HAS_LIMIT
        self.bitlen = 0 # if bytevector
                 
            