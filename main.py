from matplotlib import pyplot as plt
import spice_start
import spice_simulate

def main():
    # Path
    asc_path = './spiceModel/snspd.asc'
    net_path = './spiceModel/snspd.net'
    output_path = './output'

    # Parameters
    t = 500e-9      # simulation time
    L_k = 150       # kinetic inductance of SNSPD
    R_l = 50        # load resistance

    iteration_v = spice_start.SpiceStart(t, L_k, R_l, asc_path, net_path, output_path)

    iteration = 4
    for i in range(iteration):
        v_update = spice_simulate.SpiceSimulate(t, L_k, R_l, iteration_v, asc_path, net_path, output_path)
        iteration_v = v_update
    plt.show()

if __name__ == "__main__":
    main()
