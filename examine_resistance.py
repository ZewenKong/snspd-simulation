
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import set_up
import spice_runner

from matplotlib import pyplot as plt
import pandas as pd
import spice_runner

def ExamineResistance(asc_path, net_path, output_path):

    # Define the Load Resistance Value
    Rl_start = 1  # Lk_start = set_up.SetStartInductance()
    Rl_end = 51  # Lk_end = set_up.SetEndInductance()
    Rl_step = 5  # Lk_step = set_up.SetInductanceStep()

    # Fix the Inductance Range
    Lk = 100

    data = []

    for Rl in range(Rl_start, Rl_end + Rl_step, Rl_step):
        x, y ,s = spice_runner.SpiceRunner(Lk, Rl, asc_path, net_path, output_path)

        for j in range(len(s)):
            x_wave = x.get_wave(j)
            y_wave = y.get_wave(j)
            plt.plot(x_wave, y_wave, label=f'L={Lk} H, R={Rl} Ω', linewidth=0.5)
            
            # Save the data to the DataFrame
            for xi, yi in zip(x_wave, y_wave):
                data.append({'Lk': Lk, 'Rl': Rl, 'x': xi, 'y': yi})

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(f'{output_path}/simulation_data.csv', index=False)

    plt.get_current_fig_manager().toolbar.zoom()
    plt.show()
