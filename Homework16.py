a = input("Do you want to shutdown the program? (Y/N): ")
if a=="Y":
    import os
    os.system("shutdown /s /t 0")
elif a=="N":
    print("ok")
