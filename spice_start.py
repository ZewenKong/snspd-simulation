from matplotlib import pyplot as plt
import spice_run
import os

"""
At beginning, the bias voltage is 1.5V,
the bias current is 15uA.

When a photon is detected,
the detect current (10 uA) is applied.

(The switch current (Isw) is 20 uA)

"""

init_v = 1.5

def SpiceStart(t, L_k, R_l, asc_path, net_path, output_path):

    image_dir = 'outputPy'
    os.makedirs(image_dir, exist_ok=True)
    
    x, y_sc, y_n, y_mn, y_rp, y_p, y_sp, v, s = spice_run.SpiceRun(t, L_k, R_l, init_v, 
                                                         asc_path, net_path, output_path)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 8))

    for step in range(len(s)):
        ax1.plot(x.get_wave(step), y_n.get_wave(step),
                 color='blue', linewidth=0.5)
        
        ax1.plot(x.get_wave(step), y_rp.get_wave(step),
                 color='red', linewidth=0.5)
    ax1.grid(True)

    for step in range(len(s)):
        ax2.plot(x.get_wave(step), y_p.get_wave(step))
    ax2.grid(True)

    for step in range(len(s)):
        ax3.plot(x.get_wave(step), y_sp.get_wave(step))
    ax3.grid(True)

    for step in range(len(s)):
        ax4.plot(x.get_wave(step), v.get_wave(step))
        volt = v.get_wave(step)
    ax4.grid(True)

    plt.tight_layout()
    output_dir = "outputPy"
    plt.savefig(os.path.join(output_dir, "start_plt.png"))
    plt.close(fig)

    volt_lvl = volt[-1]
    print(f"Initial run voltage level: {volt_lvl}")

    return volt_lvl