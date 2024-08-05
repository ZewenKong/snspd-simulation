# SNSPDs-Simulation
## Process
### In practical

1. The superconducting nanowire maintained well below the critical temperature is direct current (DC) biased just below the critical current.
    
2. When a photon is absorbed by the nanowire a small resistive hotspot is created.
    
3. The supercurrent is forced to flow along the periphery of the hotspot. Since the nanowires are narrow, the local current density around the hotspot increases, exceeding the superconducting critical current density.

4. This in turn leads to the formation of a resistive barrier across the width of the nanowire.

5. Joule heating (via the DC bias) aids the growth of the resistive region along the axis of the nanowire until the current flow is blocked and the bias current is shunted by the external circuit.

6. This allows the resistive region to subside and the wire becomes fully superconducting again. The bias current through the nanowire returns to the original value.

### In LTspice

- A bias voltage source is in series with a 100 kOhm resistor (R_n).
- When a photon is detected, switch opening, the wire acquires a resistance R_n (RL circuit).
- The pulse is generated and will decay over time.
- When reaches I_ret (reset current), the decay is interrupted (dissipation is sufficient), and the switch is closed (R_n becomes very small and can be ignored, leaving only the resistance in the circuit).

## Issue I Met

1. **"Popen" issue** [[link](https://stackoverflow.com/questions/42572582/winerror-2-the-system-cannot-find-the-file-specified-when-trying-to-run-fortra)]

```
$ sheel=True
```

2. **Fail to generate .net file**\
Install the LTspice in the default path.

## References

[1] Karl K Berggren et al, "[A superconducting nanowire can be modeled by using SPICE](https://iopscience.iop.org/article/10.1088/1361-6668/aab149)", Supercond. Sci. Technol. 31 055010, 2018.

[2] Andrew J. Kerman et al, "[Kinetic-inductance-limited reset time of superconducting nanowire photon counters](https://pubs-aip-org.libproxy1.nus.edu.sg/aip/apl/article/88/11/111116/331312/Kinetic-inductance-limited-reset-time-of)", Appl. Phys. Lett. 88, 111116, 2006.

## GitHub Repos Investigated

[1] [qnngroup/snspd-spice](https://github.com/qnngroup/snspd-spice)

[2] [DongHoonPark/ltspice_pytool](https://github.com/DongHoonPark/ltspice_pytool)

[3] [nunobrum/PyLTSpice](https://github.com/nunobrum/PyLTSpice)
