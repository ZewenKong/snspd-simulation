
#==================#
# Variables Set Up #
#==================#

# Set the simulation time
def SetTime():
    time = float(input("Simulation time: "))
    t = time*1e-9
    return t

# Set the bias voltage source
def SetBiasVoltage():
    try:
        v = float(input("Voltage value (1 ~ 2 V): "))
        if 1 <= v <= 2:
            return v
        else:
            print("Value out of range.")
            return SetBiasVoltage()
    except ValueError:
        print("Invalid input.")
        return SetBiasVoltage()

# Set the kinetic inductance
def SetInductance():
    L_k = str(input("Inductance value: "))
    return L_k

# Set the load resistance
def SetLoadResistance():
    R_l = str(input("Load R value: "))
    return R_l
