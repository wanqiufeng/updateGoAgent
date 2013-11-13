import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","requests","re","bs4","zipfile","os","shutil","configparser","math"]}

# GUI applications require a different base on Windows (the default is for a
# console application).

setup(  name = "GAUpdater",
        version = "0.1",
        description = "GoAgentUpdaterByVincent",
        options = {"build_exe": build_exe_options},
        executables = [Executable("updateGoAgent.py")])