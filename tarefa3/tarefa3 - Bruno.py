# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:43:43 2019

@author: Bruno
"""

for a in range(1, 6):
  for e in [3,5,7]:
    print('{}^{} (mod {}) = {}'.format(a, e-1, e, a**(e-1) % e))