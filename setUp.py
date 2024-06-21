def setTime():
    time = int(input("Simulation time: "))
    t = time*1e-9
    return t

def setVoltage():
    try:
        volt_value = float(input("Voltage value: "))
        if 1 <= volt_value <= 2:
            return volt_value
        else:
            print("Value out of range.")
            return setVoltage()
    except ValueError:
        print("Invalid input.")
        return setVoltage()