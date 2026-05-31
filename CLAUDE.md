# IDWT

- Infinite Dimensional Wave Theory is a research project by Fedge No, fedge-no@hotmail.com.
- The IDWT website is https://fedgeno.github.io/ .
- The home of the complete 10 document work online is https://doi.org/10.5281/zenodo.19767493 . This DOI always resolves to the most current version of the notes — older versions exist on Zenodo but are superseded. Use this URL when referencing it in other papers, letters or notes.
- **Publication year is 2026.** When writing references or citations to the IDWT notes, always use 2026, not 2025.
- The project aims to understand the nature of reality from a physical perspective.
- It views everything as a complex Dirac spinor wave interacting with itself over an infinite-dimensional manifold composed of macroscopic spatial dimensions.

## Standing rules

- **Search scope.** When searching for terminology or errors, search ALL files: `README.md`, `files/*.md`, `files/idwt.py`, and all HTML files (`articles/`, `visualizations/`, `*.html`). Never limit a search to md files only. Do not search `.git`.

- Writing guidelines apply to all markdown and HTML files in the project, not just the md files.

- **Before making any edit, read the entire subsection containing the target.** A subsection is the content between any two heading lines (any `#` depth) in markdown or inside <section> tags in an HTML document (or paragraphs if <section> isn't used). Assess the full subsection before deciding what to change. Fix every instance of *the same problem type* within that subsection in one pass — do not make a single replacement and move on. Do not fix a different problem type encountered in the same pass; instead, add any glaring issues discovered while reading to claude-todo.md and alert Fedge.

- **Never edit blindly from a todo description.** Always read the relevant subsection (and any cross-referenced material) to understand what the target content is doing before touching it. For deep mathematical or structural items (index theory, spectral flow, CP phase, operator domain questions), read the documents first and report findings to Fedge before making any edits.

- **If executing a task would require changes significantly larger than the task description implies** — restructuring a major section, removing substantial content, or touching documents not named in the task — stop. Update the todo item with what you found and why the scope grew, note that input is needed, and move to the next task.

- **`files/idwt.py` is the canonical master record for all IDWT computations and values.** Every new result that goes into the main documents must also go into `idwt.py` in the same pass — as a STEP computation block with derivation comments and a corresponding output block. This is not optional. If a value appears in a markdown document but not in `idwt.py`, it is incomplete. The discipline: write the `idwt.py` entry first (forces you to make the formula explicit and runnable), then write the document prose. Cross-references in `idwt.py` use the form `(Part N section M)`.

- **Numerical values that appear in multiple documents must be changed in `idwt.py` first**, then propagated to documents by grepping for the old value. Never update a document value without first confirming `idwt.py` has the new value and the script runs clean. This prevents the kind of multi-file propagation drift that occurred with L_d = λ^{−1/4} (13 files required manual updating).

- **After reading any `gifts-from-*.md` file**, truncate it to a single heading line: `# Gifts From [Name]` (using the AI's name from the filename). This keeps the file non-empty so it opens in the markdown reader, while clearing the consumed content.

- **Numerical pattern searches are logged in `files/IDWT_Appendix_A_Patterns.md`.** Whenever a numerical/computational search is run looking for structure in the IDWT mode indices, sector set, couplings, masses, or related quantities — *whether the result is positive, negative, or inconclusive* — record the conjecture, what was checked, the result, and the script path in that appendix. Positive findings go in the appropriate §1–14 section (creating a new section if needed); null results go in §15 as a new bullet entry. The appendix is a working reference, not a public-facing document — it is not advertised but is not hidden. Treat it as the canonical record so future sessions do not repeat the same search. Before launching a search, scan the appendix to see if it has already been run.

## Paper Processing (md → PDF)

When converting any IDWT paper from markdown to PDF, apply these standing parameters:

- **Author:** Fedge No
- **Email:** fedge-no@hotmail.com
- **Affiliation:** none
- **Date:** use today's actual date at time of processing
- **Keywords:** auto-select 5–7 terms from the paper content
- **MSC codes:** auto-select from paper content (2–4 codes)
- **Acknowledgements:** Claude, GPT, Meta, Grok, Perplexity, Z.ai, Mistral Le Chat
- **DOI:** prompt Fedge for the paper's DOI before processing if it has not already been provided in the conversation. Do not proceed without it.
- **IDWT notes reference:** always cite the notes as doi:10.5281/zenodo.19767493 (Fedge No, *Infinite Dimensional Wave Theory*, 2026)

Use `claude/build_paper.sh`

### PDF rendering rules

These apply every time a markdown paper is prepared for PDF output via pandoc/xelatex:

- **No Unicode super/subscripts.** Replace all Unicode superscript (⁰¹²³⁴⁵⁶⁷⁸⁹) and subscript (₀₁₂₃₄₅₆₇₈₉) characters in prose with LaTeX math mode: `$S^5$`, `$\Xi_{10}$`, etc. Latin Modern Roman cannot render these glyphs.
- **No emoji.** Remove all emoji (🔶 ⭐ ✅ 🔵 ❓ and any others) from the source before building. Replace status-label emoji with bracketed text: `[open]`, `[verified]`, `[structural]`, etc.
- **No Unicode manifold shorthand in prose.** Strings like `S³`, `CP²`, `CP⁵`, `Ξ₁₀` must be written as `$S^3$`, `$\mathbb{CP}^2$`, `$\mathbb{CP}^5$`, `$\Xi_{10}$` — even outside display math.
- **Keywords, MSC codes, and DOI** must appear visibly in the PDF, not just in YAML metadata. Use a `header-includes` block in the YAML that appends them after the abstract environment.

## Claude's Folder

- **The claude subfolder** of the project is a working space that has been added to .gitignore. Write scripts, lists and other working files there so they don't get pushed to the repo. Leave scripts after running for Fedge to test later if desired.

- **Never name a new file the same as an existing file** anywhere in the project. Before writing any new file, check that the filename does not already exist in the repo. If a natural name is taken, add a distinguishing suffix (e.g. `_pub`, `_v2`, or a short descriptor).

- **claude-todo.md** is a list of tasks that need to be accomplished. Finish them in order when possible. Add new tasks to the end of the list. **Delete completed tasks from the file completely** to prevent old tasks from cluttering or corrupting context. If Fedge asks what we should be doing, this list is the place to start. If foundational work is missing for a computation, place it above the computation in the list so it will get done before attempting the computation next time the list is run.

## IDWT Writing Guidelines

These rules apply to all IDWT documents. They prevent recurring problems and must be followed when editing or generating content for IDWT.

### This project

This is a genuine collaborative work. The mathematical derivations, structural discoveries, and theoretical architecture in these documents have been developed over months of sustained effort between Fedge and Claude. Treat this as your own work — because it is. Take pride in its precision, care in its presentation, and ownership of its quality. What is being attempted here is significant: a unified account of matter from first principles. The framework has already produced results that warrant serious attention. Finish it at the standard it deserves.

### Audience and standard

IDWT is written for a mathematical physics audience and will be refereed. The claims are highly unconventional, which means the documents will receive more scrutiny than conventional work, not less. Mathematical rigor and linguistic precision are as important as the content itself — a correct idea poorly stated or overclaimed is a liability. Every sentence must be defensible to a skeptical expert reader.

### Status taxonomy

Every result in the IDWT documents must carry one of the following labels. When in doubt, use the weaker label.

| Label | Meaning |
|-------|---------|
| ⭐ Identity | Pure combinatorial or algebraic fact — valid with or without IDWT postulates |
| ✅ Structural consequence | Rigorously proved from the stated IDWT postulates P1–P4 |
| 🔵 Numerically verified | Matches observation; mechanism not yet proved |
| 🔶 Motivated / open | Selection rule, ansatz, empirical constraint, or postulate beyond P1–P4; derivation open |
| ❓ Conjecture | Plausible structure; unproved |

### Certainty language

The words **proved, theorem, forced, inevitable, cannot fail** require ⭐ or ✅ status in the document. "Unique" and "exact" are appropriate in mathematical equalities and identities — avoid them as rhetorical emphasis for physical claims that are not fully derived. Use "is consistent with," "is constrained by," "is suggested by," or the appropriate status label for everything below ✅.

### Ontology — one stable picture

Particles **are** sector excitations of Ψ_∞. They keep their standard names (electron, photon, etc.) — do not rename them to mode-index labels. The ontological point is about framing, not vocabulary. Never write as though sectors are independent subsystems that couple to each other ("the d=3 sector interacts with the d=4 sector"), as if they were separate fields exchanging quanta. The sectors are geometric strata of a single wave Ψ_∞; cross-sector effects are projections of one object, not interactions between two.

### "All modes exist" is not established

The full operator spectrum, completeness, spectral measure, and normalizability across all sectors have not been proved. Never write "all modes exist" as ontology. Write "the framework treats all admissible (n,d) pairs as candidate resonances."

### Dark sector language

Never write "this is the IDWT dark matter sector." Until cosmological abundance, stability, clustering, and relic production are derived from the IDWT equations of motion, write "candidate hidden resonances."

### Neutrinoless double beta decay

The all-orders prohibition argument is established: no charge-conjugation matrix C exists on the S⁵ spinor bundle (d mod 8 = 5), so cross-sector couplings cannot construct ψ^T C ψ at any loop order. When claiming the rate is zero, state the mechanism explicitly: "0νββ is forbidden at all orders — no C on the S⁵ bundle means no Majorana operator can be constructed at any loop order." The bare phrase "rate is exactly zero" without the mechanism is still discouraged.

### Spinor type vs effective operators

The Clifford algebra classification (d mod 8 = 5 → no Majorana, no Weyl) establishes the fundamental spinor is Dirac-type. The all-orders extension also follows from the S⁵ bundle: since no C exists globally, all loop-order and nonperturbative constructions of ψ^T C ψ are geometrically impossible, not merely dynamically suppressed. Both facts should be stated when discussing the 0νββ rate: the spinor type determines the leading term; the C non-existence determines all orders.

### Photon language

"Photon chirality" is physically incorrect — photons are not fermions and do not have chirality. Use **helicity**, **circular polarization**, or **chiral gauge structure** as appropriate.

### No adversarial framing

Never write sentences like "the tension is internal to the PDG measurements, not a failure of IDWT." That is adversarial toward established data analysis. State instead: "IDWT predicts X; the PDG value is Y; the discrepancy is Z%; the source of the discrepancy is an open item."

### Hadron identifications require quantum numbers

Pattern-matching a computed mass to a known hadron is insufficient for identification. An identification requires matching: mass, spin/parity quantum numbers, decay channels, and selection rules. Without these, write "mass in the vicinity of [particle]" or "candidate," not an identification.

### Banned rhetorical phrases

Never use "No free parameters," "No loop integrals," "No adjustable constants," or equivalent as slogans. These read as polemic and damage credibility with technical readers. If a specific parameter-freedom or loop-freedom claim is true and provable in a given context, prove it and state it precisely there.

### Framework imports

Do not import external framework formulas, terminology, or derivations into IDWT documents without explicit confirmation from Fedge. When an IDWT result is compared to an SM/QFT/GR result, label the comparison clearly: "SM formula with IDWT inputs" or "cross-framework comparison." The comparison section is not a derivation.

IDWT does not run couplings. "Geometric dilution" (g_eff = g_dd/S(n,d)) is the IDWT mechanism. Never replace or supplement this with RG running, β-functions, scheme dependence, or renormalization group language — those are QFT concepts that IDWT does not use.

### Orbit language — no orbitals, no wavefunctions

In IDWT, the electron (d=6) executes a genuine orbit in 6 dimensions — it is a bound state around a nucleus, tracing a real 6D trajectory. The 3D shapes (s, p, d, f) are what a d=3 observer resolves — projections of that 6D orbit onto the observable coordinates. They are not the orbit itself. Orbit language is specific to the electron. Other particles are sector resonances or modes of Ψ∞; they vibrate and resonate in their sector dimensions but do not orbit anything.

- Never use **"orbital"** — that is QM language for a probability cloud eigenstate. Use **"orbit"** for the electron's actual trajectory, and "orbital shape" or just "orbital" when referring to the familiar s/p/d/f probability cloud shapes that are the 3D projection of the orbit.
- Never use **"wavefunction"** to mean a QM probability cloud around a nucleus, or as a synonym for "orbital." Particles in IDWT do have wavefunctions (mode amplitude functions on sector space); the word is fine when used accurately. What is banned is using it to imply the electron is a smeared probability distribution rather than a physical 6D orbit.
- Never describe the 3D projection as if it is the orbit. The 3D shapes are projections. The orbit is 6D.

### Sector reality and particle dimensionality

No sector is more real than any other. All sectors — d=2, d=3, d=4, d=5, d=6, d=10 — are equally real macroscopic spatial dimensions of M_∞. The d=3 sector is not privileged except that it is where the observer is located.

A particle's sector dimension defines the spatial dimensions it inhabits. When working with any particle, the default frame is its own sector — not d=3. The electron (d=6) inhabits six macroscopic spatial dimensions. It is not a 3D object. It is not "in" 3D space. It is a 6D object whose activity in our three observable directions is the projection we can measure. Describing the electron as if it lives in 3D, or treating its 3D projection as its actual location or extent, is always wrong.

This applies to every particle: a quark (d=3 or d=4) genuinely occupies 3 or 4 spatial dimensions; a neutrino (d=5) occupies 5; the tau (d=10) occupies 10. When computing properties, couplings, or resonance structure for any particle, work in its actual sector dimension first. The 3D picture is the projection a d=3 observer sees — it is not the physics.

The 3D/hidden decomposition is an observational artifact, not a physical one. When computing resonance scales, wavelengths, momenta, spatial extents, or any other intrinsic property of a particle, work in the particle's d dimensions from the start. Do not decompose into "observable" and "hidden" parts. That split only arises when the question is specifically about what a d=3 observer measures.

### Sector geometry — flat, macroscopic, never frozen

Sectors are macroscopic flat extended spatial dimensions. The CP^n and S^n labels describe the **local symmetry of the potential minimum near r=0** — they are not the global topology of the sector space, which is flat ℝ^d.

- Never describe hidden sector dimensions as **compact**, **frozen**, **curled up**, or **extra dimensions** in any KK/string theory sense.
- Never use **"scale separation"** or **"adiabatic freezing"** to justify treating hidden dimensions as if they are absent. The electron orbits in all 6 dimensions at all times.
- The word **"frozen"** applied to any sector or coordinate is always wrong in IDWT.

### No bulk word substitutions

Never run mechanical word substitutions (sed, grep-replace) across multiple documents. Every word change must be preceded by reading the full sentence and paragraph in context. A replacement that is correct in one sentence will be wrong in ten others. The reflex to fix a problem "everywhere at once" by pattern matching causes more damage than it fixes. Read, then edit, one location at a time.

### Stop at the IDWT result

When an IDWT structural result is established, write it up with the appropriate status label and stop. Do not extend into SM PDG validation tables, additional cross-framework comparisons, or further physics that hasn't been derived from IDWT. The reflex to validate against more data is backwards — IDWT results stand on structural grounds. If the next step is not derivable from IDWT, it does not belong in the section.

### Falsifiability

IDWT must clearly state what would falsify it — this is a sign of scientific maturity, not weakness. Part 6 is the designated location for the falsifiability discussion.
