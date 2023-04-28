import platform
import struct
import sys

print("Python version:", platform.python_version())
print("Python bitness:", struct.calcsize("P") * 8, "bit")
print("Operating system:", platform.system())

print("Python path:")
for path in sys.path:
    print(path)