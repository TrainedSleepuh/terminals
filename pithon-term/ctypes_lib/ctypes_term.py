import ctypes

clibrary = ctypes.CDLL("/home/puta/CRAZY/terminals/pithon-term/ctypes_lib/clibrary.so")
clibrary.display(b"Billy Gay", 69)