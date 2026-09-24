# Reproducibility protocol

For every result used in the manuscript, record:

- commit SHA;
- Python/package versions;
- graph definition or edge list;
- ecological model and parameter vector;
- equilibrium computation method;
- Jacobian construction;
- fractional order `alpha`;
- random seed;
- diagonal-scaling distribution and range, if used;
- solver tolerances;
- exact command that reproduces the output.

Generated artifacts should go to `experiments/outputs/` and should be regenerated rather than manually edited.
