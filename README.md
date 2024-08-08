# SNSPD Simulation for Potential Use in Probabilistic Computing

## Stochastic MTJ for Probabilistic Computing

This idea is inspired from the stochastic MTJ (Magnetic Tunnelling Junction). The MTJ is characterised by its tunnelling magnetoresistance, which can be switched between high and low values by varying the angle between the magnetisation direction of the two ferromagnetic layers. The stochastic MTJ (S-MTJ) is an unstable MTJ with a free layer (broken) that has a relatively low energy barrier, allowing thermal noise to make it fluctuate between its stable states, one being parallel (P, low resistance) to the fixed layer and the other being anti-parallel (AP, high resistance). The input voltage can affect the stability of the free layer, thereby changing its resistance to vary the output voltage. This property can be used to build the stochastic neural networks for probabilistic computing.

## Superconducting Nanowire Single-PhotonDetectors (SNSPD)

The nanowire is cooled well below its superconducting critical temperature and biased with a DC current that is close to but less than the superconducting critical current of the nanowire. When a photon is detected (Cooper pairs are broken), a localised non-superconducting region (hotspot) with finite electrical resistance is formed. This produces a measurable voltage pulse that is approximately equal to the bias current multiplied by the load resistance. Then most of the bias current flowing through the load resistance, the hotspot cools and returns to the superconducting state. The time for the current to return to the nanowire is typically set by the inductive time constant (kinetic inductance of the nanowire divided by the impedance of the readout circuit) of the nanowire.

To investigate the potential of SNSPDs for probabilistic computing, simulating the electrical properties is necessary. Based on this, LTspice is used to study the electrical properties of SNSPDs. Then, by adding extra circuitry in LTspice and using Python for data processing and LTspice interaction, it is possible to achieve a phenomenon similar to that of stochastic MTJs.

## Reference
[1] W. A. Borders et al, "[Integer factorization using stochastic magnetic tunnel junctions](https://www-nature-com.libproxy1.nus.edu.sg/articles/s41586-019-1557-9)", Nature, 2019.

[2] Karl K Berggren et al, "[A superconducting nanowire can be modeled by using SPICE](https://iopscience.iop.org/article/10.1088/1361-6668/aab149)", Supercond. Sci. Technol. 31 055010, 2018.

[3] Andrew J. Kerman et al, "[Kinetic-inductance-limited reset time of superconducting nanowire photon counters](https://pubs-aip-org.libproxy1.nus.edu.sg/aip/apl/article/88/11/111116/331312/Kinetic-inductance-limited-reset-time-of)", Appl. Phys. Lett. 88, 111116, 2006.

## GitHub Repos Investigated

[1] [qnngroup/snspd-spice](https://github.com/qnngroup/snspd-spice)

[2] [DongHoonPark/ltspice_pytool](https://github.com/DongHoonPark/ltspice_pytool)

[3] [nunobrum/PyLTSpice](https://github.com/nunobrum/PyLTSpice)
