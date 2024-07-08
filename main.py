from matplotlib import pyplot as plt
import pandas as pd
import tkinter as tk

from csv_plot import CSVPlot

import set_up
import spice_run
import examine
import examine_inductance
import examine_resistance

def main():
    asc_path = './spiceModel/snspd.asc'
    net_path = './spiceModel/snspd.net'
    output_path = './output'
    csv_output_path = './outputCSV'

    plt.figure()
    # examine_inductance.ExamineInductance(asc_path, net_path, output_path, csv_output_path)
    # examine_resistance.ExamineResistance(asc_path, net_path, output_path, csv_output_path)
    # examine.Examine(asc_path, net_path, output_path, csv_output_path)

    root = tk.Tk()
    app = CSVPlot(root)
    root.mainloop()

if __name__ == "__main__":
    main()