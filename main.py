from matplotlib import pyplot as plt
from PyLTSpice import SpiceEditor, SimRunner
from PyLTSpice import RawRead
from PyLTSpice import AscEditor, LTspice

import ltspice

import setUp
import simulation
import ascEditor
import os

# Set the variables
t = setUp.SetTime()
v = setUp.SetBiasVoltage()
L_k = setUp.SetInductance()
R_l = setUp.SetLoadResistance()

# Edit the .asc file (Set the kinetic inductance)
# netlist.set_component_attribute('XU1', 'params', "Lind={L_k}")
ascEditor.ascEditor(L_k)

# LTspice simulator path
simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

# Create a netlist of the circuit
runner = SimRunner(output_folder='./output', simulator=LTspice)
runner.create_netlist('snspd.asc')
netlist = SpiceEditor('snspd.net')

# Simulation process
simulation.simulation(t, v, L_k, R_l)

# Set the bias voltage and the load resistance
netlist.set_component_value('V1', str(v))
netlist.set_component_value('R2', str(R_l))

# Set the simulation time (transfer in ns)
t_ns = int(t * 1e9)
tran_instruction = ".tran 0 {}n 0 1p uic".format(t_ns)
netlist.add_instructions(tran_instruction)

raw, log = runner.run_now(netlist)

op_raw_file= "./output/snspd_1.op.raw"

print('Successful/Total Simulations: ' + str(runner.okSim) + '/' + str(runner.runno))
raw_file = "./output/snspd_1.raw"

LTR = RawRead(raw_file)
x = LTR.get_trace('time')
y = LTR.get_trace("V(v_output)")

steps = LTR.get_steps()
for step in range(len(steps)):
    plt.plot(x.get_wave(step), y.get_wave(step), label=steps[step])

plt.show()
