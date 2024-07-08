import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class CSVPlot:
    def __init__(self, root):
        self.root = root

        # Set Matplotlib figure and canvas
        self.figure = Figure(figsize=(4, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, root)
        self.canvas.get_tk_widget().pack()
     
        # Scrollbars
        self.lk_scrollbar = tk.Scale(root, 
                                     from_=0,  # start value
                                     to=100,  # end value
                                     orient=tk.HORIZONTAL,  # horizental scrollbar
                                     label="Lk",  # label Lk
                                     command=self.update_plot)  # update the plot
        
        self.rl_scrollbar = tk.Scale(root, 
                                     from_=0, 
                                     to=100, 
                                     orient=tk.HORIZONTAL, 
                                     label="Rl", 
                                     command=self.update_plot)
        
        # Fill the available width of the root window
        self.lk_scrollbar.pack(fill=tk.X)  
        self.rl_scrollbar.pack(fill=tk.X)

        self.data = None
        self.unique_lk_values = []  # save unique Lk value
        self.unique_rl_values = []  # save unique Rl value
        self.max_x_value = 0
        self.max_y_value = 0

        # Load CSV from a fixed path
        self.csv_path = "./outputCSV/simulation_data.csv"
        self.load_csv()

    def load_csv(self):
        file_path = self.csv_path
        self.data = pd.read_csv(file_path)

        self.unique_lk_values = self.data['Lk'].unique()  # take the unique value of Lk
        self.unique_rl_values = self.data['Rl'].unique()
        self.max_x_value = self.data['x'].max()
        self.max_y_value = self.data['y'].max()

        self.lk_scrollbar.config(to=len(self.unique_lk_values) - 1)
        self.lk_scrollbar.set(0)

        self.rl_scrollbar.config(to=len(self.unique_rl_values) - 1)
        self.rl_scrollbar.set(0)

        self.update_plot()

    def update_plot(self, *args):
        if self.data is not None:
            lk_index = self.lk_scrollbar.get()
            rl_index = self.rl_scrollbar.get()
            selected_lk = self.unique_lk_values[lk_index]
            selected_rl = self.unique_rl_values[rl_index]

            filtered_data = self.data[(self.data['Lk'] == selected_lk) & (self.data['Rl'] == selected_rl)]
            self.ax.clear()

            self.ax.plot(filtered_data['x'], 
                         filtered_data['y'], 
                         label=f"Lk={selected_lk}, Rl={selected_rl}",
                         linewidth='0.75')

            self.ax.legend()
            
            self.ax.set_xlabel('Time (seconds)', fontsize='small')
            self.ax.set_ylabel('Voltage', fontsize='small')

            self.ax.set_xlim(0, self.max_x_value)
            self.ax.set_ylim(0, self.max_y_value)
            self.ax.tick_params(axis='both', which='major', labelsize=8)
            self.ax.xaxis.get_offset_text().set_fontsize(8) 

            self.ax.set_yticklabels([])
            self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVPlot(root)
    root.mainloop()
