# Agent Audit Instructions - ICHEP 2026 MH Validation

## Purpose
This packet enables an independent agent or auditor to verify the terrain contact
assessment for MH_PREDICTION_04 against ICHEP 2026 experimental results.

## What to Verify

### Step 1: Confirm sealed prediction provenance
Read: 01_SEALED_PREDICTION/prediction-record.md
Verify: The numerical values in source-csv-rows.txt match the canonical values in
the prediction-record.md, Sections IX through XI.

### Step 2: Verify terrain sources exist
Read: 02_TERRAIN_MANIFEST/manifest.csv
For each arXiv item, confirm the paper exists at the listed URL and that the abstract
matches the attributed claim in the corresponding pathway ledger.

Critical check items:
- T2 arXiv:2607.23352: Confirm abstract says "first constraint on Higgs self-coupling
  in the off-shell region"
- T3 arXiv:2607.26879: Confirm mu_HH = 2.6 +1.4/-1.0 and kappa_lambda [-3.4, 1.6]
- T12 arXiv:2606.30903 v2: Confirm "first 2sigma detection" and Smv = 100+40/-50 meV
- T14 arXiv:2607.24742: Confirm three routes and Smv < 152 meV (dark-energy-marginalized)
- T20 arXiv:2607.21952: Confirm "consistent with linear QCD potential" + "confining force"

### Step 3: Run the scorer
Execute: python 04_EXECUTABLE_SCORER/residual_calc.py
Compare output to: 08_REPLICATION_CHALLENGE/expected-output.txt
All numeric values must match within floating-point precision.

### Step 4: Verify declared P4 falsifiers are tested and not activated
The declared P4 falsifiers test: (a) the absolute mass sum Smv, and (b) whether a
robust lower bound on the individual lightest mass is produced above 2.61 meV.

These are tested by T12 (arXiv:2606.30903 v2) and T14 (arXiv:2607.24742):
- T12 detection band [50, 140] meV at 1-sigma: Smv=60.47 is inside. Falsifier (a) NOT ACTIVATED.
- T14 dark-energy-marginalized bound 152 meV: 60.47 < 152. Falsifier (a) NOT ACTIVATED.
- No source produces a robust lower bound above 2.61 meV. Falsifier (b) NOT ACTIVATED.

T13 (arXiv:2607.19340) is an oscillation-splitting paper. It is not the instrument
for testing the declared P4 falsifier forms. The declared falsifiers were tested
by T12 and T14 and were not activated.

### Step 5: Verify falsifier adjudication
Read: 06_FALSIFIER_ADJUDICATION/adjudication-sheet.html
Each pathway lists the declared falsifier form from the sealed document (read from
01_SEALED_PREDICTION/prediction-record.md) and the adjudication result.
Confirm no declared falsifier was activated.

## Audit Sign-off
If all five steps pass without discrepancy, enter:
  AUDIT RESULT: CONFIRMED
  DATE: [your date]
  AUDITOR: [your identifier]

UMtts Institute | Thomas Russell Giboney, Founder
TRUTH > COMFORT. Always.
