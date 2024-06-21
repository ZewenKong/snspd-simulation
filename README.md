# SNSPDs-Simulation

## References

[1] Karl K Berggren et al, "A superconducting nanowire can be modeled by using SPICE", Supercond. Sci. Technol. 31 055010, 2018.

## GitHub Repos Investigated

[1] [qnngroup/snspd-spice](https://github.com/qnngroup/snspd-spice)

[2] [DongHoonPark/ltspice_pytool](https://github.com/DongHoonPark/ltspice_pytool)

[3] [nunobrum/PyLTSpice](https://github.com/nunobrum/PyLTSpice)

## Issue I Met

[1] If have the "Popen" issue, call subprocess.Popen with "shell=True".
    (https://stackoverflow.com/questions/42572582/winerror-2-the-system-cannot-find-the-file-specified-when-trying-to-run-fortra)

[2] If cannot generate the .net file, use the default LTspice path
    (C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe)
