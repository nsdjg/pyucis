
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

'''
Created on Jan 11, 2020

@author: ballance
'''
from pyucis.obj import Obj
from pyucis.int_property import IntProperty
from pyucis.real_property import RealProperty
from pyucis.str_property import StrProperty
from pyucis.handle_property import HandleProperty
from pyucis.lib.libucis import get_lib

class LibObj(Obj):
    
    def __init__(self, db, obj):
        self.db = db
        self.obj = obj

    def getIntProperty(
            self, 
            coverindex : int,
            property : IntProperty
            )->int:
        raise UnimplError()
    
    def setIntProperty(
            self,
            coverindex : int,
            property : IntProperty,
            value : int):
        raise UnimplError()

    def getRealProperty(
            self,
            coverindex : int,
            property : RealProperty) -> float:
        raise UnimplError()
        
    def setRealProperty(
            self,
            coverindex : int,
            property : RealProperty,
            value : float):
        raise UnimplError()

    def getStringProperty(
            self,
            coverindex : int,
            property : StrProperty) -> str:
        raise UnimplError()
    
    def setStringProperty(
            self,
            coverindex : int,
            property : StrProperty,
            value : str):
        obj = self.db if self.obj is None else self.obj
        get_lib().ucis_SetStringProperty(self.db, obj, coverindex, property, value)
        
    def getHandleProperty(
            self,
            coverindex : int,
            property : HandleProperty) -> 'Scope':
        raise UnimplError()
    
    def setHandleProperty(
            self,
            coverindex : int,
            property : HandleProperty,
            value : 'Scope'):
        raise UnimplError()        