import numpy as np
import matplotlib.pyplot as plt
import os

def simulation (t, v):
 
    #===============================#
    # Possion statistics simulation #
    #===============================#

    """
    # Parameters #

    lambda_rate (float): Photon arrival rate (photons/s).
    t (float): Total time duration for the simulation (s).  # t = 500e-9
    dead_t (float): Dead time after each detection (s).

    a (constant): Parameter 'a' in the tanh relationship.
    b (costant): Parameter 'b' in the tanh relationship.

    v (range from 1 to 2): Bias voltages.  # v = np.linspace(1, 2, 50)

    detection_t (list): List of detection times.
    """

    lambda_rate = 0.001*(10e9)
    dead_t = 20e-9

    a = 10
    b = 1.5
    P_di = 0.5 * (np.tanh(a * (v - b)) + 1)

    expected_no_photon = np.random.poisson(lambda_rate*t)
    photon_arrt = np.sort(np.random.uniform(0, t, expected_no_photon))

    detection_t = []
    last_detection_t = -np.inf

    for arrt in photon_arrt:
        if np.random.rand() < P_di:
            # Make sure no detection in the last detection dead time
            if arrt - last_detection_t > dead_t:
                detection_t.append(arrt)
                last_detection_t = arrt

    print(P_di)
    print(detection_t)

    #==================#
    # Pulse simulation #
    #==================#

    """
    # LTspice Parameters #

    Vinitial: 初始电压
    Von: 高电压
    Tdelay: 延迟 （初始电压到高电压的初始延迟）
    time_rise: 上升的时间
    time_fall: 下降的时间
    time_on: 高电压持续时间
    period: 总时长
    """

    init_delay = 10e-9
    pulse_volt = 1  # ratio
    time_rise = 10e-12
    time_fall = 10e-12
    time_on = 10e-12
    period = 20e-9

    # Create time steps
    steps = np.linspace(0, t, int(t / 10e-12))

    # Create an array of zeros
    volt_signal = np.zeros_like(steps)

    for dt in detection_t:
        # Insert the detected photon time coordinates in the "steps" array
        start_index = np.searchsorted(steps, dt)
        end_index = np.searchsorted(steps, dt + period)

        # If the end_index is higher than the length of the "steps" array, set it to be the len(steps)
        if end_index > len(steps):
            end_index = len(steps)

        # Get pulse time period in array
        pulse_time = steps[start_index:end_index] - dt
        pulse = np.zeros_like(pulse_time)

        pulse += np.where(pulse_time < time_rise, pulse_volt,  # Rising edge
                 np.where(pulse_time < time_rise + time_on, pulse_volt,  # Constant high
                 np.where(pulse_time < time_rise + time_on + time_fall, pulse_volt * (1 - (pulse_time - (time_rise + time_on)) / time_fall), 0)))  # Falling edge

        volt_signal[start_index:end_index] += pulse

    #===============#
    # File Generate #
    #===============#

    fig, ax = plt.subplots(1, 1, figsize=(10, 4))

    ax.plot(steps, volt_signal, label='Voltage Signal', linewidth = 1)
    mid = (volt_signal.max() + volt_signal.min()) / 2
    ax.plot(photon_arrt, np.full_like(photon_arrt, mid), 'go', markerfacecolor='none', label='Photon Arrivals', markersize=10)
    ax.plot(detection_t, np.full_like(detection_t, mid), 'r.', label='Detected Photons', markersize=5)
    ax.set_ylabel('VoltageRatio')
    ax.set_xlabel('Time (s)')
    ax.legend(loc='upper right', prop={'size': 10})

    # Save the plot
    os.makedirs("outputPy", exist_ok=True)
    plt.savefig('outputPy/snspd_simulation.png')
    plt.show()

    with open("outputPy/snspd_data.txt", "w") as file:
        for time, volt in zip(steps, volt_signal):
            file.write(f"{time:.12e} {volt:.12e}\n")

    return P_di, photon_arrt, detection_t, steps, volt_signal