from matplotlib import pyplot as plt
from PyLTSpice import SpiceEditor, SimRunner
from PyLTSpice import RawRead
from PyLTSpice import LTspice

import set_up
import spice_editor

def SpiceRunner(L_k, R_l, asc_path, net_path, output_path):

    """
    $ netlist.set_component_attribute('XU1', 'params', "Lind={L_k}")

    * the "set_component_attribute()" function in PyLTspice is not worked
    * edit the asc file directly to instead
    * should be executed before simulation

    """
    spice_editor.EditInductance(L_k)

    # LTspice simulator (default) path (recommend to be default)
    simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

    # Create a netlist of the circuit
    runner = SimRunner(output_folder=output_path, simulator=LTspice)
    runner.create_netlist(asc_path)
    netlist = SpiceEditor(net_path)

    """
    * Set the load resistance (Ohm)
    * Load resistance (R_l), input (Ohm), processing (Ohm)

    """
    netlist.set_component_value('R2', str(R_l))

    """
    * Inductance (L_k), input (H), processing (nH)

    PULSE(
        initial_voltage = 0
        peak_voltage = 1 uV
        initial delay = 10 ns
        time_rise = {tf} ns
        time_fall = {tr} ns
        time_on = 10 ps
        period = 30 ns
        number_of_pulse = 1
        )

    """

    init_delay = 10**(-9)  # unit: second
    tau_fall = (float(L_k)*(10**(-9))/(float(R_l) + (100*(10**3))))  # unit: second
    tau_rise = (float(L_k)*(10**(-9))/(float(R_l)))  # unit: second
    t_on = 10**(-12)  # unit: second

    period = tau_fall + tau_rise + t_on  # unit: second
    simulation_time = float(((period + init_delay))*10)  # unit: second

    #=====================#
    # Time (in nanosecond)#
    #=====================#

    tau_fall_in_ns = tau_fall*(10**9)
    tau_rise_in_ns = tau_rise*(10**9)
    period_in_ns = period*(10**9)
    simulation_time_in_ns = simulation_time*(10**9)

    # Set the bias current resource (pulse shape)
    element_model = "PULSE(0 1u 10n {tf}n {to}n 0 {p}n 1)".format(
        tf=tau_fall_in_ns, 
        to=tau_fall_in_ns + t_on,
        p=period_in_ns
        )
    netlist.set_element_model('I1', element_model)

    # Set the simulation time
    directive = ".tran 0 {}n 0 1p".format(simulation_time_in_ns)
    netlist.add_instructions(directive)

    raw, log = runner.run_now(netlist)
    print('Successful/Total Simulations: ' + str(runner.okSim) + '/' + str(runner.runno))
    raw_file = "./output/snspd_1.raw"

    LTR = RawRead(raw_file)
    x = LTR.get_trace('time')
    y = LTR.get_trace("V(v_output)")
    steps = LTR.get_steps()

    return x, y, steps