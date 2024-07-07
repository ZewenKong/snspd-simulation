from matplotlib import pyplot as plt
import set_up
import spice_runner

#==============#
# Working path #
#==============#

asc_path = './spiceModel/snspd.asc'
net_path = './spiceModel/snspd.net'
output_path = './output'

plt.figure()

num_simulation = 5

for i in range(num_simulation):
    L_k = set_up.SetInductance()
    R_l = set_up.SetLoadResistance()

    x, y, steps = spice_runner.SpiceRunner(L_k, R_l, asc_path, net_path, output_path)

    for step in range(len(steps)):
        plt.plot(x.get_wave(step), y.get_wave(step), label=f'Simulation {i+1}, Step {step+1}')

plt.legend()
plt.show()