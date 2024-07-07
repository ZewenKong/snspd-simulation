from matplotlib import pyplot as plt
import pandas as pd
import set_up
import spice_runner
import examine_inductance
import examine_resistance

#=========================#
# Define the Working Path #
#=========================#

asc_path = './spiceModel/snspd.asc'
net_path = './spiceModel/snspd.net'
output_path = './output'

plt.figure()

# examine_inductance.ExamineInductance(asc_path, net_path, output_path)
examine_resistance.ExamineResistance(asc_path, net_path, output_path)

