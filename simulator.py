import numpy as np
import matplotlib.pyplot as plt

#===============================#
# Possion statistics simulation #
#===============================#

# Parameters
lambda_rate = 0.001*(10e9)  # photon/s # lambda_rate_in_ns = 0.001  # photon/ns
t = 500e-9
P_di = 0.9  # 90%
dead_t = 20e-9

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

#==================#
# Pulse simulation #
#==================#

# LTspice parameters (in second)
init_delay = 10e-9
pulse_volt = 10e-6  # pulse height (1uV)
time_rise = 10e-12
time_fall = 10e-12
time_on = 10e-12
period = 20e-9

steps = np.linspace(0, t, int(t / 10e-12))
volt_signal = np.zeros_like(steps)  # Create an array of zero

for dt in detection_t:
    # Insert the detected photon time coordinates in the "steps" array
    start_index = np.searchsorted(steps, dt)
    end_index = np.searchsorted(steps, dt + period)

    # If the end_index higher than the length of the "steps" array, set it to be the len(steps)
    if end_index > len(steps): end_index = len(steps)

    # Get pulse time period in array
    pulse_time = steps[start_index:end_index] - dt
    pulse = np.zeros_like(pulse_time)

    pulse += np.where(pulse_time < time_rise, pulse_volt,  # Rising edge
             np.where(pulse_time < time_rise + time_on, pulse_volt,  # Constant high
             np.where(pulse_time < time_rise + time_on + time_fall, pulse_volt * (1 - (pulse_time - (time_rise + time_on)) / time_fall), 0)))  # Falling edge
    
    volt_signal[start_index:end_index] += pulse

#==============#
# Diagram Plot #
#==============#

fig, ax = plt.subplots(1, 1, figsize=(10, 4))

ax.plot(steps, volt_signal, label='Voltage Signal', linewidth = 1)
mid = (volt_signal.max() + volt_signal.min()) / 2
ax.plot(photon_arrt, np.full_like(photon_arrt, mid), 'ro', markerfacecolor='none', label='Photon Arrivals', markersize=10)
ax.plot(detection_t, np.full_like(detection_t, mid), 'b.', label='Detected Photons', markersize=5)
ax.set_ylabel('Voltage (V)')
ax.set_xlabel('Time (s)')
ax.legend(loc='upper right', prop={'size': 10})

plt.savefig('snspd_simulation.png')

#===================#
# PWL File Generate #
#===================#

with open("snspd_data.txt", "w") as file:
    for time, volt in zip(steps, volt_signal):
        file.write(f"{time:.12e} {volt:.12e}\n")