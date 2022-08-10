import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter", 'requests', 'os']}

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

setup(
    name="Climas",
    version="0.1",
    description="Este programa retorna alguns dados climaticos dos lugares propostos",
    options={"build_exe": build_exe_options},
    executables=[Executable("../python_climas.py", base=base)]
)

#  python .\setup.py build
