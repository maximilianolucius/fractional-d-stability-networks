.PHONY: test demo applied-simulation applied-figure paper clean

test:
	pytest

demo:
	python3 scripts/demo_fractional_stability.py

applied-simulation:
	PYTHONPATH=src python3 computations/figures_wave2/scripts/nonlinear_caputo_simulation.py

applied-figure:
	PYTHONPATH=src python3 computations/figures_wave2/scripts/fig09_nonlinear_caputo_dynamics.py

paper:
	cd paper && TEXINPUTS='.:../reference-paper//:' BSTINPUTS='.:../reference-paper//:' latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex

clean:
	cd paper && latexmk -C || true
