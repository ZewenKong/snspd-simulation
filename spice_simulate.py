from matplotlib import pyplot as plt
import spice_run
import os

def SpiceSimulate(t, L_k, R_l, v, asc_path, net_path, output_path):

    image_dir = 'outputPy'
    os.makedirs(image_dir, exist_ok=True)
    
    """
    At beginning, the bias voltage is 1.5V,
    the bias current is 15uA.

    When a photon is detected,
    the detect current (10 uA) is applied.

    (The switch current (Isw) is 20 uA)

    """
    print(f"Run SpiceSimulate.py | voltage value:{v}")

    x, y_sc, y_n, y_mn, y_rp, y_p, y_sp, v, s = spice_run.SpiceRun(t, L_k, R_l, v, asc_path, net_path, output_path)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 8))

    for step in range(len(s)):
        # normal
        ax1.plot(x.get_wave(step), y_n.get_wave(step),
                color='blue', linewidth=0.5)
        # result pulse
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

    volt_level = volt[-1]

    return volt_level
