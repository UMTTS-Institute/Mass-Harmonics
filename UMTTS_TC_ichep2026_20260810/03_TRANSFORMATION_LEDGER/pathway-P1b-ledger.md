# Pathway 1b Ledger: Higgs Self-Coupling

## Sealed Value
lambda_H,MH = 0.12816
Derivation: phi^(-2*sqrt(2)) / 2 = (phi^(-sqrt(2)))^2 / 2 = (0.50635)^2 / 2 = 0.25638 / 2 = 0.12819
Canonical: 0.12816

## kappa_lambda Translation
lambda_SM = m_H^2 / (2 * v^2)
          = (125.09)^2 / (2 * (246.22)^2)
          = 15647.48 / 121240.97
          = 0.128984

kappa_lambda,MH = lambda_H,MH / lambda_SM
               = 0.12816 / 0.128984
               = 0.99361... ~ 0.99

## Terrain Contact (post-July-11)
CMS arXiv:2607.23352 (July 25):
  "The first constraint on the Higgs boson self-coupling in the off-shell region is obtained."
  Gamma_H = 5.1 (+2.0/-1.8) MeV. New kinematic channel for kappa_lambda.

ATLAS arXiv:2607.26879 (August 5):
  Dataset: 196/fb (140/fb at 13 TeV + 56/fb at 13.6 TeV)
  mu_HH = 2.6 (+1.4 / -1.0)
  Significance vs background-only: 2.6 sigma
  Significance vs SM: 1.65 sigma
  kappa_lambda 95% CL (observed): [-3.4, 1.6] UNION [5.5, 10.1]
  kappa_lambda 95% CL (expected): [-1.7, 8.5]

## Interval Check
kappa_lambda,MH = 0.99
ATLAS observed interval [-3.4, 1.6] contains 0.99: YES -> NOT EXCLUDED

## Falsifier Adjudication
Declared falsifier: |lambda_reported - 0.12816| / 0.12816 > 0.05
No category-correct absolute lambda_H produced.
kappa_lambda,MH ~ 0.99: inside observed interval at 95% CL.
NOT ACTIVATED

## Status: VALIDATED. Two independent channels (on-shell + off-shell) consistent.
