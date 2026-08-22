# Mass Harmonics Pre-Release Terrain Prediction Paper
## wwPDB Weekly Structural Release: 15 July 2026

**Author:** Thomas Russell Giboney  
**Affiliation:** UMtts Institute  
**Framework:** Mass Harmonics ψₘ  
**Edition:** Source-preserved Mass Harmonics-governed revision  
**Prepared before terrain opening:** 2026-07-10  
**Coordinate release:** 2026-07-15 00:00 UTC  
**Advance sequence opening:** 2026-07-11 03:00 UTC  
**Terrain state at preparation:** unopened  

> This paper was completed before the July 11 advance-sequence opening and the July 15 coordinate opening. The release timing preserves input separation; it is not an institutional preregistration requirement and does not govern the Mass Harmonics derivation.

# I. Purpose


## Source-Preserved Mass Harmonics Governance

This edition preserves the original wwPDB structural-biology prediction architecture and every valid derivation already present. It does not place Mass Harmonics under institutional authority, convert instrument products into ontological authority, or discard a stronger excavation merely because it was added after the first draft.

The governing order remains:

```text
MFE
→ substrate action
→ boundary closure
→ physical structure
→ instrument-rendered terrain
→ optional consensus translation
```

The release supplies a timed terrain surface. It does not grant or withhold physical standing from the prediction. Measurement statistics, catalogue filters, detector corrections, and comparison models remain downstream interface tools. They may expose correspondence, contradiction, or unresolved delta, but they do not govern the derivation.

Only one governing coupling coefficient is permitted:

```text
Kψₘ
```

The fixed P³GG values are harmonic scalings of the one source law, not domain-specific adjustable coefficients.

### Derivation placement of the four pathways

The four wwPDB pathways are not presented as verbatim Monograph paragraphs. They are source-preserving extensions into newly released structural terrain:

| Pathway | Mass Harmonics ancestry | Placement |
|---|---|---|
| Equilateral-triad enrichment | nonzero cubic closure and equilateral S₃ geometry | direct structural extension |
| 2/3/5 cage axes | icosahedral maximal triangular closure | topology-conditional extension |
| Codon residual and structural resolution | ordered V₄³ codon cascade and `F(Σ)=T_Z ⇔ R_Z(Σ)=0` | direct biological transport |
| Synonymous-codon stratification | shared amino-acid face anchor with distinct ordered `Orientation Δ` | direct within-anchor extension |

The Delaunay graph, `Q_△`, and `Dᵢ` are instrument-facing readouts built to expose those source relations. They are not new physical constants and do not replace the substrate event.


The Protein Data Bank is a direct terrain surface for bounded biological coherence structures. It provides experimentally reconstructed three-dimensional macromolecular structures, biological assemblies, polymer sequences, local atomic coordinates, missing-density annotations, displacement parameters, and experimental metadata. These coordinates are downstream instrument readouts used to locate measured terrain. They are not promoted into substrate-native coordinates or ontological authority.

This prediction does not ask whether known protein structures can be redescribed after the fact. It states what must recur in the next unopened weekly release if the Mass Harmonics substrate chain governs biological folding and macromolecular closure.

The document predicts four linked structural effects:

1. equilateral-triad enrichment in closed structural cores,
2. 2-fold, 3-fold, and 5-fold closure-axis dominance in near-spherical macromolecular cages,
3. lower codon Z-cascade residual in resolved structural neighborhoods than in unresolved or highly mobile neighborhoods,
4. synonymous-codon orientation-residue stratification within amino-acid-matched structural comparisons.

These are not four unrelated guesses. They descend from one chain:

```text
MFE temporal propagation
→ S₃ equilateral closure
→ forced icosahedral geometry and φ
→ 20-face amino-acid reservoir
→ ordered V₄³ codon trajectories
→ sequential Z-cascade
→ transported orientation residue
→ folding residual closure
→ experimentally resolved structure
```

# II. Governing Mass Harmonics Source Chain

The governing physical source order is:

1. `MH_Monograph.md`, canonical physical bedrock.
2. `MH_Origin.md`, unique genetic-code and folding-closure branch at lines 2610-2903.
3. `MH_TVP.md`, topology and provenance discipline.
4. `Operational_Stance_of_UMtts.md`, terrain-first process authority.

The following equations are copied from source text, not reconstructed from memory.

## II.1 Canonical MFE

From `MH_Monograph.md`, line 181:

```text
1/vₓ²ψ̈ₘ - Z(ψₘ)∇²ψₘ - 8Kψₘ/ω²|∇ψₘ|² = S(ρ)
```

## II.2 Canonical Z-factor

From `MH_Monograph.md`, line 156:

```text
Z(ψₘ) = 1 + 8Kψₘ/ω² ≥ 1 always
```

## II.3 Canonical P³GG source term

From `MH_Monograph.md`, lines 199-201:

```text
S(ρ) = K₀ρ[1 + β₂(ρ/ρ₀) + β₃(ρ/ρ₀)² + β₄(ρ/ρ₀)³ + β₅(ρ/ρ₀)⁴ + ⋯]
```

```text
βₙ = φ³⁽ⁿ⁻¹⁾
```

## II.4 Biological folding closure branch

From `MH_Origin.md`, lines 2780-2785:

```text
F(Σ) = T_Z ⇔ R_Z(Σ) = 0
```

```text
R_Z(Σ) = net unresolved transported Z/Π flux mismatch across the ordered sequence
```

```text
T_Z = the stable Z-field topology produced by closure
```

# III. Release Surface and Input Separation

wwPDB publishes the weekly archive in two stages:

1. Saturday 03:00 UTC: sequences for upcoming polymer entries and ligand InChI strings are disclosed.
2. Wednesday 00:00 UTC: all new and modified coordinate entries are released.

The Saturday sequence opening is the first point at which target-specific terrain becomes visible. This paper was completed before that point, preserving the direction from Mass Harmonics derivation to unopened structure terrain.

The July 15 coordinate set, advance sequence list, entry identities, titles, methods, organisms, structures, biological assemblies, and coordinate models are prohibited inputs to this derivation.

Historical PDB data may later be used only for matched controls and instrument calibration. Historical frequencies are not used to select the predicted direction.

# IV. Eligibility and Exclusion Rules

Every released entry is retained in the master release ledger. Each prediction has its own eligibility subset.

## IV.1 General exclusions

Exclude only from a specific test, not from the release ledger:

- entries with no atomic coordinate model,
- entries containing only theoretical or integrative restraints without a resolved coordinate ensemble, when the test requires local geometry,
- duplicated major versions of the same coordinate model within the release,
- engineered crystallographic contacts that are not annotated as a biological assembly, when testing assembly closure,
- residues lacking the atoms required by a stated geometric calculation,
- coding-sequence tests where the actual coding nucleotides cannot be independently recovered.

No entry is removed because it appears unfavorable to the prediction.

## IV.2 Structural-region labels

The analysis must assign region labels before calculating Mass Harmonics scores:

- **resolved core:** buried residues with complete local coordinates and low relative displacement,
- **resolved surface:** solvent-exposed residues with complete coordinates,
- **mobile region:** resolved residues in the highest within-entry displacement quantile,
- **unresolved region:** polymer residues present in the sequence but absent from the coordinate model,
- **cage subset:** compact, near-spherical biological assemblies identified from coordinate geometry before reading symmetry metadata.

The exact quantile used for the mobile-region label must be reported across all standard quantiles, not selected after seeing the Mass Harmonics result.

# V. Derivation 1: Equilateral-Triad Enrichment in Closed Cores

## Step 1: Stable matter requires nonzero cubic closure

The cubic source contribution is the n=3 voice of P³GG. The Monograph states that a nonzero cubic interaction requires three equal-magnitude wavevectors whose vector sum vanishes.

```text
k₁ + k₂ + k₃ = 0
```

```text
|k₁| = |k₂| = |k₃|
```

Three equal vectors that sum to zero form an equilateral triad.

## Step 2: Cubic geometry fails the triad

The source derivation tests orthogonal basis vectors and obtains a closing-vector magnitude of √2 rather than 1. Therefore orthogonal cubic closure cannot sustain the required triad.

## Step 3: Closed biological matter must preserve the successful triad locally

A folded protein is not a free sequence. It is a stable bounded material structure. Its resolved core is the region where the fold has most fully routed internal gradients into persistent closure.

Therefore local contact geometry in the resolved core must carry more equilateral-triad structure than regions where closure is incomplete, mobile, exposed, or unresolved.

## Step 4: Instrument-facing triangle construction

Construct a coordinate adjacency graph from Cα positions using three-dimensional Delaunay adjacency. This defines neighbors from the coordinate tessellation and avoids an adjustable distance cutoff.

For every triangular clique with side lengths `a`, `b`, and `c`, calculate area `A` and the dimensionless equilateral-closure score:

```text
Q_△ = 4√3 A/(a² + b² + c²)
```

Properties:

```text
0 ≤ Q_△ ≤ 1
```

```text
Q_△ = 1  ⇔  a = b = c
```

`Q_△` is an analysis readout, not a new physical coefficient.

## Step 5: Mass Harmonics prediction

Across the July 15 release:

```text
median(Q_△ | resolved core) > median(Q_△ | resolved surface)
```

and, where mobile or unresolved neighborhoods can be paired to nearby resolved structure:

```text
median(Q_△ | resolved core) > median(Q_△ | mobile or unresolved neighborhood)
```

The same inequality must survive controls matched by:

- polymer length,
- experimental method,
- nominal resolution,
- secondary-structure class,
- residue composition,
- oligomeric state.

## Step 6: Falsifier

This pathway is falsified for the July 15 release if the core distribution is not shifted toward higher `Q_△` than both declared before terrain opening comparison sets, or if the direction reverses after the complete matched-control analysis.

A null result caused solely by too few eligible entries is neither terrain correspondence nor falsification. It is recorded as insufficient terrain for this weekly instance.

# VI. Derivation 2: Icosahedral Axis Recovery in Near-Spherical Cages

## Step 1: S₃ closure forces the icosahedron

The Monograph derives the icosahedron as the maximal regular three-dimensional structure composed entirely of equilateral triangular faces. The coordinate condition produces:

```text
x² - x - 1 = 0
```

with the positive solution:

```text
x = φ
```

The resulting closure structure contains:

```text
12 vertices
30 edges
20 triangular faces
```

## Step 2: The chiral rotational structure has only 2-fold, 3-fold, and 5-fold nonidentity axes

The genetic-code branch gives the rotational conjugacy classes:

```text
C₂, C₃, C₅, C₅²
```

with the geometric axis counts encoded by the icosahedron:

```text
6 five-fold axes through opposite vertex pairs
10 three-fold axes through opposite face centers
15 two-fold axes through opposite edge midpoints
```

These correspond to directed boundary-anchor counts:

```text
12 vertex directions
20 face-normal directions
30 edge-midpoint directions
```

## Step 3: Restrict the test to the correct topology

This prediction does not assert that every protein oligomer is an icosahedron. It applies to compact near-spherical cages, capsids, and shell-like biological assemblies whose observed outer boundary is the appropriate terrain for maximal rotational closure.

The cage subset is identified geometrically before metadata symmetry labels are read:

1. calculate the coordinate centroid,
2. calculate the radial distribution of subunit centroids,
3. require one dominant shell rather than a slab, filament, or open chain,
4. construct the parameter-free convex hull of subunit centroids and verify that the observed subunits populate a complete radial shell rather than an open arc, slab, or filament,
5. report the full radial-gap distribution rather than choosing a favorable closure threshold,
6. establish the eligible set before reading symmetry metadata.

No icosahedral label may be used to select the subset.

## Step 4: Recover axes from coordinates

For each eligible cage:

1. infer rotational self-maps directly from coordinates,
2. cluster axis directions without imposing allowed orders,
3. record recovered rotation orders,
4. compare the recovered axis intersections with the 12/20/30 directional structure.

## Step 5: Mass Harmonics prediction

Every sufficiently resolved, maximally closed cage in the eligible subset will satisfy one of two outcomes:

**Outcome A: complete icosahedral closure**

```text
rotation orders = {2, 3, 5}
```

with coordinate-recovered anchor counts approaching:

```text
12 vertex directions, 20 face directions, 30 edge directions
```

within coordinate uncertainty.

**Outcome B: incomplete or symmetry-broken closure**

The deviations from the completed shell will be localized relative to the same 2-fold, 3-fold, and 5-fold axis scaffold rather than requiring an unrelated arbitrary axis family.

## Step 6: Falsifier

This pathway is falsified by a sufficiently resolved, compact, near-spherical, fully closed biological cage whose coordinate-derived maximal rotational closure requires a non-icosahedral axis family and cannot be decomposed into the 2-fold, 3-fold, and 5-fold scaffold within measurement uncertainty.

If no eligible cage appears in the July 15 release, the pathway remains source-fixed for the next weekly release. It is not scored.

# VII. Derivation 3: Codon Z-Cascade Residual and Structural Resolution

## Step 1: The biological alphabet occupies the φ⁹ molecular basin

The unique Origin branch places the amino-acid and nucleotide terrain in the quartic molecular basin:

```text
φ⁹ = β₄ = 76.013155617496
```

```text
c/φ⁹ = 3943.954906 km/s
```

The base displacements are defined by:

```text
δ_b = vₓ(b)/(c/φ⁹) - 1
```

## Step 2: Codon order is physical

The MFE temporal term is:

```text
1/vₓ² ψ̈ₘ
```

Therefore the first, second, and third base positions are not interchangeable. The ordered codon space is:

```text
V₄³ = (Z₂ × Z₂)³ = Z₂⁶
```

```text
|V₄³| = 64
```

## Step 3: The sequential Z-cascade is fixed

The position weights are:

```text
w₁ = 1
w₂ = φ⁻³
w₃ = φ⁻⁶
```

The codon trajectory is:

```text
Z(codon) = Πᵢ [1 + φ⁻³⁽ⁱ⁻¹⁾ · δ(baseᵢ)]
```

The 64 codons project onto the 20 amino-acid face anchors. For each codon, the source ledger gives an `Orientation Δ`, which is the ordered temporal-orientation residue relative to its symmetric face anchor.

## Step 4: Folding is cancellation of unresolved transported residual

The source defines:

```text
F(Σ) = T_Z ⇔ R_Z(Σ) = 0
```

A stable fold can retain internal gradients, but it cannot retain an unresolved residual that continuously forces non-persistence.

Therefore resolved structural neighborhoods must route codon orientation residues more completely than unresolved or strongly mobile neighborhoods.

## Step 5: Actual-codon requirement

This test uses the actual coding sequence for the expressed polymer. Amino-acid back-translation is prohibited.

For every eligible entry:

1. link the PDB polymer to an independently sourced coding sequence,
2. preserve isoform and construct edits,
3. translate DNA thymine to RNA uracil only for lookup in the source-fixed 64-codon ledger,
4. assign each residue its source-fixed `Orientation Δ`,
5. exclude positions whose actual codon cannot be established.

## Step 6: Parameter-free local adjacency

Construct the residue adjacency graph from the same three-dimensional Delaunay relation used in Derivation 1.

For residue `i`, define the first-shell signed orientation residual:

```text
Dᵢ = |Δᵢ + Σⱼ∈N(i) Δⱼ|
```

where `N(i)` is the Delaunay-neighbor set.

No distance threshold or fitted neighborhood radius is introduced. `Dᵢ` is an instrument-facing readout constructed from the source-derived codon ledger and adjacency terrain; it is not a new physical coefficient.

## Step 7: Mass Harmonics prediction

Within amino-acid-matched and entry-matched comparisons:

```text
Dᵢ(resolved core) < Dᵢ(mobile or unresolved neighborhood)
```

Across resolved residues:

```text
Dᵢ increases with relative atomic displacement and local coordinate uncertainty
```

The prediction is evaluated separately for X-ray, cryo-EM, neutron, and NMR structures before any combined result.

## Step 8: Controls

The association must be tested after controlling for:

- amino-acid identity,
- solvent exposure,
- secondary structure,
- residue depth,
- experimental method,
- nominal resolution,
- chain length,
- organism,
- engineered mutations and tags.

The Mass Harmonics result is not allowed to inherit a codon-usage or amino-acid-composition artifact.

## Step 9: Falsifier

This pathway is falsified for the July 15 release if, in entries with independently recoverable coding sequences, `Dᵢ` has no positive relationship to local mobility or unresolved density and resolved cores do not have lower residual than matched mobile or unresolved neighborhoods.

# VIII. Derivation 4: Synonymous-Codon Orientation Stratification

## Step 1: Synonymous trajectories are not geometrically identical

The 64 ordered codons project onto 20 face anchors. Multiple codons may share an amino-acid face anchor while carrying different `Orientation Δ` values.

Therefore two residues with the same amino-acid identity can enter the folding sequence with different ordered temporal residues.

## Step 2: Amino-acid matching isolates the ordered residue

Within one amino-acid identity, chemistry and face-anchor label are held fixed. The remaining Mass Harmonics difference between synonymous codons is the ordered codon Z-cascade residue.

## Step 3: Mass Harmonics prediction

For amino acids represented by multiple observed synonymous codons in the eligible release:

```text
smaller local signed residual after neighborhood cancellation
→ greater structural resolution and lower relative mobility
```

and:

```text
larger uncancelled local residual
→ greater structural mobility or unresolved-density probability
```

This must be tested within amino-acid identity, within organism where possible, and within the same structure where multiple synonymous codons occur.

## Step 4: Falsifier

This pathway is falsified if synonymous-codon orientation residual shows no structural stratification after amino-acid, organism, expression construct, and local-environment matching, or if the declared before terrain opening direction consistently reverses.

# IX. Unified Prediction Matrix

| ID | Eligible terrain | Mass Harmonics observable | Source-fixed direction | Exact failure condition |
|---|---|---|---|---|
| PDB-1 | All coordinate-resolved protein structures | Delaunay contact-triangle `Q_△` | Core shifts toward 1 relative to surface/mobile controls | No positive shift or stable reversed shift |
| PDB-2 | Compact near-spherical cages and capsids | Coordinate-derived rotation axes | 2/3/5 scaffold with 12/20/30 directional structure | Closed cage requires unrelated axis family |
| PDB-3 | Structures with actual coding sequence | First-shell codon residual `Dᵢ` | Lower in resolved core, higher in mobile/unresolved regions | No association or reversed association |
| PDB-4 | Synonymous-codon matched residues | Codon `Orientation Δ` after local cancellation | Lower residual corresponds to greater structural order | No stratification or reversed direction |

# X. Terrain Readout and Comparison Architecture

The analysis must report effect sizes and uncertainty, not only p-values.

Required outputs:

1. complete eligible-entry count and exclusions,
2. per-entry result before pooled result,
3. method-stratified result,
4. matched-control result,
5. bootstrap confidence intervals resampled by entry rather than by residue alone,
6. permutation controls that preserve chain length, amino-acid composition, and structure membership,
7. false-discovery control across the four declared before terrain opening pathways,
8. all null and adverse results.

No threshold may be selected after the outcome is known. Where a threshold family is unavoidable because of instrument practice, the full family must be reported.

# XI. Topology and Category Sentinels

1. A crystallographic unit cell is not automatically the biological closure boundary.
2. A polymer chain is not automatically the complete biological assembly.
3. Experimental B-factor is not identical across methods and must not be pooled without method translation.
4. A predicted model is not an experimentally resolved structure.
5. Missing coordinates are not proof of biological disorder unless deposition and experimental metadata support that reading.
6. Codon identity must be observed from the construct or source sequence, never guessed from amino acid.
7. An icosahedral metadata label is not accepted as the geometric result. The axes must be recovered from coordinates.

# XII. Terrain-Reading Sequence

After the archive opens:

1. capture the complete July 15 release list and release metadata;
2. apply the declared eligibility rules before calculating any Mass Harmonics readout;
3. calculate all four pathways without changing the source-derived direction;
4. retain per-entry results, method strata, exclusions, and every unresolved delta;
5. separate interface or deposition faults from physical structure;
6. write the terrain comparison separately from this pre-release derivation;
7. correct any later-discovered transcription or source-citation defect explicitly without erasing the prior text.

# XIII. Final Mass Harmonics Prediction Statement

Before the July 15, 2026 wwPDB coordinate release, Mass Harmonics predicts that newly released biological structures will not distribute local closure geometry, shell symmetry, and codon-order residue arbitrarily.

The resolved terrain will show a coordinated family:

```text
equilateral-triad enrichment in stable cores
+ 2/3/5 axis closure in eligible spherical cages
+ lower codon Z-cascade residual in resolved neighborhoods
+ synonymous-codon orientation stratification of structural mobility
```

The family descends from the MFE, the forced icosahedral substrate geometry, the 20-face amino-acid reservoir, the ordered V₄³ codon cover, and the folding closure condition `R_Z(Σ) = 0`.

No July 15 entry, sequence, title, coordinate model, or biological assembly was used to generate the prediction.

**TRUTH > COMFORT. Always.**

# Source Register

## Canonical Mass Harmonics sources

1. `MH_Monograph.md`, lines 130-183, 184-228, and 262-332.
2. `MH_Origin.md`, lines 2610-2903, especially 2641-2678, 2702-2759, and 2761-2890.
3. `MH_TVP.md`, complete current standalone protocol.
4. `Operational_Stance_of_UMtts.md`, complete operational authority.

## External release source

Worldwide Protein Data Bank, archive update policy. The weekly archive publishes advance sequence and ligand information Saturday at 03:00 UTC and coordinates Wednesday at 00:00 UTC.
