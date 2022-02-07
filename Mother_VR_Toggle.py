path="D:\SteamLibrary\steamapps\common\Alien Isolation\mothervr.json"
enabled='        \"VRRuntime\": \"Oculus\"\n'
disabled='        \"VRRuntime\": \"None\"\n'

def main():
    a=readjson()
    if ln[a] == disabled:
        b=input("VR is disabled. Do you want to enable it? y/n ")
        if b == "y" or b == "Y":
            ln[a]=enabled
            writejson()
            print ("Enabled")
        else:
            print ("VR was not enabled...exiting")
    elif ln[a] == enabled:
        b=input("VR is enabled. Do you want to disable it? y/n ")
        if b == "y" or b == "Y":
            ln[a]=disabled
            writejson()
            print ("Disabled")
        else:
            print ("VR was not enabled...exiting")


def readjson():
    global ln
    f=open(path,"r")
    ln=f.readlines()
    f.close()
    try:
        g=ln.index(enabled)
    except ValueError:
        g=ln.index(disabled)
    return (g)

def writejson():
    f=open(path,"w")
    for item in ln:
        f.write(item)
    f.close()

if __name__=="__main__":
    main()
    
