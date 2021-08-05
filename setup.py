# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:56:12 2021

@author: lakna
"""
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os","nltk"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "similarity_engine",
    version = "0.1",
    description = "My app for CityGrows!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("common_fields_script.py", base=None)]
)

