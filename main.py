from matplotlib import pyplot as plt
from PyLTSpice import SpiceEditor, SimRunner
from PyLTSpice import RawRead
from PyLTSpice import AscEditor, LTspice

import set_up
import simulation
import inductance_editor
import os

# Set the variables
t = set_up.SetTime()
v = set_up.SetBiasVoltage()
L_k = set_up.SetInductance()
R_l = set_up.SetLoadResistance()
"""
$ netlist.set_component_attribute('XU1', 'params', "Lind={L_k}")

* the "set_component_attribute()" function in PyLTspice is not worked
* edit the asc file directly to instead
* should be executed before simulation
"""
inductance_editor.ascEditor(L_k)

# LTspice simulator (default) path (recommend to be default)
simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

# Create a netlist of the circuit
runner = SimRunner(output_folder='./output', simulator=LTspice)
runner.create_netlist('./spiceModel/snspd.asc')
netlist = SpiceEditor('./spiceModel/snspd.net')

# Simulate
simulation.simulation(t, v, L_k, R_l)

# Set the bias voltage and the load resistance
netlist.set_component_value('V1', str(v))
netlist.set_component_value('R2', str(R_l))

# Set the simulation time (transfer in ns)
t_ns = int(t * 1e9)
tran_instruction = ".tran 0 {}n 0 1p uic".format(t_ns)
netlist.add_instructions(tran_instruction)

raw, log = runner.run_now(netlist)
print('Successful/Total Simulations: ' + str(runner.okSim) + '/' + str(runner.runno))
raw_file = "./output/snspd_1.raw"

LTR = RawRead(raw_file)
x = LTR.get_trace('time')
y = LTR.get_trace("V(v_output)")

steps = LTR.get_steps()
for step in range(len(steps)):
    plt.plot(x.get_wave(step), y.get_wave(step), label=steps[step])

plt.show()
