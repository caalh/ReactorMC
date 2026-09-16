BEAVRS-like PWR full core - OWEN 3D geometry preview test fixture (viz only)
c =====================================================================
c Nested lattice: a core lattice (pitch 21.50364 cm) of 17x17 assembly
c lattices (pitch 1.26 cm) of pins. ~197 fuel assemblies, 3-region
c illustrative loading (1.6 / 2.4 / 3.1 wt% UO2). Radii 0.39218 /
c 0.40005 / 0.45720; barrel & RPV shells from BEAVRS Rev 2.0.
c Closed and finite: every cell is bounded by 90/91 axially and 84 radially,
c and both lattice levels carry a water ring so no region is left without a
c universe. Runs without lost particles. The loading is illustrative, so the
c resulting k is not a BEAVRS result - do not cite it as one.
c ZAID library assumed .80c (ENDF/B-VII.1).
c =====================================================================
c ----- Fuel pins: u=1 (1.6%), u=2 (2.4%), u=3 (3.1%) -----
1  1 -10.40   -1     u=1 imp:n=1   $ UO2 1.6%
2  2 -0.00159  1 -2  u=1 imp:n=1
3  5 -6.55     2 -3  u=1 imp:n=1
4  6 -0.74     3     u=1 imp:n=1
5  3 -10.40   -1     u=2 imp:n=1   $ UO2 2.4%
6  2 -0.00159  1 -2  u=2 imp:n=1
7  5 -6.55     2 -3  u=2 imp:n=1
8  6 -0.74     3     u=2 imp:n=1
9  4 -10.40   -1     u=3 imp:n=1   $ UO2 3.1%
10 2 -0.00159  1 -2  u=3 imp:n=1
11 5 -6.55     2 -3  u=3 imp:n=1
12 6 -0.74     3     u=3 imp:n=1
c ----- Guide tube (u=4) -----
13 6 -0.74    -4     u=4 imp:n=1
14 5 -6.55     4 -5  u=4 imp:n=1
15 6 -0.74     5     u=4 imp:n=1
c ----- Instrument tube (u=5) -----
16 7 -0.00120 -6     u=5 imp:n=1   $ air
17 5 -6.55     6 -7  u=5 imp:n=1
18 6 -0.74     7 -8  u=5 imp:n=1
19 5 -6.55     8 -9  u=5 imp:n=1
20 6 -0.74     9     u=5 imp:n=1
c ----- Water-only universe (u=6) -----
c Fills the 0.042 cm gap between the 17x1.26 cm pin lattice and the
c 21.50364 cm assembly window, the unloaded core-lattice positions, and the
c corner of the barrel that the 17x17 assembly grid does not reach. Without
c it those regions have no universe under them and MCNP loses particles there.
21 6 -0.74    -3:3   u=6 imp:n=1   $ water everywhere (-3:3 = all space)
c ----- Assembly lattices (u=20 1.6%, u=21 2.4%, u=22 3.1%) -----
c Lattice cells list the +x (+y) plane FIRST: MCNP puts element (1,0,0) beyond the
c first listed surface (manual 5.5.5), so "-51 50" makes +i run toward +x and the
c fill array reads as drawn (bottom row first). "50 -51" mirrored the map 180 degrees.
100 0  -51 50 -53 52  lat=1 u=20 imp:n=1
     fill=-9:9 -9:9 0:0
      6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 1 1 1 1 1 4 1 1 4 1 1 4 1 1 1 1 1 6
      6 1 1 1 4 1 1 1 1 1 1 1 1 1 4 1 1 1 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 1 1 4 1 1 4 1 1 4 1 1 4 1 1 4 1 1 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 1 1 4 1 1 4 1 1 5 1 1 4 1 1 4 1 1 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 1 1 4 1 1 4 1 1 4 1 1 4 1 1 4 1 1 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 1 1 1 4 1 1 1 1 1 1 1 1 1 4 1 1 1 6
      6 1 1 1 1 1 4 1 1 4 1 1 4 1 1 1 1 1 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6
      6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
101 0  -51 50 -53 52  lat=1 u=21 imp:n=1
     fill=-9:9 -9:9 0:0
      6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 2 2 2 2 2 4 2 2 4 2 2 4 2 2 2 2 2 6
      6 2 2 2 4 2 2 2 2 2 2 2 2 2 4 2 2 2 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 2 2 4 2 2 4 2 2 4 2 2 4 2 2 4 2 2 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 2 2 4 2 2 4 2 2 5 2 2 4 2 2 4 2 2 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 2 2 4 2 2 4 2 2 4 2 2 4 2 2 4 2 2 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 2 2 2 4 2 2 2 2 2 2 2 2 2 4 2 2 2 6
      6 2 2 2 2 2 4 2 2 4 2 2 4 2 2 2 2 2 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 6
      6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
102 0  -51 50 -53 52  lat=1 u=22 imp:n=1
     fill=-9:9 -9:9 0:0
      6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 3 3 3 3 3 4 3 3 4 3 3 4 3 3 3 3 3 6
      6 3 3 3 4 3 3 3 3 3 3 3 3 3 4 3 3 3 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 3 3 4 3 3 4 3 3 4 3 3 4 3 3 4 3 3 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 3 3 4 3 3 4 3 3 5 3 3 4 3 3 4 3 3 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 3 3 4 3 3 4 3 3 4 3 3 4 3 3 4 3 3 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 3 3 3 4 3 3 3 3 3 3 3 3 3 4 3 3 3 6
      6 3 3 3 3 3 4 3 3 4 3 3 4 3 3 3 3 3 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6
      6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
c ----- Core lattice (u=100), pitch 21.50364, 17x17 assemblies -----
200 0  -71 70 -73 72  lat=1 u=100 imp:n=1
     fill=-9:9 -9:9 0:0
       6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6
       6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6
       6  6  6  6  6  6 20 20 20 20 20 20 20  6  6  6  6  6  6
       6  6  6  6 21 21 21 21 21 21 21 21 21 21 21  6  6  6  6
       6  6  6 21 21 21 21 21 21 21 21 21 21 21 21 21  6  6  6
       6  6 20 21 21 21 21 21 21 21 21 21 21 21 21 21 20  6  6
       6  6 20 21 21 21 22 22 22 22 22 22 22 21 21 21 20  6  6
       6  6 20 21 21 21 22 22 22 22 22 22 22 21 21 21 20  6  6
       6  6 20 21 21 21 22 22 22 22 22 22 22 21 21 21 20  6  6
       6  6 20 21 21 21 22 22 22 22 22 22 22 21 21 21 20  6  6
       6  6 20 21 21 21 22 22 22 22 22 22 22 21 21 21 20  6  6
       6  6 20 21 21 21 22 22 22 22 22 22 22 21 21 21 20  6  6
       6  6 20 21 21 21 22 22 22 22 22 22 22 21 21 21 20  6  6
       6  6 20 21 21 21 21 21 21 21 21 21 21 21 21 21 20  6  6
       6  6  6 21 21 21 21 21 21 21 21 21 21 21 21 21  6  6  6
       6  6  6  6 21 21 21 21 21 21 21 21 21 21 21  6  6  6  6
       6  6  6  6  6  6 20 20 20 20 20 20 20  6  6  6  6  6  6
       6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6
       6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6
c ----- Core barrel, RPV shells, graveyard -----
c The axial planes close the deck: without 90 -91 every cell below is infinite
c in z, which makes any volume-divided tally a fatal error.
300 0          -80    90 -91  fill=100  imp:n=1   $ core region (lattice)
301 6 -0.74    80 -81 90 -91            imp:n=1   $ core barrel inner water
302 5 -6.55    81 -82 90 -91            imp:n=1   $ core barrel
303 6 -0.74    82 -83 90 -91            imp:n=1   $ downcomer water
304 5 -6.55    83 -84 90 -91            imp:n=1   $ RPV
305 0          84 : -90 : 91            imp:n=0   $ graveyard

c ===================== SURFACES =====================
1  cz 0.39218
2  cz 0.40005
3  cz 0.4572
4  cz 0.56134
5  cz 0.60198
6  cz 0.43688
7  cz 0.48387
8  cz 0.56134
9  cz 0.60198
50 px -0.63
51 px  0.63
52 py -0.63
53 py  0.63
70 px -10.75182
71 px 10.75182
72 py -10.75182
73 py 10.75182
80 cz 187.96    $ core barrel inner
81 cz 193.675   $ core barrel outer
82 cz 219.150   $ RPV liner
83 cz 219.710   $ RPV inner
84 cz 241.300   $ RPV outer
c axial active-fuel planes set the preview height
90 pz -182.88
91 pz  182.88

c ===================== DATA =====================
mode n
m1  92235.80c 0.01600 92238.80c 0.98400 8016.80c 2.0     $ UO2 1.6 wt%
m3  92235.80c 0.02400 92238.80c 0.97600 8016.80c 2.0     $ UO2 2.4 wt%
m4  92235.80c 0.03100 92238.80c 0.96900 8016.80c 2.0     $ UO2 3.1 wt%
m2  2004.80c 1.0                              $ helium
m5  40090.80c 0.5145 40091.80c 0.1122 40092.80c 0.1715   $ Zircaloy-4
     40094.80c 0.1738 40096.80c 0.0280
c Borated water at 975 ppm B by weight (BEAVRS cycle-1 HZP soluble boron).
c Atom fractions per 1 mol H2O: 975/10.811 mol B against 999025/18.015 mol H2O
c gives B/H2O = 1.6265e-3, split 19.9/80.1 at% between B-10 and B-11.
m6  1001.80c 2.0 8016.80c 1.0 5010.80c 3.237e-4 5011.80c 1.3028e-3  $ borated water
mt6 lwtr.20t
m7  7014.80c 0.78 8016.80c 0.21 18040.80c 0.01 $ air
kcode 10000 1.0 50 250
ksrc 0 0 0
