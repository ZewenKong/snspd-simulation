Version 4
SymbolType BLOCK
LINE Normal 0 48 0 -48
LINE Normal 32 -48 32 -32
LINE Normal 32 48 32 32
RECTANGLE Normal 48 32 16 -32
TEXT 64 0 Left 2 SC
SYMATTR ModelFile sc.lib
SYMATTR Prefix X
SYMATTR SpiceModel superconductor
SYMATTR Value Ic=10u Rsc=1f Rn=1500 Rct=10u
PIN 0 -48 NONE 8
PINATTR PinName gate
PINATTR SpiceOrder 1
PIN 0 48 NONE 8
PINATTR PinName gatereturn
PINATTR SpiceOrder 2
PIN 32 -48 NONE 8
PINATTR PinName n1
PINATTR SpiceOrder 3
PIN 32 48 NONE 8
PINATTR PinName n2
PINATTR SpiceOrder 4
