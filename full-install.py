#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
  full-install.py
  Main Script  
    - installation-prerequis.py
    - configuration-https.py
    - configuration-glpi.py
"""
# Import of the required modules
import subprocess
try:
  #Launch first script 
  subprocess.run(["python3","installation-prerequis.py"])
  #Launch second 
  subprocess.run(["python3","configuration-https.py"])
  #Launch third script
  subprocess.run(["python3","configuration-glpi.py"])
  
except Exception as e:
  raise e
