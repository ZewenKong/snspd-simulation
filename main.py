from matplotlib import pyplot as plt
from PyLTSpice import SpiceEditor, SimRunner
from PyLTSpice import RawRead
from PyLTSpice import AscEditor, LTspice

# Files import
import setUp
import simulation

# LTspice simulator path (default)
simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

# Create a netlist of the circuit
runner = SimRunner(output_folder='./output', simulator=LTspice)
runner.create_netlist('snspd.asc')

# Set the voltage and time
t = setUp.setTime()
voltage_value = setUp.setVoltage()

# Simulation the pulse voltage on the generated time point (Possion Distribution)
simulation.simulation(t, voltage_value)

# Edit the netlist
netlist = SpiceEditor('snspd.net')
netlist.set_component_value('V1', str(voltage_value))

"""
netlist.add_instructions(
        ".tran 0 500n 0 1p uic"
)
"""

print(t)
t_ns = int(t * 1e9)
print(t_ns)
tran_instruction = ".tran 0 {}n 0 1p uic".format(t_ns)
netlist.add_instructions(tran_instruction)

raw, log = runner.run_now(netlist)
print('Successful/Total Simulations: ' + str(runner.okSim) + '/' + str(runner.runno))

raw_file = "./output/snspd_1.raw"
LTR = RawRead(raw_file)

# print(LTR.get_trace_names())
# print(LTR.get_raw_property())

v = LTR.get_trace("V(v_output)")
x = LTR.get_trace('time')  # Gets the time axis
steps = LTR.get_steps()

for step in range(len(steps)):
    plt.plot(x.get_wave(step), v.get_wave(step), label=steps[step])

plt.show()
