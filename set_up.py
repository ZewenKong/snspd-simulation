# Set the kinetic inductance
def SetInductance():
    Lk = str(input("Inductance value: "))
    return Lk

# Set the load resistance
def SetLoadResistance():
    Rl = str(input("Load R value: "))
    return Rl

# -------------------------

def SetStartInductance():
    Lk_s = float(input("Start Inductance value: "))
    return Lk_s

def SetEndInductance():
    Lk_e = float(input("End Inductance value: "))
    return Lk_e

def SetInductanceStep():
    Lk_step = float(input("Inductand step: "))
    return Lk_step

def SetStartLoadResistance():
    Rl_s = float(input("Start Load R value: "))
    return Rl_s

def SetEndLoadResistance():
    Rl_e = float(input("End Load R value: "))
    return Rl_e

def SetLoadResistanceStep():
    Rl_step = float(input("Load R step: "))
    return Rl_step