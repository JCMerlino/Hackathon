import ctypes

user32 = ctypes.windll.user32
h = user32.GetSystemMetrics(0)
w = user32.GetSystemMetrics(1)
print(h + w)



if h >= w:
    print("Compuper")
else:
    print("Not a Compuper")
