import numpy as np
import matplotlib.pyplot as plt
import os

import poissonProcess

def simulation (t, v, L_k, R_l):

    """
    Structure: Meander structure with a 50% fill factor.

    Temperature (T): Measurement temperature set at 2 K (Tc = 9 ~ 10 K).

    Pulse repetition rate (lambda_rate): 10 MHz, the photon arrival rate (photons/s).

    Simulation time (t): Total time duration for the simulation (s).

    Dead time (tau_dead): Dead time after each detection (s).

    a (constant): Parameter 'a' in the tanh relationship.
    b (costant): Parameter 'b' in the tanh relationship.

    Bias voltage (v): Bias voltage source (V).
    Resistance (R_n): Variable resistance (in LTspice is set to 100 kOhm).
    Load Resistance (R_l): Load resistance (Ohm).
    Kinetice inductance (L_k): Kinetic inductance of the SNSPD (nH).

    """

    # Photons will arrive following a Poisson distribution
    # return a list of detection time points
    arr_t = poissonProcess.PoissonProcess(t, lambda_rate = 0.001*(10e9))

    #=============================#
    # Detection events simulation #
    #=============================#

    # Detection probability of SNSPD based on the bias voltage
    # v_bias vs. P_d follows a tanh relationship
    a, b = 10, 1.5
    P_d = 0.5 * (np.tanh(a * (v - b)) + 1)

    #==================#
    # Pulse simulation #
    #==================#

    """
    # LTspice Parameters #

    Vinitial: Initial voltage
    Von: Peak voltage / On voltage
    Tdelay: Delay at the beginning
    time_rise: Rise time (duration taken to reach peak)
    time_fall: Fall time
    time_on: Duration to maintain peak voltage
    period: Total period for one pulse
    tau_fall = L_k/(R_l + 1000)
    tau_rise = L_k/R_l

    """

    init_delay = 10e-9
    tau_fall = (float(L_k)*10e-9)/(float(R_l) + 100e3)
    tau_rise = (float(L_k)*10e-9)/(float(R_l))
    tau_dead = tau_fall + tau_rise

    detection_t = []
    ldtp = -np.inf  # ldt - last detection time point

    for atp in arr_t:  # atp - arrival time point
        if atp < init_delay: continue
        if np.random.rand() < P_d:
            if atp - ldtp > tau_dead:
                detection_t.append(atp)
                ldtp = atp

    print("------------------------------")
    print("Detection Probability: ",P_d*100,"%")
    print("------------------------------")
    print("Photon generates:\n", ["{:.5e}".format(i) for i in arr_t])
    print("------------------------------")
    print("Detected Time Points [array]:\n", ["{:.5e}".format(i) for i in detection_t])

    pwl_data = []

    pulse = (v/100e3)*float(R_l)
    rise_t = 10e-12
    on_t = 10e-12

    for dt in detection_t:
        pwl_data.append((dt, 0))
        pwl_data.append((dt + rise_t, pulse))
        pwl_data.append((dt + rise_t + on_t, 0))

    #===================#
    # TXT File Generate #
    #===================#

    os.makedirs("outputPy", exist_ok=True)
    with open("outputPy/snspd_data.txt", "w") as file:
        for time, volt in pwl_data:
            file.write(f"{time:.12e} {volt:.12e}\n")

    return P_d, arr_t, detection_t