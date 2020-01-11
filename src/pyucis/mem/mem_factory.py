
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
Created on Jan 5, 2020

@author: ballance
'''
from pyucis import ucis
from pyucis.mem.mem_ucis import MemUCIS

class MemFactory():
    
    
    @staticmethod
    def create() -> ucis:
        """
        Creates a new in-memory database. 
        """
        return MemUCIS()
    
    
    @staticmethod
    def clone(db : ucis):
        """Clones an existing database and creates a new in-memory database"""
        pass

        
    
        
        