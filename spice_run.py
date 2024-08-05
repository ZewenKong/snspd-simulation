from PyLTSpice import SpiceEditor, SimRunner
from PyLTSpice import RawRead
from PyLTSpice import LTspice
import pulse_simulation

def SpiceRun(t, L_k, R_l, v, asc_path, net_path, output_path):

    """
    $ netlist.set_component_attribute('XU1', 'params', "Lind={Lk}")

    * the "set_component_attribute()" function in PyLTspice is not worked
    * edit the asc file directly to instead
    * should be executed before simulation
    
    # spice_edit.EditInductance(L_k)

    """
 
    # Simulate the photon arrival events in poisson distribution
    pulse_simulation.PulseSimulation(t, L_k, R_l, v)

    # Define the LTspice simulator path (recommend to be default)
    simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

    # Create a netlist of the circuit
    runner = SimRunner(output_folder=output_path, simulator=LTspice)
    runner.create_netlist(asc_path)
    netlist = SpiceEditor(net_path)

    """
    # Set the load resistance
    # netlist.set_component_value('R2', str(R_l))

    # Set the simulation time (transfer in ns)
    # t_ns = int(t * 1e9)
    # tran_instruction = ".tran 0 {}n 0 1p uic".format(t_ns)
    # netlist.add_instructions(tran_instruction)

    """
    
    if v <=1.0:
        voltage = 1.0001
    if v > 2.0:
        voltage = 2.0
    else:
        voltage = v

    netlist.set_component_value('V1', f'SINE(0 {voltage} 50MEG 0 0 0)')   # superconducting
    netlist.set_component_value('V2', f'SINE(0 {voltage} 50MEG 0 0 0)')   # normal
    netlist.set_component_value('V3', str(voltage))                       # snspd

    # hotspot resistance (the Ihs is fixed at 5 uA)
    Rhs = (((voltage/1e5)-5e-6)/5e-6)*50
    netlist.set_component_value('Rn', str(Rhs))
    
    # set variable parameters
    critical_current = ((voltage/1e5)-5e-6)*1.09    # sine wave critical current Ic
    threshold_voltage = ((voltage/1e5)-5e-6)*50     # threshold voltage of VCVS (comparator)
    netlist.set_parameters(Ic=critical_current, pvt=threshold_voltage, 
                           nvt=(-threshold_voltage), vi=voltage)

    # Run the netlist file
    raw, log = runner.run_now(netlist)
    print('Successful/Total Simulations: ' + str(runner.okSim) + '/' + str(runner.runno))
 
    # Read the raw file
    raw_file = "./output/snspd_1.raw"
    LTR = RawRead(raw_file)
    x = LTR.get_trace('time')

    y_sc = LTR.get_trace("V(superconducting)")   # superconducting voltage
    y_n = LTR.get_trace("V(normal)")             # normal state voltage
    y_mn = LTR.get_trace("V(modified-normal)")   # modified normal state voltage
    y_rp = LTR.get_trace("V(result-pulse)")      # voltage pulse (leaving superconducting)

    y_p = LTR.get_trace("V(photon)")             # snspd photon detection pulse
    y_sp = LTR.get_trace("V(square-pulse)")      # square pulse to change the voltage level
    v = LTR.get_trace("V(voltage-level)")       # voltage level (moire transistor)
    s = LTR.get_steps()

    return x, y_sc, y_n, y_mn, y_rp, y_p, y_sp, v, s