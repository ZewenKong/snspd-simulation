import numpy as np
import os
import poisson_process
import random

def PulseSimulation (t, L_k, R_l, v):

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
    lambda_rate = 10e6
    arr_t, detection_p = poisson_process.PoissonProcess(t, lambda_rate, v)

    # Pulse time simulation
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
    
    init_delay = 10e-12 # 10 ns
    time_on = 10e-12    # 10 ps
    tau_fall = (float(L_k)*(10**(-9))/(float(R_l) + (1500))) 
    tau_rise = (float(L_k)*(10**(-9))/(float(R_l)))
    tau_dead = tau_fall + tau_rise + time_on
    safe_tau_dead = tau_dead*10

    detection_t = []
    ldtp = -np.inf  # ldtp - last detection time point (set to negative infinite)

    for atp in arr_t:  # atp - arrival time point
        if atp > init_delay and atp - ldtp > safe_tau_dead and random.random()<detection_p:
            detection_t.append(atp)
            ldtp = atp

    print("--------------------")
    print("Photon generates:\n", 
          ["{:.5e}".format(i) for i in arr_t])
    print("Detected Time Points [array]:\n", 
          ["{:.5e}".format(i) for i in detection_t])
    print("--------------------")

    pwl_data = []
    for dt in detection_t:
        pwl_data.append((dt, 0))
        pwl_data.append((dt + 10e-12, 1))
        pwl_data.append((dt + 10e-12 + time_on, 0))

    # TXT File Generate

    os.makedirs("outputPy", exist_ok=True)
    with open("outputPy/snspd_data.txt", "w") as file:
        for time, volt in pwl_data:
            file.write(f"{time:.12e} {volt:.12e}\n")
    return arr_t, detection_t