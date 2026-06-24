BEAVRS Cycle 1 full-core PWR - MCNP translation (community example deck)
c =====================================================================
c PROVENANCE: Geometry + materials translated from the author-VERIFIED
c Cambridge SCONE BEAVRS full-core deck (reactor-test-decks/
c beavrs_scone_fullcore.scone) and the public MIT BEAVRS rev 2.0.2
c specification (Horelik, Herman, Forget, Smith; CRPG/MIT, 2018).
c This is a COMMUNITY EXAMPLE DECK, geometry/materials-derived - it is
c NOT benchmark-validated. Not an official MIT/CRPG product.
c
c WHAT THIS DECK CONTAINS:
c  - 17x17 core lattice (assembly pitch 21.50364 cm), 193 fuel assemblies
c    on the verified BEAVRS loading map (3 enrichment zones).
c  - 17x17 assemblies (pin pitch 1.26 cm): fuel 0.39218/gap 0.40005/
c    clad 0.45720 cm; 24 guide tubes + 1 central instrument tube.
c  - Enrichment zones: 1.6 / 2.4 / 3.1 wt% UO2 (m16/m24/m31).
c  - Pyrex burnable poison rods (m6) in BA assemblies; control rods
c    fully WITHDRAWN (guide tubes water-filled), matching the SCONE deck.
c  - Radial: core barrel (SS304) / downcomer water / RPV liner / RPV
c    (carbon steel); vacuum outside.
c
c ASSUMPTIONS / SIMPLIFICATIONS (FLAGGED):
c  * Library: ZAID suffix .80c (ENDF/B-VII.1, 293.6 K) assumed for
c    availability. The VERIFIED SCONE deck used JEF-3.1.1 at 600 K.
c    Material NUMBER DENSITIES are identical to the verified deck;
c    only the data library/temperature differ -> expect a cross-library
c    k-eff bias. For 600 K work use a hot library (e.g. .81c/.82c) or
c    tmp/mt cards. lwtr.20t S(a,b) is on WATER ONLY (never on UO2).
c  * Axial geometry SIMPLIFIED: a single uniform active-fuel zone
c    (0 -> 365.76 cm) with ~30 cm water reflectors top/bottom. The
c    verified deck's ~25 axial layers (grid spacers, plenum, nozzles,
c    dashpot, end plugs) are NOT reproduced here.
c  * Burnable-poison spatial layout is a REPRESENTATIVE 20-rod Pyrex
c    pattern applied uniformly to all BA assemblies (the verified deck's
c    6/12/15/16/20-rod directional variants are collapsed).
c  * Neutron-shield panels and the detailed SS baffle/former plates are
c    omitted (radial reflector = water + barrel + RPV).
c  * Cell densities are POSITIVE atoms/b-cm (= per-material sums); m-card
c    fractions are POSITIVE atom densities, so MCNP reproduces the exact
c    verified number densities.
c =====================================================================
c ----- Fuel pins: u=1 (1.6%), u=2 (2.4%), u=3 (3.1%) -----
1  16 6.89175e-2  -1     u=1 imp:n=1   $ UO2 1.6%
2  2  2.40440e-4   1 -2   u=1 imp:n=1   $ He gap
3  4  4.34389e-2   2 -3   u=1 imp:n=1   $ Zircaloy clad
4  5  7.41863e-2    3      u=1 imp:n=1   $ borated water
5  24 6.88170e-2  -1     u=2 imp:n=1   $ UO2 2.4%
6  2  2.40440e-4   1 -2   u=2 imp:n=1
7  4  4.34389e-2   2 -3   u=2 imp:n=1
8  5  7.41863e-2    3      u=2 imp:n=1
9  31 6.88510e-2  -1     u=3 imp:n=1   $ UO2 3.1%
10 2  2.40440e-4   1 -2   u=3 imp:n=1
11 4  4.34389e-2   2 -3   u=3 imp:n=1
12 5  7.41863e-2    3      u=3 imp:n=1
c ----- Guide tube u=4 (CR withdrawn -> water-filled) -----
13 5  7.41863e-2   -4      u=4 imp:n=1
14 4  4.34389e-2   4 -5   u=4 imp:n=1
15 5  7.41863e-2    5      u=4 imp:n=1
c ----- Instrument tube u=5 (air / Zr / water / Zr / water) -----
16 9  2.52837e-4 -6      u=5 imp:n=1   $ air thimble
17 4  4.34389e-2   6 -7   u=5 imp:n=1
18 5  7.41863e-2    7 -8   u=5 imp:n=1
19 4  4.34389e-2   8 -9   u=5 imp:n=1
20 5  7.41863e-2    9      u=5 imp:n=1
c ----- Pyrex burnable-poison pin u=6 (BP above dashpot) -----
21 9  2.52837e-4 -30     u=6 imp:n=1   $ air
22 7  8.79322e-2   30 -31 u=6 imp:n=1   $ SS304 inner tube
23 2  2.40440e-4   31 -32 u=6 imp:n=1   $ He
24 6  7.15028e-2   32 -33 u=6 imp:n=1   $ borosilicate (pyrex)
25 2  2.40440e-4   33 -34 u=6 imp:n=1   $ He
26 7  8.79322e-2   34 -35 u=6 imp:n=1   $ SS304 outer tube
27 5  7.41863e-2    35 -36 u=6 imp:n=1   $ water
28 4  4.34389e-2   36 -37 u=6 imp:n=1   $ Zircaloy guide tube
29 5  7.41863e-2    37    u=6 imp:n=1   $ water
c ----- Water "assembly" universe u=30 (reflector positions) -----
40 5  7.41863e-2          u=30 imp:n=1
c ----- Assembly lattices (u=20 A16, 21 A24, 22 A24B, 23 A31, 24 A31B) -----
100 0  50 -51 52 -53  lat=1 u=20 imp:n=1
     fill=0:16 0:16 0:0
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
       1  1  1  1  1  4  1  1  4  1  1  4  1  1  1  1  1
       1  1  1  4  1  1  1  1  1  1  1  1  1  4  1  1  1
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
       1  1  4  1  1  4  1  1  4  1  1  4  1  1  4  1  1
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
       1  1  4  1  1  4  1  1  5  1  1  4  1  1  4  1  1
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
       1  1  4  1  1  4  1  1  4  1  1  4  1  1  4  1  1
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
       1  1  1  4  1  1  1  1  1  1  1  1  1  4  1  1  1
       1  1  1  1  1  4  1  1  4  1  1  4  1  1  1  1  1
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
       1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1
101 0  50 -51 52 -53  lat=1 u=21 imp:n=1
     fill=0:16 0:16 0:0
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  4  2  2  4  2  2  4  2  2  2  2  2
       2  2  2  4  2  2  2  2  2  2  2  2  2  4  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  4  2  2  4  2  2  4  2  2  4  2  2  4  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  4  2  2  4  2  2  5  2  2  4  2  2  4  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  4  2  2  4  2  2  4  2  2  4  2  2  4  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  4  2  2  2  2  2  2  2  2  2  4  2  2  2
       2  2  2  2  2  4  2  2  4  2  2  4  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
102 0  50 -51 52 -53  lat=1 u=22 imp:n=1
     fill=0:16 0:16 0:0
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  6  2  2  6  2  2  6  2  2  2  2  2
       2  2  2  6  2  2  2  2  2  2  2  2  2  6  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  6  2  2  6  2  2  4  2  2  6  2  2  6  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  6  2  2  4  2  2  5  2  2  4  2  2  6  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  6  2  2  6  2  2  4  2  2  6  2  2  6  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  6  2  2  2  2  2  2  2  2  2  6  2  2  2
       2  2  2  2  2  6  2  2  6  2  2  6  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
       2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2
103 0  50 -51 52 -53  lat=1 u=23 imp:n=1
     fill=0:16 0:16 0:0
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  4  3  3  4  3  3  4  3  3  3  3  3
       3  3  3  4  3  3  3  3  3  3  3  3  3  4  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  4  3  3  4  3  3  4  3  3  4  3  3  4  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  4  3  3  4  3  3  5  3  3  4  3  3  4  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  4  3  3  4  3  3  4  3  3  4  3  3  4  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  4  3  3  3  3  3  3  3  3  3  4  3  3  3
       3  3  3  3  3  4  3  3  4  3  3  4  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
104 0  50 -51 52 -53  lat=1 u=24 imp:n=1
     fill=0:16 0:16 0:0
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  6  3  3  6  3  3  6  3  3  3  3  3
       3  3  3  6  3  3  3  3  3  3  3  3  3  6  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  6  3  3  6  3  3  4  3  3  6  3  3  6  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  6  3  3  4  3  3  5  3  3  4  3  3  6  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  6  3  3  6  3  3  4  3  3  6  3  3  6  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  6  3  3  3  3  3  3  3  3  3  6  3  3  3
       3  3  3  3  3  6  3  3  6  3  3  6  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
       3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3
c ----- Core lattice u=100 (assembly pitch 21.50364) -----
200 0  60 -61 62 -63  lat=1 u=100 imp:n=1
     fill=0:16 0:16 0:0
      30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30
      30 30 30 30 30 23 24 23 24 23 24 23 30 30 30 30 30
      30 30 30 23 23 24 20 24 20 24 20 24 23 23 30 30 30
      30 30 23 24 22 20 22 20 22 20 22 20 22 24 23 30 30
      30 30 23 22 21 22 20 22 20 22 20 22 21 22 23 30 30
      30 23 24 20 22 20 22 20 22 20 22 20 22 20 24 23 30
      30 24 20 22 20 22 20 22 20 22 20 22 20 22 20 24 30
      30 23 24 20 22 20 22 20 22 20 22 20 22 20 24 23 30
      30 24 20 22 20 22 20 22 20 22 20 22 20 22 20 24 30
      30 23 24 20 22 20 22 20 22 20 22 20 22 20 24 23 30
      30 24 20 22 20 22 20 22 20 22 20 22 20 22 20 24 30
      30 23 24 20 22 20 22 20 22 20 22 20 22 20 24 23 30
      30 30 23 22 21 22 20 22 20 22 20 22 21 22 23 30 30
      30 30 23 24 22 20 22 20 22 20 22 20 22 24 23 30 30
      30 30 30 23 23 24 20 24 20 24 20 24 23 23 30 30 30
      30 30 30 30 30 23 24 23 24 23 24 23 30 30 30 30 30
      30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30
c ----- Core container, reflectors, barrel, RPV, graveyard -----
300 0          -80 70 -71  fill=100 imp:n=1   $ active core (lattice)
301 5 7.41863e-2   -80 72 -70             imp:n=1   $ bottom water reflector
302 5 7.41863e-2   -80 71 -73             imp:n=1   $ top water reflector
303 7 8.79322e-2   80 -81 72 -73         imp:n=1   $ core barrel (SS304)
304 5 7.41863e-2    81 -82 72 -73         imp:n=1   $ downcomer water
305 7 8.79322e-2   82 -83 72 -73         imp:n=1   $ RPV liner (SS304)
306 8 8.50964e-2   83 -84 72 -73         imp:n=1   $ RPV (carbon steel)
307 0          84 : -72 : 73          imp:n=0   $ graveyard

c ===================== SURFACES =====================
1  cz 0.39218     $ fuel pellet
2  cz 0.40005     $ gap
3  cz 0.45720     $ clad
4  cz 0.56134     $ guide tube inner
5  cz 0.60198     $ guide tube outer
6  cz 0.43688     $ instr air
7  cz 0.48387     $ instr inner Zr
8  cz 0.56134     $ instr water
9  cz 0.60198     $ instr outer Zr
30 cz 0.21400     $ BP air
31 cz 0.23051     $ BP SS inner
32 cz 0.24130     $ BP He
33 cz 0.42672     $ BP pyrex
34 cz 0.43688     $ BP He
35 cz 0.48387     $ BP SS outer
36 cz 0.56134     $ BP water
37 cz 0.60198     $ BP Zr guide tube
50 px -0.63       $ pin lattice
51 px  0.63
52 py -0.63
53 py  0.63
60 px -10.75182   $ assembly lattice (pitch 21.50364)
61 px  10.75182
62 py -10.75182
63 py  10.75182
70 pz 0.0         $ active fuel bottom
71 pz 365.76      $ active fuel top
72 pz -30.0       $ reflector bottom
73 pz 395.76      $ reflector top
80 cz 187.96      $ core barrel inner
81 cz 193.675     $ core barrel outer
82 cz 219.150     $ RPV liner inner
83 cz 219.710     $ RPV inner
84 cz 241.3       $ RPV outer

c ===================== DATA =====================
c kcode: neutrons/cycle  k-guess  inactive  total cycles
kcode 20000 1.0 50 250
c Initial source: uniform across the active core footprint.
ksrc 0 0 182.88
c --- Materials (atom densities atoms/b-cm; ported from verified SCONE deck) ---
c UO2-16  (atom density sum = 6.89175e-2 atoms/b-cm)
m16   8016.80c     4.58970e-2
      8017.80c     1.74360e-5
      92234.80c    3.01310e-6
      92235.80c    3.75030e-4
      92238.80c    2.26250e-2
c UO2-24  (atom density sum = 6.88170e-2 atoms/b-cm)
m24   8016.80c     4.58300e-2
      8017.80c     1.74110e-5
      92234.80c    4.48420e-6
      92235.80c    5.58140e-4
      92238.80c    2.24070e-2
c UO2-31  (atom density sum = 6.88510e-2 atoms/b-cm)
m31   8016.80c     4.58530e-2
      8017.80c     1.74200e-5
      92234.80c    5.79870e-6
      92235.80c    7.21750e-4
      92238.80c    2.22530e-2
c Helium  (atom density sum = 2.40440e-4 atoms/b-cm)
m2   2003.80c     4.80890e-10
      2004.80c     2.40440e-4
c Zircaloy  (atom density sum = 4.34389e-2 atoms/b-cm)
m4   24050.80c    3.29620e-6
      24052.80c    6.35640e-5
      24053.80c    7.20760e-6
      24054.80c    1.79410e-6
      26054.80c    8.66980e-6
      26056.80c    1.36100e-4
      26057.80c    3.14310e-6
      26058.80c    4.18290e-7
      8016.80c     3.07440e-4
      8017.80c     1.16800e-7
      50112.80c    4.67350e-6
      50114.80c    3.17990e-6
      50115.80c    1.63810e-6
      50116.80c    7.00550e-5
      50117.80c    3.70030e-5
      50118.80c    1.16690e-4
      50119.80c    4.13870e-5
      50120.80c    1.56970e-4
      50122.80c    2.23080e-5
      50124.80c    2.78970e-5
      40090.80c    2.18280e-2
      40091.80c    4.76010e-3
      40092.80c    7.27590e-3
      40094.80c    7.37340e-3
      40096.80c    1.18790e-3
c Water  (atom density sum = 7.41863e-2 atoms/b-cm)
m5   1001.80c     4.94560e-2
      5010.80c     7.97140e-6
      5011.80c     3.22470e-5
      1002.80c     7.70350e-6
      8016.80c     2.46730e-2
      8017.80c     9.37340e-6
mt5   lwtr.20t
c BorosilicateGlass  (atom density sum = 7.15028e-2 atoms/b-cm)
m6   13027.80c    1.73520e-3
      5010.80c     9.65060e-4
      5011.80c     3.91890e-3
      8016.80c     4.65140e-2
      8017.80c     1.76710e-5
      14028.80c    1.69260e-2
      14029.80c    8.59440e-4
      14030.80c    5.66540e-4
c StainlessSteel304  (atom density sum = 8.79322e-2 atoms/b-cm)
m7   24050.80c    7.67780e-4
      24052.80c    1.48060e-2
      24053.80c    1.67890e-3
      24054.80c    4.17910e-4
      26054.80c    3.46200e-3
      26056.80c    5.43450e-2
      26057.80c    1.25510e-3
      26058.80c    1.67030e-4
      25055.80c    1.76040e-3
      28058.80c    5.60890e-3
      28060.80c    2.16050e-3
      28061.80c    9.39170e-5
      28062.80c    2.99450e-4
      28064.80c    7.62610e-5
      14028.80c    9.52810e-4
      14029.80c    4.83810e-5
      14030.80c    3.18930e-5
c CarbonSteel  (atom density sum = 8.50964e-2 atoms/b-cm)
m8   13027.80c    4.35230e-5
      5010.80c     2.58330e-6
      5011.80c     1.04500e-5
      6012.80c     1.04420e-3
      20040.80c    1.70430e-5
      20042.80c    1.13750e-7
      20043.80c    2.37340e-8
      20044.80c    3.66730e-7
      20046.80c    7.03220e-10
      20048.80c    3.28750e-8
      24050.80c    1.37380e-5
      24052.80c    2.64930e-4
      24053.80c    3.00410e-5
      24054.80c    7.47780e-6
      29063.80c    1.02230e-4
      29065.80c    4.56080e-5
      26054.80c    4.74370e-3
      26056.80c    7.44650e-2
      26057.80c    1.71970e-3
      26058.80c    2.28860e-4
      25055.80c    6.41260e-4
      42100.80c    2.98140e-5
      42092.80c    4.48220e-5
      42094.80c    2.81100e-5
      42095.80c    4.85670e-5
      42096.80c    5.10150e-5
      42097.80c    2.93190e-5
      42098.80c    7.43270e-5
      41093.80c    5.05590e-6
      28058.80c    4.08620e-4
      28060.80c    1.57400e-4
      28061.80c    6.84200e-6
      28062.80c    2.18150e-5
      28064.80c    5.55570e-6
      15031.80c    3.79130e-5
      16032.80c    3.48080e-5
      16033.80c    2.74200e-7
      16034.80c    1.53680e-6
      16036.80c    5.33980e-9
      14028.80c    6.17020e-4
      14029.80c    3.13300e-5
      14030.80c    2.06530e-5
      22046.80c    1.21440e-6
      22047.80c    1.09520e-6
      22048.80c    1.08510e-5
      22049.80c    7.96340e-7
      22050.80c    7.62490e-7
      23051.80c    4.59890e-5
c Air  (atom density sum = 2.52837e-4 atoms/b-cm)
m9   18036.80c    7.87300e-9
      18038.80c    1.48440e-9
      18040.80c    2.35060e-6
      6012.80c     6.75390e-8
      7014.80c     1.96800e-4
      7015.80c     7.23540e-7
      8016.80c     5.28660e-5
      8017.80c     2.00840e-8
c --- Tallies: assembly-wise fission via FMESH over the core footprint ---
fmesh4:n geom=xyz origin=-182.78094 -182.78094 0
        imesh=182.78094 iints=17
        jmesh=182.78094 jints=17
        kmesh=365.76 kints=1
prdmp j 250 1 2
print
