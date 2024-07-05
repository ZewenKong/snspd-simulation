import numpy as np
import matplotlib.pyplot as plt
import os

def Simulation (t, v, L_k, R_l):

    #==================#
    # Pulse simulation #
    #==================#

    init_delay = 10e-9
    tau_fall = (float(L_k)*10e-9)/(float(R_l) + 100e3)
    tau_rise = (float(L_k)*10e-9)/(float(R_l))
    tau_dead = tau_fall + tau_rise
    t_on = 10e-12

    pdt_1 = 5.0e-8   # pre defined time
    pdt_2 = pdt_1 + tau_fall
    pdt_3 = pdt_2 + t_on
    
    pdp = [(pdt_1, 0), (pdt_2, 1), (pdt_3, 0)]  # pre defined pulse

    os.makedirs("outputPy", exist_ok=True)
    with open("outputPy/snspd_data.txt", "w") as file:
        for t, v in pdp: file.write(f"{t} {v}\n")
