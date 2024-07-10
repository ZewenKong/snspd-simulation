
from matplotlib import pyplot as plt
import pandas as pd
import spice_run

def ExamineResistance(asc_path, net_path, output_path, csv_output_path):

    Rl_start = 1  # Define the Load Resistance Value
    Rl_end = 201
    Rl_step = 50

    Lk = 100  # Fix the Inductance Range

    data = []

    for Rl in range(int(Rl_start), int(Rl_end + Rl_step), int(Rl_step)):
        x, y ,s = spice_run.SpiceRunner(Lk, Rl, asc_path, net_path, output_path)

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
    df.to_csv(f'{csv_output_path}/simulation_data.csv', index=False)

    plt.get_current_fig_manager().toolbar.zoom()
    plt.show()
