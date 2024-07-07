# Set the kinetic inductance
def SetInductance():
    Lk = str(input("Inductance value: "))
    return Lk

# Set the load resistance
def SetLoadResistance():
    Rl = str(input("Load R value: "))
    return Rl

def SetStartInductance():
    Lk_s = str(input("Start Inductance value: "))
    return Lk_s

def SetEndInductance():
    Lk_e = str(input("Start Inductance value: "))
    return Lk_e

def SetInductanceStep():
    Lk_step = str(input("Inductand step: "))
    return Lk_step

def SetStartLoadResistance():
    R_l_s = str(input("Start Load R value: "))
    return R_l_s

def SetEndLoadResistance():
    R_l_e = str(input("End Load R value: "))
    return R_l_e