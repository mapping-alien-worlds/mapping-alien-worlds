# 🤝 Contributing to Mapping Alien Worlds

Thank you for your interest in this project! This is an open concept study — contributions of all kinds are welcome, from code to critique.

## 🌟 Who We Are Looking For

- **Astronomers / astrophysicists**: photon budgets, nulling interferometry, observation strategy
- **ML / AI researchers**: sparse image reconstruction (diffusion priors, compressed sensing), swarm RL
- **Space systems engineers**: formation flight, metrology, OPD control
- **Everyone else**: documentation, translations, visualizations, questions

## 🚀 How to Contribute

1. **Discussions**: Not sure where to start? Introduce yourself or ask a question in [Discussions](../../discussions).
2. **Issues**: Found an error in the physics, math, or code? Open an [Issue](../../issues) — technical critique is the most valuable contribution at this stage.
3. **Pull Requests**:
   - Fork the repository and create a branch (`git checkout -b my-improvement`)
   - Make your changes and commit with a clear message
   - Open a Pull Request describing *what* and *why*

## 🧪 Code Guidelines

- Python 3.9+, keep dependencies minimal (`numpy`, `scipy`, `matplotlib`)
- Include docstrings and cite sources for physical constants / formulas
- Simulations must be reproducible (fixed random seeds)
- One focused change per pull request

## 📐 Scientific Standards

- Claims should be backed by calculations or citations (papers, NASA/ESA/JAXA sources)
- First-order estimates are fine — but label them as such
- Keep the two target scenarios (Alpha Cen A vs. Proxima b) consistent — never mix their photon budgets

## 💡 Open Problems (Great Starting Points)

- End-to-end photon budget including zodiacal/exozodiacal backgrounds
- AI reconstruction benchmark: diffusion prior vs. CLEAN/Wiener on sparse uv data
- Inner working angle feasibility at ~37 mas (Proxima b)
- Formation-flight OPD stabilization requirements

See [docs/technical_overview.md](docs/technical_overview.md) for full context.

## 🤲 Code of Conduct

Be respectful and constructive. Critique ideas, not people. We are building an open, welcoming scientific community.

---
*© 2026 Gökhan Can — MIT License*
