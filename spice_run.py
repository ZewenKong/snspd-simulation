from matplotlib import pyplot as plt
from PyLTSpice import SpiceEditor, SimRunner
from PyLTSpice import RawRead
from PyLTSpice import LTspice

import spice_edit

def SpiceRunner(Lk, Rl, asc_path, net_path, output_path):

    """
    $ netlist.set_component_attribute('XU1', 'params', "Lind={Lk}")

    * the "set_component_attribute()" function in PyLTspice is not worked
    * edit the asc file directly to instead
    * should be executed before simulation

    """
    spice_edit.EditInductance(Lk)

    """
    * Define the LTspice simulator path (recommend to be default)

    """
    simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

    # Create a netlist of the circuit
    runner = SimRunner(output_folder=output_path, simulator=LTspice)
    runner.create_netlist(asc_path)
    netlist = SpiceEditor(net_path)

    #=================#
    # Time parameters #
    #=================#

    """
    * Inductance (Lk), input (H), processing (nH)

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
    tau_fall = (float(Lk)*(10**(-9))/(float(Rl) + (100*(10**3))))  # unit: second
    tau_rise = (float(Lk)*(10**(-9))/(float(Rl)))  # unit: second
    t_on = 10**(-12)  # unit: second

    period = tau_fall + tau_rise + t_on  # unit: second
    simulation_time = float(((period + init_delay))*10)  # unit: second

    # Time (in nanosecond)
    tau_fall_in_ns = tau_fall*(10**9)
    tau_rise_in_ns = tau_rise*(10**9)
    period_in_ns = period*(10**9)
    simulation_time_in_ns = simulation_time*(10**9)

    #================#
    # Set parameters #
    #================#

    # Se the load resistance
    netlist.set_component_value('R2', str(Rl))

    # Set the bias current resource (pulse shape)
    element_model = "PULSE(0 1u 10n {t1}n {t2}n 0 {p}n 1)".format(
        t1=tau_fall_in_ns, 
        t2=tau_fall_in_ns + t_on,
        p=period_in_ns
        )
    netlist.set_element_model('I1', element_model)

    # Set the simulation time
    directive = ".tran 0 {}n 0 1p".format(simulation_time_in_ns)
    netlist.add_instructions(directive)

    #==============#
    # Run and Read #
    #==============#

    # Run the netlist file
    raw, log = runner.run_now(netlist)
    print('Successful/Total Simulations: ' + str(runner.okSim) + '/' + str(runner.runno))
    
    # Read the raw file
    raw_file = "./output/snspd_1.raw"
    LTR = RawRead(raw_file)
    x = LTR.get_trace('time')
    y = LTR.get_trace("V(v_output)")
    s = LTR.get_steps()  # step

    return x, y, s