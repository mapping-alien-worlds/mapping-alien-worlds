# Technical Overview — Mapping Alien Worlds

**AI-Coordinated Space Optical Interferometry for Direct Imaging of Exoplanet Surfaces**

*Version 1.1 — Public technical summary*

---

## 1. Concept

Direct surface imaging of exoplanets requires angular resolution far beyond any single telescope. Our approach combines:

- **Distributed aperture**: 10–20 small satellites (first phase) in precision formation flight, forming an optical interferometer with baselines of 100–1000 km, operating in visible light (~500–550 nm)
- **Dynamic hierarchical nulling** (following Stankus, NIAC 2026): suppressing host-star light via hierarchical phase combination of multiple apertures, with starlight preserved in a separate beam as phase reference
- **AI-driven coordination and reconstruction**: autonomous swarm formation flight, OPD stabilization, and recovery of surface maps from extremely sparse uv-plane data

## 2. Resolution vs. Baseline (at ~1.3 pc, λ = 550 nm)

| Baseline | Surface resolution | What becomes visible |
|---|---|---|
| 1 km | ~25,000 km | Planet disk (unresolved) |
| 10 km | ~2,500 km | Hemispheric features |
| **100 km** | **~250 km** | **Continents, oceans, clouds, ice caps** |
| 1,000 km | ~25 km | Regional detail |

Target baseline: **~100 km** (consistent with the NASA NIAC 2026 study by Paul Stankus).

![Baseline vs resolution](../figures/fig1_baseline_resolution.png)

## 3. Photon Budget — Two Scenarios

A key subtlety: the Alpha Centauri system offers two very different physical regimes. All numbers below are first-order estimates (zodiacal/exozodiacal background, detector noise, and realistic phase curves not yet included).

### Scenario A — Alpha Cen A + hypothetical Earth-like planet (1.25 AU, 1.34 pc)

- Star: G2V, V = 0.01 → photon flux ~10⁸ ph/s/m² (V band)
- Planet/star contrast: ~1–2×10⁻¹⁰ → **photon-rich but null-limited regime**
- Requires nulling depth 10⁻⁸–10⁻¹⁰
- Budget example: 10 telescopes × 12.6 m² × 1000 h × efficiency ~0.1 → ~10⁷–10⁸ planet photons; SNR(20×20 px) ~260 at null 10⁻¹⁰, ~30–40 at 10⁻⁸

### Scenario B — Proxima Centauri b (real, known planet; 0.0485 AU, 1.30 pc)

- Star: M5.5V, V = 11.13 (~26,000× fainter than Alpha Cen A) → flux ~3.5×10³ ph/s/m²
- Planet is much closer in → contrast ~8×10⁻⁸ (**~760× better than Scenario A**)
- Planet signal: ~8–9 ph/hour (10 × 1 m apertures) → **photon-limited regime**
- Nulling requirement relaxes to ~10⁻⁶ — a major engineering advantage
- Trade-offs: star–planet separation only ~37 mas (vs ~930 mas in Scenario A), requiring a more aggressive inner working angle; long integrations needed for per-pixel mapping SNR. Detection SNR(24 h) ~13.

**Consistency rule**: narrative examples may use Proxima b (a real planet), but photon-budget numbers must always be tied to the correct scenario.

## 4. uv-Coverage and Image Reconstruction

- 10-satellite circular array → 45 baseline pairs; formation rotation yields ring-pattern super-synthesis
- Simulation (10 satellites, 100 km circle, 24 epochs): uv coverage only **~1.8%**
- The resulting "dirty image" is dominated by sidelobe artifacts — classical imaging fails
- Wiener-filter reconstruction already recovers continent/ocean structure; modern AI priors (diffusion models, compressed sensing) are expected to do substantially better
- This sparse-coverage result is the direct motivation for AI-based reconstruction at the core of the concept

![uv-plane simulation](../figures/fig2_uv_simulation.png)

*Left to right: ground-truth surface model, uv coverage (~1.8%), dirty image, Wiener reconstruction.*

## 5. Role of AI

| Task | Technique |
|---|---|
| Autonomous formation flight | Swarm reinforcement learning |
| Speckle suppression | Real-time CNN wavefront correction |
| OPD stabilization | Predictive control (LSTM) + micro-thrusters |
| Sparse image reconstruction | Diffusion models / compressed sensing |
| Closure-phase selection | Baseline-pair optimization |
| Observation strategy | Multi-objective optimization |
| Multi-epoch fusion | Temporal consistency networks |

## 6. Technology Readiness

| Technology | Status | Evidence |
|---|---|---|
| nm/pm metrology | Proven | LISA (in development), JWST |
| Radio VLBI | Proven | EHT (M87 black hole image) |
| Visible-light space interferometry | Not yet demonstrated | Core challenge |
| Space formation flight (10+ sats) | Not yet demonstrated | LISA = 3 sats (2030s); SILVIA (JAXA) demo |
| Visible-light nulling at 10⁻⁸–10⁻¹⁰ | Not yet demonstrated | Lab: ~10⁻⁶ |
| AI autonomous control | Emerging | LISA-related development |

## 7. Scientific Context

- **NASA NIAC 2026 Phase I** — Paul Stankus (Brookhaven Science Associates), *"Mapping Alien Continents: Achieving Optical VLBI for Exoplanet Imaging"*: dynamic hierarchical nulling, ~100 km baseline between nullers, Michelson imaging
- **LIFE** (Large Interferometer For Exoplanets, ETH Zürich) — mid-IR nulling formation-flying mission concept
- **SILVIA** (JAXA) — precision formation-flying technology demonstration

## 8. Phased Roadmap

| Phase | Timeframe | Goal |
|---|---|---|
| 0 — Concept | 2026–2027 | Open-source simulations, community building, NIAC-aligned studies |
| 1 — Technology | 2027–2035 | Ground-based nulling prototype, AI swarm algorithms, 2–4 sat LEO formation demo |
| 2 — Space proof | 2035–2045 | 3–6 satellites, nulling test, first planet signal |
| 3 — First image | 2045–2060 | 10–20 satellites, 100 km baseline, first surface map |
| 4 — High resolution | 2060+ | 100+ satellites, longer baselines |

## 9. Key Bottlenecks and Mitigations

| Bottleneck | Mitigation |
|---|---|
| Formation flight at scale | Build on LISA heritage, AI-based scaling |
| Visible-light nulling | Dynamic hierarchical nulling (Stankus approach) |
| Beam combination over 100 km | Laser links, starlight phase reference |
| OPD stabilization | AI predictive control, picometre metrology |
| Sparse uv coverage | AI reconstruction (diffusion priors, compressed sensing) |

## 10. Open Questions

- End-to-end photon budget including zodiacal/exozodiacal backgrounds and detector noise
- Achievable nulling depth in visible light beyond current lab ~10⁻⁶
- Inner working angle feasibility at ~37 mas (Proxima b)
- Benchmark: AI reconstruction (diffusion prior) vs. CLEAN/Wiener on realistic sparse data

---

*This document is a public technical summary intended for open collaboration. Contributions and critique are welcome — please open a GitHub Issue or Discussion.*

*© 2026 Gökhan Can — MIT License*
