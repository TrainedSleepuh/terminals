import os
from termcolor import colored

p_table = colored('''				PERIODIC TABLE
  
| H  |                                                                               | He |
| Li | Be |                                                 | B  | C  | N  | O  | F  | Ne |
| Na | Mg |                                                 | Al | Si | P  | S  | Cl | Ar |
| K  | Ca | Sc | Ti | V  | Cr | Mn | Fe | Co | Ni | Cu | Zn | Ga | Ge | As | Se | Br | Kr |
| Rb | Sr | Y  | Zr | Nb | Mo | Tc | Ru | Rh | Pd | Ag | Cd | ln | Sn | Sb | Te | l  | Xe |
| Cs | Ba |    | Hf | Ta | W  | Re | Os | lr | Pt | Au | Hg | Tl | Pb | Bi | Po | At | Rn |
| Fr | Ra      | Rf | Db | Sg | Bh | Hs | Mt | Ds | Rg | Cn | Nh | Fl | Mc | Lv | Ts | Og |
               | La | Ce | Pr | Nd | Pm | Sm | Eu | Gd | Tb | Dy | Ho | Er | Tm | Yb | Lu |
               | Ac | Th | Pa | U  | Np | Pu | Am | Cm | Bk | Cf | Es | Fm | Md | No | Lr |

''', 'magenta')
print(p_table)

p_table_input = input("PICK A SYMBOL <>--->")

if p_table_input == 'H':
	print('''
Hydrogen
1
Nonmetal

Atomic Mass	1.0080 u
Standard State	gas
Electron Configuration	1s1
Oxidation States	+1, -1
Electronegativity (Pauling Scale)	2.2
Atomic Radius (van der Waals)	120 pm
Ionization Energy	13.598 eV
Electron Affinity	0.754 eV
Melting Point	13.81 K
Boiling Point	20.28 K
Density	0.00008988 g/cm³
Year Discovered	1766
''')

if p_table_input == 'He':
	print('''
Helium
2
Noble Gas
	
Atomic Mass	4.00260 u
Standard State	gas
Electron Configuration	1s2
Oxidation States	0
Atomic Radius (van der Waals)	140 pm
Ionization Energy	24.587 eV
Melting Point	0.95 K
Boiling Point	4.22 K
Density	0.0001785 g/cm³
Year Discovered	1868
''')

if p_table_input == 'Li':
	print('''
Lithium
3
Alkali Metal
	
Atomic Mass	7.0 u
Standard State	solid
Electron Configuration	[He]2s1
Oxidation States	+1
Electronegativity (Pauling Scale)	0.98
Atomic Radius (van der Waals)	182 pm
Ionization Energy	5.392 eV
Electron Affinity	0.618 eV
Melting Point	453.65 K
Boiling Point	1615 K
Density	0.534 g/cm³
Year Discovered	1817
''')

if p_table_input == 'Be':
	print('''
Beryllium
4
Alkaline Earth Metal
	
Atomic Mass	9.012183 u
Standard State	solid
Electron Configuration	[He]2s2
Oxidation States	+2
Electronegativity (Pauling Scale)	1.57
Atomic Radius (van der Waals)	153 pm
Ionization Energy	9.323 eV
Melting Point	1560 K
Boiling Point	2744 K
Density	1.85 g/cm³
Year Discovered	1798
''')

if p_table_input == 'B':
	print('''
Boron
5
Metalloid
	
Atomic Mass	10.81 u
Standard State	solid
Electron Configuration	[He]2s22p1
Oxidation States	+3
Electronegativity (Pauling Scale)	2.04
Atomic Radius (van der Waals)	192 pm
Ionization Energy	8.298 eV
Electron Affinity	0.277 eV
Melting Point	2348 K
Boiling Point	4273 K
Density	2.37 g/cm³
Year Discovered	1808	
''')

if p_table_input == 'C':
	print('''
Carbon
6
Nonmetal
	
Atomic Mass	12.011 u
Standard State	solid
Electron Configuration	[He]2s22p2
Oxidation States	+4, +2, -4
Electronegativity (Pauling Scale)	2.55
Atomic Radius (van der Waals)	170 pm
Ionization Energy	11.260 eV
Electron Affinity	1.263 eV
Melting Point	3823 K
Boiling Point	4098 K
Density	2.2670 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'N':
	print('''
Nitrogen
7
Nonmetal
	
Atomic Mass	14.007 u
Standard State	gas
Electron Configuration	[He]2s22p3
Oxidation States	+5, +4, +3, +2, +1, -1, -2, -3
Electronegativity (Pauling Scale)	3.04
Atomic Radius (van der Waals)	155 pm
Ionization Energy	14.534 eV
Melting Point	63.15 K
Boiling Point	77.36 K
Density	0.0012506 g/cm³
Year Discovered	1772
''')

if p_table_input == 'O':
	print('''
Oxygen
8
Nonmetal
	
Atomic Mass	15.999 u
Standard State	gas
Electron Configuration	[He]2s22p4
Oxidation States	-2
Electronegativity (Pauling Scale)	3.44
Atomic Radius (van der Waals)	152 pm
Ionization Energy	13.618 eV
Electron Affinity	1.461 eV
Melting Point	54.36 K
Boiling Point	90.2 K
Density	0.001429 g/cm³
Year Discovered	1774
''')

if p_table_input == 'F':
	print('''
Fluorine
9
Halogen
	
Atomic Mass	18.99840316 u
Standard State	gas
Electron Configuration	[He]2s22p5
Oxidation States	-1
Electronegativity (Pauling Scale)	3.98
Atomic Radius (van der Waals)	135 pm
Ionization Energy	17.423 eV
Electron Affinity	3.339 eV
Melting Point	53.53 K
Boiling Point	85.03 K
Density	0.001696 g/cm³
Year Discovered	1670
''')

if p_table_input == 'Ne':
	print('''
Neon
10
Noble Gas
	
Atomic Mass	20.180 u
Standard State	gas
Electron Configuration	[He]2s22p6
Oxidation States	0
Atomic Radius (van der Waals)	154 pm
Ionization Energy	21.565 eV
Melting Point	24.56 K
Boiling Point	27.07 K
Density	0.0008999 g/cm³
Year Discovered	1898
''')

if p_table_input == 'Na':
	print('''
Sodium
11
Alkali Metal
	
Atomic Mass	22.9897693 u
Standard State	solid
Electron Configuration	[Ne]3s1
Oxidation States	+1
Electronegativity (Pauling Scale)	0.93
Atomic Radius (van der Waals)	227 pm
Ionization Energy	5.139 eV
Electron Affinity	0.548 eV
Melting Point	370.95 K
Boiling Point	1156 K
Density	0.97 g/cm³
Year Discovered	1807
''')

if p_table_input == 'Mg':
	print('''
Magnesium
12
Alkaline Earth Metal
	
Atomic Mass	24.305 u
Standard State	solid
Electron Configuration	[Ne]3s2
Oxidation States	+2
Electronegativity (Pauling Scale)	1.31
Atomic Radius (van der Waals)	173 pm
Ionization Energy	7.646 eV
Melting Point	923 K
Boiling Point	1363 K
Density	1.74 g/cm³
Year Discovered	1808
''')

if p_table_input == 'Al':
	print('''
Aluminum
13
Post-transition Metal
	
Atomic Mass	26.981538 u
Standard State	solid
Electron Configuration	[Ne]3s23p1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.61
Atomic Radius (van der Waals)	184 pm
Ionization Energy	5.986 eV
Electron Affinity	0.441 eV
Melting Point	933.437 K
Boiling Point	2792 K
Density	2.70 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Si':
	print('''
Silicon
14
Metalloid
	
Atomic Mass	28.085 u
Standard State	solid
Electron Configuration	[Ne]3s23p2
Oxidation States	+4, +2, -4
Electronegativity (Pauling Scale)	1.9
Atomic Radius (van der Waals)	210 pm
Ionization Energy	8.152 eV
Electron Affinity	1.385 eV
Melting Point	1687 K
Boiling Point	3538 K
Density	2.3296 g/cm³
Year Discovered	1854
''')

if p_table_input == 'P':
	print('''
Phosphorus
15
Nonmetal
	
Atomic Mass	30.97376200 u
Standard State	solid
Electron Configuration	[Ne]3s23p3
Oxidation States	+5, +3, -3
Electronegativity (Pauling Scale)	2.19
Atomic Radius (van der Waals)	180 pm
Ionization Energy	10.487 eV
Electron Affinity	0.746 eV
Melting Point	317.3 K
Boiling Point	553.65 K
Density	1.82 g/cm³
Year Discovered	1669
''')

if p_table_input == 'S':
	print('''
Sulfur
16
Nonmetal
	
Atomic Mass	32.07 u
Standard State	solid
Electron Configuration	[Ne]3s23p4
Oxidation States	+6, +4, -2
Electronegativity (Pauling Scale)	2.58
Atomic Radius (van der Waals)	180 pm
Ionization Energy	10.360 eV
Electron Affinity	2.077 eV
Melting Point	388.36 K
Boiling Point	717.75 K
Density	2.067 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Cl':
	print('''
Chlorine
17
Halogen
	
Atomic Mass	35.45 u
Standard State	gas
Electron Configuration	[Ne]3s23p5
Oxidation States	+7, +5, +1, -1
Electronegativity (Pauling Scale)	3.16
Atomic Radius (van der Waals)	175 pm
Ionization Energy	12.968 eV
Electron Affinity	3.617 eV
Melting Point	171.65 K
Boiling Point	239.11 K
Density	0.003214 g/cm³
Year Discovered	1774
''')

if p_table_input == 'Ar':
	print('''
Argon
18
Noble Gas
	
Atomic Mass	39.9 u
Standard State	gas
Electron Configuration	[Ne]3s23p6
Oxidation States	0
Atomic Radius (van der Waals)	188 pm
Ionization Energy	15.760 eV
Melting Point	83.8 K
Boiling Point	87.3 K
Density	0.0017837 g/cm³
Year Discovered	1894
''')

if p_table_input == 'K':
	print('''
Potassium
19
Alkali Metal
	
Atomic Mass	39.0983 u
Standard State	solid
Electron Configuration	[Ar]4s1
Oxidation States	+1
Electronegativity (Pauling Scale)	0.82
Atomic Radius (van der Waals)	275 pm
Ionization Energy	4.341 eV
Electron Affinity	0.501 eV
Melting Point	336.53 K
Boiling Point	1032 K
Density	0.89 g/cm³
Year Discovered	1807
''')

if p_table_input == 'Ca':
	print('''
Calcium
20
Alkaline Earth Metal
	
Atomic Mass	40.08 u
Standard State	solid
Electron Configuration	[Ar]4s2
Oxidation States	+2
Electronegativity (Pauling Scale)	1
Atomic Radius (van der Waals)	231 pm
Ionization Energy	6.113 eV
Melting Point	1115 K
Boiling Point	1757 K
Density	1.54 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Sc':
	print('''
Scandium
21
Transition Metal
	
Atomic Mass	44.95591 u
Standard State	solid
Electron Configuration	[Ar]4s23d1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.36
Atomic Radius (van der Waals)	211 pm
Ionization Energy	6.561 eV
Electron Affinity	0.188 eV
Melting Point	1814 K
Boiling Point	3109 K
Density	2.99 g/cm³
Year Discovered	1879
''')

if p_table_input == 'Ti':
	print('''
Titanium
22
Transition Metal
	
Atomic Mass	47.867 u
Standard State	solid
Electron Configuration	[Ar]4s23d2
Oxidation States	+4, +3, +2
Electronegativity (Pauling Scale)	1.54
Atomic Radius (van der Waals)	187 pm
Ionization Energy	6.828 eV
Electron Affinity	0.079 eV
Melting Point	1941 K
Boiling Point	3560 K
Density	4.5 g/cm³
Year Discovered	1791
''')

if p_table_input == 'V':
	print('''
Vanadium
23
Transition Metal
	
Atomic Mass	50.9415 u
Standard State	solid
Electron Configuration	[Ar]4s23d3
Oxidation States	+5, +4, +3, +2
Electronegativity (Pauling Scale)	1.63
Atomic Radius (van der Waals)	179 pm
Ionization Energy	6.746 eV
Electron Affinity	0.525 eV
Melting Point	2183 K
Boiling Point	3680 K
Density	6.0 g/cm³
Year Discovered	1801
''')

if p_table_input == 'Cr':
	print('''
Chromium
24
Transition Metal
	
Atomic Mass	51.996 u
Standard State	solid
Electron Configuration	[Ar]3d54s1
Oxidation States	+6, +3, +2
Electronegativity (Pauling Scale)	1.66
Atomic Radius (van der Waals)	189 pm
Ionization Energy	6.767 eV
Electron Affinity	0.666 eV
Melting Point	2180 K
Boiling Point	2944 K
Density	7.15 g/cm³
Year Discovered	1797
''')

if p_table_input == 'Mn':
	print('''
Manganese
25
Transition Metal
	
Atomic Mass	54.93804 u
Standard State	solid
Electron Configuration	[Ar]4s23d5
Oxidation States	+7, +4, +3, +2
Electronegativity (Pauling Scale)	1.55
Atomic Radius (van der Waals)	197 pm
Ionization Energy	7.434 eV
Melting Point	1519 K
Boiling Point	2334 K
Density	7.3 g/cm³
Year Discovered	1774
''')

if p_table_input == 'Fe':
	print('''
Iron
26
Transition Metal
	
Atomic Mass	55.84 u
Standard State	solid
Electron Configuration	[Ar]4s23d6
Oxidation States	+3, +2
Electronegativity (Pauling Scale)	1.83
Atomic Radius (van der Waals)	194 pm
Ionization Energy	7.902 eV
Electron Affinity	0.163 eV
Melting Point	1811 K
Boiling Point	3134 K
Density	7.874 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Co':
	print('''
Cobalt
27
Transition Metal
	
Atomic Mass	58.93319 u
Standard State	solid
Electron Configuration	[Ar]4s23d7
Oxidation States	+3, +2
Electronegativity (Pauling Scale)	1.88
Atomic Radius (van der Waals)	192 pm
Ionization Energy	7.881 eV
Electron Affinity	0.661 eV
Melting Point	1768 K
Boiling Point	3200 K
Density	8.86 g/cm³
Year Discovered	1735
''')

if p_table_input == 'Ni':
	print('''
Nickel
28
Transition Metal
	
Atomic Mass	58.693 u
Standard State	solid
Electron Configuration	[Ar]4s23d8
Oxidation States	+3, +2
Electronegativity (Pauling Scale)	1.91
Atomic Radius (van der Waals)	163 pm
Ionization Energy	7.640 eV
Electron Affinity	1.156 eV
Melting Point	1728 K
Boiling Point	3186 K
Density	8.912 g/cm³
Year Discovered	1751
''')

if p_table_input == 'Cu':
	print('''
Copper
29
Transition Metal	

Atomic Mass	63.55 u
Standard State	solid
Electron Configuration	[Ar]4s13d10
Oxidation States	+2, +1
Electronegativity (Pauling Scale)	1.9
Atomic Radius (van der Waals)	140 pm
Ionization Energy	7.726 eV
Electron Affinity	1.228 eV
Melting Point	1357.77 K
Boiling Point	2835 K
Density	8.933 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Zn':
	print('''
Zinc
30
Transition Metal	

Atomic Mass	65.4 u
Standard State	solid
Electron Configuration	[Ar]4s23d10
Oxidation States	+2
Electronegativity (Pauling Scale)	1.65
Atomic Radius (van der Waals)	139 pm
Ionization Energy	9.394 eV
Melting Point	692.68 K
Boiling Point	1180 K
Density	7.134 g/cm³
Year Discovered	1746
''')

if p_table_input == 'Ga':
	print('''
Gallium
31
Post-transition Metal
	
Atomic Mass	69.723 u
Standard State	solid
Electron Configuration	[Ar]4s23d104p1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.81
Atomic Radius (van der Waals)	187 pm
Ionization Energy	5.999 eV
Electron Affinity	0.3 eV
Melting Point	302.91 K
Boiling Point	2477 K
Density	5.91 g/cm³
Year Discovered	1875
''')

if p_table_input == 'Ge':
	print('''
Germanium
32
Metalloid
	
Atomic Mass	72.63 u
Standard State	solid
Electron Configuration	[Ar]4s23d104p2
Oxidation States	+4, +2
Electronegativity (Pauling Scale)	2.01
Atomic Radius (van der Waals)	211 pm
Ionization Energy	7.900 eV
Electron Affinity	1.35 eV
Melting Point	1211.4 K
Boiling Point	3106 K
Density	5.323 g/cm³
Year Discovered	1886
''')

if p_table_input == 'As':
	print('''
Arsenic
33
Metalloid
	
Atomic Mass	74.92159 u
Standard State	solid
Electron Configuration	[Ar]4s23d104p3
Oxidation States	+5, +3, -3
Electronegativity (Pauling Scale)	2.18
Atomic Radius (van der Waals)	185 pm
Ionization Energy	9.815 eV
Electron Affinity	0.81 eV
Melting Point	1090 K
Boiling Point	887 K
Density	5.776 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Se':
	print('''
Selenium
34
Nonmetal
	
Atomic Mass	78.97 u
Standard State	solid
Electron Configuration	[Ar]4s23d104p4
Oxidation States	+6, +4, -2
Electronegativity (Pauling Scale)	2.55
Atomic Radius (van der Waals)	190 pm
Ionization Energy	9.752 eV
Electron Affinity	2.021 eV
Melting Point	493.65 K
Boiling Point	958 K
Density	4.809 g/cm³
Year Discovered	1817
''')

if p_table_input == 'Br':
	print('''
Bromine
35
Halogen	

Atomic Mass	79.90 u
Standard State	liquid
Electron Configuration	[Ar]4s23d104p5
Oxidation States	+5, +1, -1
Electronegativity (Pauling Scale)	2.96
Atomic Radius (van der Waals)	183 pm
Ionization Energy	11.814 eV
Electron Affinity	3.365 eV
Melting Point	265.95 K
Boiling Point	331.95 K
Density	3.11 g/cm³
Year Discovered	1826
''')

if p_table_input == 'Kr':
	print('''
Krypton
36
Noble Gas	

Atomic Mass	83.80 u
Standard State	gas
Electron Configuration	[Ar]4s23d104p6
Oxidation States	0
Electronegativity (Pauling Scale)	3
Atomic Radius (van der Waals)	202 pm
Ionization Energy	14.000 eV
Melting Point	115.79 K
Boiling Point	119.93 K
Density	0.003733 g/cm³
Year Discovered	1898
''')

if p_table_input == 'Rb':
	print('''
Rubidium
37
Alkali Metal
	
Atomic Mass	85.468 u
Standard State	solid
Electron Configuration	[Kr]5s1
Oxidation States	+1
Electronegativity (Pauling Scale)	0.82
Atomic Radius (van der Waals)	303 pm
Ionization Energy	4.177 eV
Electron Affinity	0.468 eV
Melting Point	312.46 K
Boiling Point	961 K
Density	1.53 g/cm³
Year Discovered	1861
''')

if p_table_input == 'Sr':
	print('''
Strontium
38
Alkaline Earth Metal
	
Atomic Mass	87.62 u
Standard State	solid
Electron Configuration	[Kr]5s2
Oxidation States	+2
Electronegativity (Pauling Scale)	0.95
Atomic Radius (van der Waals)	249 pm
Ionization Energy	5.695 eV
Melting Point	1050 K
Boiling Point	1655 K
Density	2.64 g/cm³
Year Discovered	1790
''')

if p_table_input == 'Y':
	print('''
Yttrium
39
Transition Metal
	
Atomic Mass	88.90584 u
Standard State	solid
Electron Configuration	[Kr]5s24d1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.22
Atomic Radius (van der Waals)	219 pm
Ionization Energy	6.217 eV
Electron Affinity	0.307 eV
Melting Point	1795 K
Boiling Point	3618 K
Density	4.47 g/cm³
Year Discovered	1794
''')

if p_table_input == 'Zr':
	print('''
Zirconium
40
Transition Metal
	
Atomic Mass	91.22 u
Standard State	solid
Electron Configuration	[Kr]5s24d2
Oxidation States	+4
Electronegativity (Pauling Scale)	1.33
Atomic Radius (van der Waals)	186 pm
Ionization Energy	6.634 eV
Electron Affinity	0.426 eV
Melting Point	2128 K
Boiling Point	4682 K
Density	6.52 g/cm³
Year Discovered	1789
''')

if p_table_input == 'Nb':
	print('''
Niobium
41
Transition Metal
	
Atomic Mass	92.90637 u
Standard State	solid
Electron Configuration	[Kr]5s14d4
Oxidation States	+5, +3
Electronegativity (Pauling Scale)	1.6
Atomic Radius (van der Waals)	207 pm
Ionization Energy	6.759 eV
Electron Affinity	0.893 eV
Melting Point	2750 K
Boiling Point	5017 K
Density	8.57 g/cm³
Year Discovered	1801
''')

if p_table_input == 'Mo':
	print('''
Molybdenum
42
Transition Metal
	
Atomic Mass	95.95 u
Standard State	solid
Electron Configuration	[Kr]5s14d5
Oxidation States	+6
Electronegativity (Pauling Scale)	2.16
Atomic Radius (van der Waals)	209 pm
Ionization Energy	7.092 eV
Electron Affinity	0.746 eV
Melting Point	2896 K
Boiling Point	4912 K
Density	10.2 g/cm³
Year Discovered	1778
''')

if p_table_input == 'Tc':
	print('''
Technetium
43
Transition Metal
	
Atomic Mass	96.90636 u
Standard State	solid
Electron Configuration	[Kr]5s24d5
Oxidation States	+7, +6, +4
Electronegativity (Pauling Scale)	1.9
Atomic Radius (van der Waals)	209 pm
Ionization Energy	7.28 eV
Electron Affinity	0.55 eV
Melting Point	2430 K
Boiling Point	4538 K
Density	11 g/cm³
Year Discovered	1937
''')

if p_table_input == 'Ru':
	print('''
Ruthenium
44
Transition Metal
	
Atomic Mass	101.1 u
Standard State	solid
Electron Configuration	[Kr]5s14d7
Oxidation States	+3
Electronegativity (Pauling Scale)	2.2
Atomic Radius (van der Waals)	207 pm
Ionization Energy	7.361 eV
Electron Affinity	1.05 eV
Melting Point	2607 K
Boiling Point	4423 K
Density	12.1 g/cm³
Year Discovered	1827
''')

if p_table_input == 'Rh':
	print('''
Rhodium
45
Transition Metal
	
Atomic Mass	102.9055 u
Standard State	solid
Electron Configuration	[Kr]5s14d8
Oxidation States	+3
Electronegativity (Pauling Scale)	2.28
Atomic Radius (van der Waals)	195 pm
Ionization Energy	7.459 eV
Electron Affinity	1.137 eV
Melting Point	2237 K
Boiling Point	3968 K
Density	12.4 g/cm³
Year Discovered	1803
''')

if p_table_input == 'Pd':
	print('''
Palladium
46
Transition Metal
	
Atomic Mass	106.42 u
Standard State	solid
Electron Configuration	[Kr]4d10
Oxidation States	+3, +2
Electronegativity (Pauling Scale)	2.2
Atomic Radius (van der Waals)	202 pm
Ionization Energy	8.337 eV
Electron Affinity	0.557 eV
Melting Point	1828.05 K
Boiling Point	3236 K
Density	12.0 g/cm³
Year Discovered	1803
''')

if p_table_input == 'Ag':
	print('''
Silver
47
Transition Metal
	
Atomic Mass	107.868 u
Standard State	solid
Electron Configuration	[Kr]5s14d10
Oxidation States	+1
Electronegativity (Pauling Scale)	1.93
Atomic Radius (van der Waals)	172 pm
Ionization Energy	7.576 eV
Electron Affinity	1.302 eV
Melting Point	1234.93 K
Boiling Point	2435 K
Density	10.501 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Cd':
	print('''
Cadmium
48
Transition Metal
	
Atomic Mass	112.41 u
Standard State	solid
Electron Configuration	[Kr]5s24d10
Oxidation States	+2
Electronegativity (Pauling Scale)	1.69
Atomic Radius (van der Waals)	158 pm
Ionization Energy	8.994 eV
Melting Point	594.22 K
Boiling Point	1040 K
Density	8.69 g/cm³
Year Discovered	1817
''')

if p_table_input == 'ln':
	print('''
Indium
49
Post-transition Metal
	
Atomic Mass	114.818 u
Standard State	solid
Electron Configuration	[Kr]5s24d105p1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.78
Atomic Radius (van der Waals)	193 pm
Ionization Energy	5.786 eV
Electron Affinity	0.3 eV
Melting Point	429.75 K
Boiling Point	2345 K
Density	7.31 g/cm³
Year Discovered	1863
''')

if p_table_input == 'Sn':
	print('''
Tin
50
Post-transition Metal
	
Atomic Mass	118.71 u
Standard State	solid
Electron Configuration	[Kr]5s24d105p2
Oxidation States	+4, +2
Electronegativity (Pauling Scale)	1.96
Atomic Radius (van der Waals)	217 pm
Ionization Energy	7.344 eV
Electron Affinity	1.2 eV
Melting Point	505.08 K
Boiling Point	2875 K
Density	7.287 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Sb':
	print('''
Antimony
51
Metalloid
	
Atomic Mass	121.760 u
Standard State	solid
Electron Configuration	[Kr]5s24d105p3
Oxidation States	+5, +3, -3
Electronegativity (Pauling Scale)	2.05
Atomic Radius (van der Waals)	206 pm
Ionization Energy	8.64 eV
Electron Affinity	1.07 eV
Melting Point	903.78 K
Boiling Point	1860 K
Density	6.685 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Te':
	print('''
Tellurium
52
Metalloid
	
Atomic Mass	127.6 u
Standard State	solid
Electron Configuration	[Kr]5s24d105p4
Oxidation States	+6, +4, -2
Electronegativity (Pauling Scale)	2.1
Atomic Radius (van der Waals)	206 pm
Ionization Energy	9.010 eV
Electron Affinity	1.971 eV
Melting Point	722.66 K
Boiling Point	1261 K
Density	6.232 g/cm³
Year Discovered	1782
''')

if p_table_input == 'l':
	print('''
Iodine
53
Halogen
	
Atomic Mass	126.9045 u
Standard State	solid
Electron Configuration	[Kr]5s24d105p5
Oxidation States	+7, +5, +1, -1
Electronegativity (Pauling Scale)	2.66
Atomic Radius (van der Waals)	198 pm
Ionization Energy	10.451 eV
Electron Affinity	3.059 eV
Melting Point	386.85 K
Boiling Point	457.55 K
Density	4.93 g/cm³
Year Discovered	1811
''')

if p_table_input == 'Xe':
	print('''
Xenon
54
Noble Gas
	
Atomic Mass	131.29 u
Standard State	gas
Electron Configuration	[Kr]5s24d105p6
Oxidation States	0
Electronegativity (Pauling Scale)	2.6
Atomic Radius (van der Waals)	216 pm
Ionization Energy	12.130 eV
Melting Point	161.36 K
Boiling Point	165.03 K
Density	0.005887 g/cm³
Year Discovered	1898
''')

if p_table_input == 'Cs':
	print('''
Cesium
55
Alkali Metal
	
Atomic Mass	132.9054520 u
Standard State	solid
Electron Configuration	[Xe]6s1
Oxidation States	+1
Electronegativity (Pauling Scale)	0.79
Atomic Radius (van der Waals)	343 pm
Ionization Energy	3.894 eV
Electron Affinity	0.472 eV
Melting Point	301.59 K
Boiling Point	944 K
Density	1.93 g/cm³
Year Discovered	1860
''')

if p_table_input == 'Ba':
	print('''
Barium
56
Alkaline Earth Metal
	
Atomic Mass	137.33 u
Standard State	solid
Electron Configuration	[Xe]6s2
Oxidation States	+2
Electronegativity (Pauling Scale)	0.89
Atomic Radius (van der Waals)	268 pm
Ionization Energy	5.212 eV
Melting Point	1000 K
Boiling Point	2170 K
Density	3.62 g/cm³
Year Discovered	1808
''')

if p_table_input == 'Hf':
	print('''
Hafnium
72
Transition Metal
	
Atomic Mass	178.49 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d2
Oxidation States	+4
Electronegativity (Pauling Scale)	1.3
Atomic Radius (van der Waals)	212 pm
Ionization Energy	6.825 eV
Melting Point	2506 K
Boiling Point	4876 K
Density	13.3 g/cm³
Year Discovered	1923
''')

if p_table_input == 'Ta':
	print('''
Tantalum
73
Transition Metal
	
Atomic Mass	180.9479 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d3
Oxidation States	+5
Electronegativity (Pauling Scale)	1.5
Atomic Radius (van der Waals)	217 pm
Ionization Energy	7.89 eV
Electron Affinity	0.322 eV
Melting Point	3290 K
Boiling Point	5731 K
Density	16.4 g/cm³
Year Discovered	1802
''')

if p_table_input == 'W':
	print('''
Tungsten
74
Transition Metal
	
Atomic Mass	183.84 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d4
Oxidation States	+6
Electronegativity (Pauling Scale)	2.36
Atomic Radius (van der Waals)	210 pm
Ionization Energy	7.98 eV
Electron Affinity	0.815 eV
Melting Point	3695 K
Boiling Point	5828 K
Density	19.3 g/cm³
Year Discovered	1783
''')

if p_table_input == 'Re':
	print('''
Rhenium
75
Transition Metal
	
Atomic Mass	186.207 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d5
Oxidation States	+7, +6, +4
Electronegativity (Pauling Scale)	1.9
Atomic Radius (van der Waals)	217 pm
Ionization Energy	7.88 eV
Electron Affinity	0.15 eV
Melting Point	3459 K
Boiling Point	5869 K
Density	20.8 g/cm³
Year Discovered	1925
''')

if p_table_input == 'Os':
	print('''
Osmium
76
Transition Metal
	
Atomic Mass	190.2 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d6
Oxidation States	+4, +3
Electronegativity (Pauling Scale)	2.2
Atomic Radius (van der Waals)	216 pm
Ionization Energy	8.7 eV
Electron Affinity	1.1 eV
Melting Point	3306 K
Boiling Point	5285 K
Density	22.57 g/cm³
Year Discovered	1803
''')

if p_table_input == 'lr':
	print('''
Iridium
77
Transition Metal
	
Atomic Mass	192.22 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d7
Oxidation States	+4, +3
Electronegativity (Pauling Scale)	2.2
Atomic Radius (van der Waals)	202 pm
Ionization Energy	9.1 eV
Electron Affinity	1.565 eV
Melting Point	2719 K
Boiling Point	4701 K
Density	22.42 g/cm³
Year Discovered	1803
''')

if p_table_input == 'Pt':
	print('''
Platinum
78
Transition Metal
	
Atomic Mass	195.08 u
Standard State	solid
Electron Configuration	[Xe]6s14f145d9
Oxidation States	+4, +2
Electronegativity (Pauling Scale)	2.28
Atomic Radius (van der Waals)	209 pm
Ionization Energy	9 eV
Electron Affinity	2.128 eV
Melting Point	2041.55 K
Boiling Point	4098 K
Density	21.46 g/cm³
Year Discovered	1735
''')

if p_table_input == 'Au':
	print('''
Gold
79
Transition Metal
	
Atomic Mass	196.96657 u
Standard State	solid
Electron Configuration	[Xe]6s14f145d10
Oxidation States	+3, +1
Electronegativity (Pauling Scale)	2.54
Atomic Radius (van der Waals)	166 pm
Ionization Energy	9.226 eV
Electron Affinity	2.309 eV
Melting Point	1337.33 K
Boiling Point	3129 K
Density	19.282 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Hg':
	print('''
Mercury
80
Transition Metal
	
Atomic Mass	200.59 u
Standard State	liquid
Electron Configuration	[Xe]6s24f145d10
Oxidation States	+2, +1
Electronegativity (Pauling Scale)	2
Atomic Radius (van der Waals)	209 pm
Ionization Energy	10.438 eV
Melting Point	234.32 K
Boiling Point	629.88 K
Density	13.5336 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Tl':
	print('''
Thallium
81
Post-transition Metal
	
Atomic Mass	204.383 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d106p1
Oxidation States	+3, +1
Electronegativity (Pauling Scale)	1.62
Atomic Radius (van der Waals)	196 pm
Ionization Energy	6.108 eV
Electron Affinity	0.2 eV
Melting Point	577 K
Boiling Point	1746 K
Density	11.8 g/cm³
Year Discovered	1861
''')

if p_table_input == 'Pb':
	print('''
Lead
82
Post-transition Metal
	
Atomic Mass	207 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d106p2
Oxidation States	+4, +2
Electronegativity (Pauling Scale)	2.33
Atomic Radius (van der Waals)	202 pm
Ionization Energy	7.417 eV
Electron Affinity	0.36 eV
Melting Point	600.61 K
Boiling Point	2022 K
Density	11.342 g/cm³
Year Discovered	ancient
''')

if p_table_input == 'Bi':
	print('''
Bismuth
83
Post-transition Metal
	
Atomic Mass	208.98040 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d106p3
Oxidation States	+5, +3
Electronegativity (Pauling Scale)	2.02
Atomic Radius (van der Waals)	207 pm
Ionization Energy	7.289 eV
Electron Affinity	0.946 eV
Melting Point	544.55 K
Boiling Point	1837 K
Density	9.807 g/cm³
Year Discovered	1753
''')

if p_table_input == 'Po':
	print('''
Polonium
84
Matalloid
	
Atomic Mass	208.98243 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d106p4
Oxidation States	+4, +2
Electronegativity (Pauling Scale)	2
Atomic Radius (van der Waals)	197 pm
Ionization Energy	8.417 eV
Electron Affinity	1.9 eV
Melting Point	527 K
Boiling Point	1235 K
Density	9.32 g/cm³
Year Discovered	1898
''')

if p_table_input == 'At':
	print('''
Astatine
85
Halogen
	
Atomic Mass	209.98715 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d106p5
Oxidation States	7, 5, 3, 1, -1
Electronegativity (Pauling Scale)	2.2
Atomic Radius (van der Waals)	202 pm
Ionization Energy	9.5 eV
Electron Affinity	2.8 eV
Melting Point	575 K
Density	7 g/cm³
Year Discovered	1940
''')

if p_table_input == 'Rn':
	print('''
Radon
86
Noble Gas
	
Atomic Mass	222.01758 u
Standard State	gas
Electron Configuration	[Xe]6s24f145d106p6
Oxidation States	0
Atomic Radius (van der Waals)	220 pm
Ionization Energy	10.745 eV
Melting Point	202 K
Boiling Point	211.45 K
Density	0.00973 g/cm³
Year Discovered	1900
''')

if p_table_input == 'Fr':
	print('''
Francium
87
Alkali Metal
	
Atomic Mass	223.01973 u
Standard State	solid
Electron Configuration	[Rn]7s1
Oxidation States	+1
Electronegativity (Pauling Scale)	0.7
Atomic Radius (van der Waals)	348 pm
Ionization Energy	3.9 eV
Electron Affinity	0.47 eV
Melting Point	300 K
Year Discovered	1939
''')

if p_table_input == 'Ra':
	print('''
Radium
88
Alkaline Earth Metal
	
Atomic Mass	226.02541 u
Standard State	solid
Electron Configuration	[Rn]7s2
Oxidation States	+2
Electronegativity (Pauling Scale)	0.9
Atomic Radius (van der Waals)	283 pm
Ionization Energy	5.279 eV
Melting Point	973 K
Boiling Point	1413 K
Density	5 g/cm³
Year Discovered	1898
''')

if p_table_input == 'Rf':
	print('''
Rutherfordium
104
Transition Metal
	
Atomic Mass	267.122 u
Standard State	solid
Electron Configuration	[Rn]7s25f146d2
Oxidation States	+4
Year Discovered	1964
''')

if p_table_input == 'Db':
	print('''
Dubnium
105
Transition Metal
	
Atomic Mass	268.126 u
Standard State	solid
Electron Configuration	[Rn]7s25f146d3
Oxidation States	5, 4, 3
Year Discovered	1967
''')

if p_table_input == 'Sg':
	print('''
Seaborgium
106
Transition Metal
	
Atomic Mass	269.128 u
Standard State	solid
Electron Configuration	[Rn]7s25f146d4
Oxidation States	6, 5, 4, 3, 0
Year Discovered	1974
''')

if p_table_input == 'Bh':
	print('''
Bohrium
107
Transition Metal
	
Atomic Mass	270.133 u
Standard State	solid
Electron Configuration	[Rn]7s25f146d5
Oxidation States	7, 5, 4, 3
Year Discovered	1976
''')

if p_table_input == 'Hs':
	print('''
Hassium
108
Transition Metal
	
Atomic Mass	269.1336 u
Standard State	solid
Electron Configuration	[Rn]7s25f146d6
Oxidation States	8, 6, 5, 4, 3, 2
Year Discovered	1984
''')

if p_table_input == 'Mt':
	print('''
Meitnerium
109
Transition Metal
	
Atomic Mass	277.154 u
Standard State	solid
Electron Configuration	[Rn]7s25f146d7
Oxidation States	9, 8, 6, 4, 3, 1
Year Discovered	1982
''')

if p_table_input == 'Ds':
	print('''
Darmstadtium
110
Transition Metal
	
Atomic Mass	282.166 u
Standard State	solid (expected)
Electron Configuration	[Rn]7s25f146d8
Oxidation States	8, 6, 4, 2, 0
Year Discovered	1994
''')

if p_table_input == 'Rg':
	print('''
Roentgenium
111
Transition Metal
	
Atomic Mass	282.169 u
Standard State	solid (expected)
Electron Configuration	[Rn]7s25f146d9
Oxidation States	5, 3, 1, -1
Year Discovered	1994
''')

if p_table_input == 'Cn':
	print('''
Copernicium
112
Transition Metal
	
Atomic Mass	286.179 u
Standard State	solid (expected)
Electron Configuration	[Rn]7s25f146d10
Oxidation States	2, 1, 0
Year Discovered	1996
''')

if p_table_input == 'Nh':
	print('''
Nihonium
113
Post-transition Metal
	
Atomic Mass	286.182 u
Standard State	solid (expected)
Electron Configuration	[Rn]5f146d107s27p1
Year Discovered	2004
''')

if p_table_input == 'Fl':
	print('''
Flerovium
114
Post-transition Metal
	
Atomic Mass	290.192 u
Standard State	solid (expected)
Electron Configuration	[Rn]7s27p25f146d10
Oxidation States	6, 4,2, 1, 0
Year Discovered	1998
''')

if p_table_input == 'Mc':
	print('''
Moscovium
115
Post-transition Metal
	
Atomic Mass	290.196 u
Standard State	solid (expected)
Electron Configuration	[Rn]7s27p35f146d10
Oxidation States	3, 1
Year Discovered	2003
''')

if p_table_input == 'Lv':
	print('''
Livermorium
116
Post-transition Metal
	
Atomic Mass	293.205 u
Standard State	solid (expected)
Electron Configuration	[Rn]7s27p45f146d10
Oxidation States	+4, +2, -2
Year Discovered	2000
''')

if p_table_input == 'Ts':
	print('''
Tennessine
117
Halogen
	
Atomic Mass	294.211 u
Standard State	solid (expected)
Electron Configuration	[Rn]7s27p55f146d10
Oxidation States	+5, +3, +1, -1
Year Discovered	2010
''')

if p_table_input == 'Og':
	print('''
Oganesson
118
Noble Gas
	
Atomic Mass	295.216 u
Standard State	gas (expected)
Electron Configuration	[Rn]7s27p65f146d10
Oxidation States	+6, +4, +2, +1, 0, -1
Year Discovered	2006
''')

if p_table_input == 'La':
	print('''
Lanthanum
57
Lanthanide
	
Atomic Mass	138.9055 u
Standard State	solid
Electron Configuration	[Xe]6s25d1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.1
Atomic Radius (van der Waals)	240 pm
Ionization Energy	5.577 eV
Electron Affinity	0.5 eV
Melting Point	1191 K
Boiling Point	3737 K
Density	6.15 g/cm³
Year Discovered	1839
''')

if p_table_input == 'Ce':
	print('''
Cerium
58
Lanthanide
	
Atomic Mass	140.116 u
Standard State	solid
Electron Configuration	[Xe]6s24f15d1
Oxidation States	+4, +3
Electronegativity (Pauling Scale)	1.12
Atomic Radius (van der Waals)	235 pm
Ionization Energy	5.539 eV
Electron Affinity	0.5 eV
Melting Point	1071 K
Boiling Point	3697 K
Density	6.770 g/cm³
Year Discovered	1803
''')

if p_table_input == 'Pr':
	print('''
Praseodymium
59
Lanthanide
	
Atomic Mass	140.90766 u
Standard State	solid
Electron Configuration	[Xe]6s24f3
Oxidation States	+3
Electronegativity (Pauling Scale)	1.13
Atomic Radius (van der Waals)	239 pm
Ionization Energy	5.464 eV
Melting Point	1204 K
Boiling Point	3793 K
Density	6.77 g/cm³
Year Discovered	1885
''')

if p_table_input == 'Nd':
	print('''
Neodymium
60
Lanthanide
	
Atomic Mass	144.24 u
Standard State	solid
Electron Configuration	[Xe]6s24f4
Oxidation States	+3
Electronegativity (Pauling Scale)	1.14
Atomic Radius (van der Waals)	229 pm
Ionization Energy	5.525 eV
Melting Point	1294 K
Boiling Point	3347 K
Density	7.01 g/cm³
Year Discovered	1885
''')

if p_table_input == 'Pm':
	print('''
Promethium
61
Lanthanide
	
Atomic Mass	144.91276 u
Standard State	solid
Electron Configuration	[Xe]6s24f5
Oxidation States	+3
Atomic Radius (van der Waals)	236 pm
Ionization Energy	5.55 eV
Melting Point	1315 K
Boiling Point	3273 K
Density	7.26 g/cm³
Year Discovered	1945
''')

if p_table_input == 'Sm':
	print('''
Samarium
62
Lanthanide
	
Atomic Mass	150.4 u
Standard State	solid
Electron Configuration	[Xe]6s24f6
Oxidation States	+3, +2
Electronegativity (Pauling Scale)	1.17
Atomic Radius (van der Waals)	229 pm
Ionization Energy	5.644 eV
Melting Point	1347 K
Boiling Point	2067 K
Density	7.52 g/cm³
Year Discovered	1879
''')

if p_table_input == 'Eu':
	print('''
Europium
63
Lanthanide
	
Atomic Mass	151.964 u
Standard State	solid
Electron Configuration	[Xe]6s24f7
Oxidation States	+3, +2
Atomic Radius (van der Waals)	233 pm
Ionization Energy	5.670 eV
Melting Point	1095 K
Boiling Point	1802 K
Density	5.24 g/cm³
Year Discovered	1901
''')

if p_table_input == 'Gd':
	print('''
Gadolinium
64
Lanthanide
	
Atomic Mass	157.2 u
Standard State	solid
Electron Configuration	[Xe]6s24f75d1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.2
Atomic Radius (van der Waals)	237 pm
Ionization Energy	6.150 eV
Melting Point	1586 K
Boiling Point	3546 K
Density	7.90 g/cm³
Year Discovered	1880
''')

if p_table_input == 'Tb':
	print('''
Terbium
65
Lanthanide
	
Atomic Mass	158.92535 u
Standard State	solid
Electron Configuration	[Xe]6s24f9
Oxidation States	+3
Atomic Radius (van der Waals)	221 pm
Ionization Energy	5.864 eV
Melting Point	1629 K
Boiling Point	3503 K
Density	8.23 g/cm³
Year Discovered	1843
''')

if p_table_input == 'Dy':
	print('''
Dysprosium
66
Lanthanide
	
Atomic Mass	162.500 u
Standard State	solid
Electron Configuration	[Xe]6s24f10
Oxidation States	+3
Electronegativity (Pauling Scale)	1.22
Atomic Radius (van der Waals)	229 pm
Ionization Energy	5.939 eV
Melting Point	1685 K
Boiling Point	2840 K
Density	8.55 g/cm³
Year Discovered	1886
''')

if p_table_input == 'Ho':
	print('''
Holmium
67
Lanthanide
	
Atomic Mass	164.93033 u
Standard State	solid
Electron Configuration	[Xe]6s24f11
Oxidation States	+3
Electronegativity (Pauling Scale)	1.23
Atomic Radius (van der Waals)	216 pm
Ionization Energy	6.022 eV
Melting Point	1747 K
Boiling Point	2973 K
Density	8.80 g/cm³
Year Discovered	1878
''')

if p_table_input == 'Er':
	print('''
Erbium
68
Lanthanide
	
Atomic Mass	167.26 u
Standard State	solid
Electron Configuration	[Xe]6s24f12
Oxidation States	+3
Electronegativity (Pauling Scale)	1.24
Atomic Radius (van der Waals)	235 pm
Ionization Energy	6.108 eV
Melting Point	1802 K
Boiling Point	3141 K
Density	9.07 g/cm³
Year Discovered	1843
''')

if p_table_input == 'Tm':
	print('''
Thulium
69
Lanthanide
	
Atomic Mass	168.93422 u
Standard State	solid
Electron Configuration	[Xe]6s24f13
Oxidation States	+3
Electronegativity (Pauling Scale)	1.25
Atomic Radius (van der Waals)	227 pm
Ionization Energy	6.184 eV
Melting Point	1818 K
Boiling Point	2223 K
Density	9.32 g/cm³
Year Discovered	1879
''')

if p_table_input == 'Yb':
	print('''
Ytterbium
70
Lanthanide	

Atomic Mass	173.05 u
Standard State	solid
Electron Configuration	[Xe]6s24f14
Oxidation States	+3, +2
Atomic Radius (van der Waals)	242 pm
Ionization Energy	6.254 eV
Melting Point	1092 K
Boiling Point	1469 K
Density	6.90 g/cm³
Year Discovered	1878
''')

if p_table_input == 'Lu':
	print('''
Lutetium
71
Lanthanide
	
Atomic Mass	174.9668 u
Standard State	solid
Electron Configuration	[Xe]6s24f145d1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.27
Atomic Radius (van der Waals)	221 pm
Ionization Energy	5.426 eV
Melting Point	1936 K
Boiling Point	3675 K
Density	9.84 g/cm³
Year Discovered	1907
''')

if p_table_input == 'Ac':
	print('''
Actinium
89
Actinide
	
Atomic Mass	227.02775 u
Standard State	solid
Electron Configuration	[Rn]7s26d1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.1
Atomic Radius (van der Waals)	260 pm
Ionization Energy	5.17 eV
Melting Point	1324 K
Boiling Point	3471 K
Density	10.07 g/cm³
Year Discovered	1899
''')

if p_table_input == 'Th':
	print('''
Thorium
90
Actinide
	
Atomic Mass	232.038 u
Standard State	solid
Electron Configuration	[Rn]7s26d2
Oxidation States	+4
Electronegativity (Pauling Scale)	1.3
Atomic Radius (van der Waals)	237 pm
Ionization Energy	6.08 eV
Melting Point	2023 K
Boiling Point	5061 K
Density	11.72 g/cm³
Year Discovered	1828
''')

if p_table_input == 'Pa':
	print('''
Protactinium
91
Actinide
	
Atomic Mass	231.03588 u
Standard State	solid
Electron Configuration	[Rn]7s25f26d1
Oxidation States	+5, +4
Electronegativity (Pauling Scale)	1.5
Atomic Radius (van der Waals)	243 pm
Ionization Energy	5.89 eV
Melting Point	1845 K
Density	15.37 g/cm³
Year Discovered	1913
''')

if p_table_input == 'U':
	print('''
Uranium
92
Actinide
	
Atomic Mass	238.0289 u
Standard State	solid
Electron Configuration	[Rn]7s25f36d1
Oxidation States	+6, +5, +4, +3
Electronegativity (Pauling Scale)	1.38
Atomic Radius (van der Waals)	240 pm
Ionization Energy	6.194 eV
Melting Point	1408 K
Boiling Point	4404 K
Density	18.95 g/cm³
Year Discovered	1789
''')

if p_table_input == 'Np':
	print('''
Neptunium
93
Actinide
	
Atomic Mass	237.048172 u
Standard State	solid
Electron Configuration	[Rn]7s25f46d1
Oxidation States	+6, +5, +4, +3
Electronegativity (Pauling Scale)	1.36
Atomic Radius (van der Waals)	221 pm
Ionization Energy	6.266 eV
Melting Point	917 K
Boiling Point	4175 K
Density	20.25 g/cm³
Year Discovered	1940
''')

if p_table_input == 'Pu':
	print('''
Plutonium
94
Actinide
	
Atomic Mass	244.06420 u
Standard State	solid
Electron Configuration	[Rn]7s25f6
Oxidation States	+6, +5, +4, +3
Electronegativity (Pauling Scale)	1.28
Atomic Radius (van der Waals)	243 pm
Ionization Energy	6.06 eV
Melting Point	913 K
Boiling Point	3501 K
Density	19.84 g/cm³
Year Discovered	1940
''')

if p_table_input == 'Am':
	print('''
Americium
95
Actinide
	
Atomic Mass	243.061380 u
Standard State	solid
Electron Configuration	[Rn]7s25f7
Oxidation States	+6, +5, +4, +3
Electronegativity (Pauling Scale)	1.3
Atomic Radius (van der Waals)	244 pm
Ionization Energy	5.993 eV
Melting Point	1449 K
Boiling Point	2284 K
Density	13.69 g/cm³
Year Discovered	1944
''')

if p_table_input == 'Cm':
	print('''
Curium
96
Actinide
	
Atomic Mass	247.07035 u
Standard State	solid
Electron Configuration	[Rn]7s25f76d1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.3
Atomic Radius (van der Waals)	245 pm
Ionization Energy	6.02 eV
Melting Point	1618 K
Boiling Point	3400 K
Density	13.51 g/cm³
Year Discovered	1944
''')

if p_table_input == 'Bk':
	print('''
Berkelium
97
Actinide

Atomic Mass	247.07031 u
Standard State	solid
Electron Configuration	[Rn]7s25f9
Oxidation States	+4, +3
Electronegativity (Pauling Scale)	1.3
Atomic Radius (van der Waals)	244 pm
Ionization Energy	6.23 eV
Melting Point	1323 K
Density	14 g/cm³
Year Discovered	1949
''')

if p_table_input == 'Cf':
	print('''
Californium
98
Actinide
	
Atomic Mass	251.07959 u
Standard State	solid
Electron Configuration	[Rn]7s25f10
Oxidation States	+3
Electronegativity (Pauling Scale)	1.3
Atomic Radius (van der Waals)	245 pm
Ionization Energy	6.30 eV
Melting Point	1173 K
Year Discovered	1950
''')

if p_table_input == 'Es':
	print('''
Einsteinium
99
Actinide
	
Atomic Mass	252.0830 u
Standard State	solid
Electron Configuration	[Rn]7s25f11
Oxidation States	+3
Electronegativity (Pauling Scale)	1.3
Atomic Radius (van der Waals)	245 pm
Ionization Energy	6.42 eV
Melting Point	1133 K
Year Discovered	1952
''')

if p_table_input == 'Fm':
	print('''
Fermium
100
Actinide
	
Atomic Mass	257.09511 u
Standard State	solid
Electron Configuration	[Rn]5f127s2
Oxidation States	+3
Electronegativity (Pauling Scale)	1.3
Ionization Energy	6.50 eV
Melting Point	1800 K
Year Discovered	1952
''')

if p_table_input == 'Md':
	print('''
Mendelevium
101
Actinide
	
Atomic Mass	258.09843 u
Standard State	solid
Electron Configuration	[Rn]7s25f13
Oxidation States	+3, +2
Electronegativity (Pauling Scale)	1.3
Ionization Energy	6.58 eV
Melting Point	1100 K
Year Discovered	1955
''')

if p_table_input == 'No':
	print('''
Nobelium
102
Actinide
	
Atomic Mass	259.10100 u
Standard State	solid
Electron Configuration	[Rn]7s25f14
Oxidation States	+3, +2
Electronegativity (Pauling Scale)	1.3
Ionization Energy	6.65 eV
Melting Point	1100 K
Year Discovered	1957
''')

if p_table_input == 'Lr':
	print('''
Lawrencium
103
Actinide
	
Atomic Mass	266.120 u
Standard State	solid
Electron Configuration	[Rn]7s25f146d1
Oxidation States	+3
Electronegativity (Pauling Scale)	1.3
Melting Point	1900 K
Year Discovered	1961
''')

anotha = input("PRESS ENTER TO RETURN HOME <>--->")
os.system('clear')
os.system('python /home/puta/CRAZY/terminals/chem-term/scripts/periodic_table/p_table.py')
