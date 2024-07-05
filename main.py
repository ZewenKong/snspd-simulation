from matplotlib import pyplot as plt
from PyLTSpice import SpiceEditor, SimRunner
from PyLTSpice import RawRead
from PyLTSpice import AscEditor, LTspice

import set_up
import simulation
import inductance_editor

"""
* Before run, please check the LTspice PWL file path
"""

t = 100 # 100 ns (pre-defined)
v = 2   # 2 V (pre-defined)
L_k = set_up.SetInductance()
R_l = set_up.SetLoadResistance()
"""
$ netlist.set_component_attribute('XU1', 'params', "Lind={L_k}")

* the "set_component_attribute()" function in PyLTspice is not worked
* edit the asc file directly to instead
* should be executed before simulation
"""
inductance_editor.EditInductance(L_k)

# LTspice simulator (default) path (recommend to be default)
simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

# Create a netlist of the circuit
runner = SimRunner(output_folder='./output', simulator=LTspice)
runner.create_netlist('./spiceModel/snspd.asc')
netlist = SpiceEditor('./spiceModel/snspd.net')
# Generate detection time points
simulation.Simulation(t, v, L_k, R_l)

# Set the load resistance (R2 in electrical model) (Ohm)
netlist.set_component_value('R2', str(R_l))

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
