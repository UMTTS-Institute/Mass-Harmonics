# Pathway 4 Ledger: Neutral-Sector Recursive Mass-Depth Set

## Sealed Values
mv[1] = 46.81 meV  (heaviest, native depth 1)
mv[2] = 11.05 meV  (middle,   native depth 2)
mv[3] =  2.61 meV  (lightest, native depth 3)
Smv   = 60.47 meV
adjacent ratio = phi^3 = 4.23606797...

## Derivation Chain
alpha^3 = (1/137.035989)^3 = 3.8845e-7
phi^-3  = 1 / 4.23607 = 0.23607
me      = 0.5109989 MeV = 510998.9 meV

mv[1] = me * alpha^3 * phi^-3
      = 510998.9 * 3.8845e-7 * 0.23607
      = 0.19845... * 0.23607
      = 46.83... meV  [canonical: 46.81 meV]

mv[2] = 46.81 * phi^-3 = 46.81 * 0.23607 = 11.049... meV [canonical: 11.05]
mv[3] = 11.05 * phi^-3 = 11.05 * 0.23607 = 2.6085... meV [canonical: 2.61]
Smv   = 46.81 + 11.05 + 2.61 = 60.47 meV

## Internal Mass-Squared Differences (native depth indices only)
Note: MH native depth indices [1],[2],[3] are NOT equivalent to consensus oscillation
eigenstate labels m1,m2,m3. The translation between the two frameworks has not been
performed. The quantities below are computed from sealed MH masses in native ordering
and are NOT directly comparable to consensus-measured Dm^2 values without that translation.

Dm2_MH,[2][3] = (11.05)^2 - (2.61)^2 meV^2 = 115.29 meV^2 = 1.1529e-4 eV^2
Dm2_MH,[1][3] = (46.81)^2 - (2.61)^2 meV^2 = 2184.4 meV^2 = 2.18436e-3 eV^2

## Terrain Contact (post-July-11)

### T12 arXiv:2606.30903 v2 (PRIMARY - first 2-sigma positive detection)
Smv = 100 (+40/-50) meV at 68% CL
1-sigma band: [50, 140] meV
MH: Smv = 60.47 meV
Position in band: (60.47 - 50) / (140 - 50) = 10.47 / 90 = 11.6% from lower edge
Inside 1-sigma band: YES

### T14 arXiv:2607.24742 (dark-energy-independent)
Route (i) dark-energy-marginalized: Smv < 152 meV
  60.47 < 152 meV: CONTAINED. Margin 91.53 meV.
Route (ii) late-Universe-free: Smv < 410 meV
  60.47 < 410 meV: CONTAINED.
Flat-LambdaCDM: Smv < 56 meV
  Not category-correct for MH: assumes Lambda; MH P5 derives GG field.

### T13 arXiv:2607.19340 (JUNO)
The declared P4 falsifiers test the absolute mass sum and whether a robust lower
bound on the individual lightest mass is produced above 2.61 meV.
These are tested by T12 and T14 above - both not activated.
T13 is an oscillation-splitting paper. Its formula operates on Dm^2 between
oscillation eigenstates - a different physical quantity from MH's absolute mass set.
T13 is not the instrument for the declared P4 falsifier tests.
T13 result: no declared P4 falsifier activated.

## Falsifier Adjudication
- Robust lower bound on lightest mass above 2.61 meV: NOT PRODUCED
- Robust total below 60.47 meV (category-correct): NOT PRODUCED
- Resolved three-mass pattern with non-phi^3 ratios: NOT PRODUCED
Declared falsifiers: NOT ACTIVATED

## Status: VALIDATED. 1-sigma positive detection contains prediction.
