from matplotlib import pyplot as plt
import pandas as pd
import set_up
import spice_run

def Examine(asc_path, net_path, output_path, csv_output_path):
    # Define the Inductance Range
    Lk_start = set_up.SetStartInductance()
    Lk_end = set_up.SetEndInductance()
    Lk_step = set_up.SetInductanceStep()

    # Define the Load Resistance Value
    Rl_start = set_up.SetStartLoadResistance()
    Rl_end = set_up.SetEndLoadResistance()
    Rl_step = set_up.SetLoadResistanceStep()

    data = []

    for Lk in range(int(Lk_start), int(Lk_end + Lk_step), int(Lk_step)):
        for Rl in range(int(Rl_start), int(Rl_end + Rl_step), int(Rl_step)):
            x, y, s = spice_run.SpiceRunner(Lk, Rl, asc_path, net_path, output_path)

            for i in range(len(s)):
                x_wave = x.get_wave(i)
                y_wave = y.get_wave(i)
                plt.plot(x_wave, y_wave, label=f'L={Lk} H, R={Rl} Ω', linewidth=0.5)

                for xi, yi in zip(x_wave, y_wave):
                    data.append({'Lk': Lk, 'Rl': Rl, 'x': xi, 'y': yi})

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(f'{csv_output_path}/simulation_data.csv', index=False)

    plt.get_current_fig_manager().toolbar.zoom()
    plt.show()