
"""
#==============#
# LTspice Plot #
#==============#

import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os

file_path = os.path.join(os.path.dirname(__file__), 'snspd.raw')
l = ltspice.Ltspice(file_path)
l.parse()

time = l.get_time()
voltage = l.get_data('V(v_output)')

plt.plot(time, voltage)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()
"""

"""
#==============#
# LTspice Edit #
#==============#

LTC = SimRunner(output_folder='./output')
LTC.create_netlist('snspd.asc')
netlist = SpiceEditor('snspd.net')
netlist.set_component_value('V1', '1')

LTC.run(netlist)

netlist.reset_netlist()

print('Successful/Total Simulations: ' + str(LTC.okSim) + '/' + str(LTC.runno))

enter = input("Press enter to delete created files")
if enter == '':
    LTC.file_cleanup()
"""


"""
# LTspice parameters (in second)
init_delay = 10e-9
pulse_volt = 1  # ratio
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
"""

"""
# Parameters
lambda_rate = 0.001*(10e9)  # photon/s # lambda_rate_in_ns = 0.001  # photon/ns
t = 500e-9
dead_t = 20e-9

# Photon detection probability v.s. Voltage relationship
# P_di = 0.9  # 90%


a = 10
b = 1.5
v_bias = np.linspace(1, 2, 50)
P_di = 0.5 * (np.tanh(a * v_bias - b) + 1)

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


#==============#
# Diagram Plot #
#==============#

fig, ax = plt.subplots(1, 1, figsize=(10, 4))

ax.plot(steps, volt_signal, label='Voltage Signal', linewidth = 1)
mid = (volt_signal.max() + volt_signal.min()) / 2
ax.plot(photon_arrt, np.full_like(photon_arrt, mid), 'ro', markerfacecolor='none', label='Photon Arrivals', markersize=10)
ax.plot(detection_t, np.full_like(detection_t, mid), 'b.', label='Detected Photons', markersize=5)
ax.set_ylabel('VoltageRatio')
ax.set_xlabel('Time (s)')
ax.legend(loc='upper right', prop={'size': 10})

plt.savefig('snspd_simulation.png')

#===================#
# PWL File Generate #
#===================#

with open("snspd_data.txt", "w") as file:
    for time, volt in zip(steps, volt_signal):
        file.write(f"{time:.12e} {volt:.12e}\n")
"""