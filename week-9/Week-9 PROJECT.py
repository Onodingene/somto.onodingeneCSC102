#!/usr/bin/env python
# coding: utf-8

# In[ ]:


PROJECT 1

class federal_bursary:

    def __init__(self,name,origin):
        name = input("Enter your full name: ").upper()
        origin = input("Enter your state of origin ").upper()
        self.name = name
        self.origin = origin

    def bursary(self):
        names = ["MATTHEW AGBONROFO","EDITH AKANBI","MUSA YARADUA"],
        origins =["EDOCLAS","ABEOKUTA","KANO"]
        if self.name == "MATTHEW AGBONROFO" :
            import numpy as np
            array = np.array([["MATTHEW AGBONROFO","EDITH AKANBI","MUSA YARADUA"],
                              ["EDOCLAS","ABEOKUTA","KANO"],
                              [15000,25000,20000],
                              [20000,15000,3000]])
            column_index = 0
            column = array[:, column_index]
            print(column)
        elif self.name == "EDITH AKANBI":
            import numpy as np
            array = np.array([["MATTHEW AGBONROFO", "EDITH AKANBI", "MUSA YARADUA"],
                              ["EDOCLAS", "ABEOKUTA", "KANO"],
                              [15000, 25000, 20000],
                              [20000, 15000, 3000]])
            column_index = 1
            print(array[:, column_index])
        elif self.name == "MUSA YARADUA":
            import numpy as np
            array = np.array([["MATTHEW AGBONROFO", "EDITH AKANBI", "MUSA YARADUA"],
                              ["EDOCLAS", "ABEOKUTA", "KANO"],
                              [15000, 25000, 20000],
                              [20000, 15000, 30000]])
            column_index = 2
            print(array[:, column_index])
        else:
            print("ERROR!")

nigeria = federal_bursary('MATTHEW AGBONROFO','EDOCLAS')
nigeria.bursary()

