.PHONY: test demo paper clean

test:
	pytest

demo:
	python scripts/demo_fractional_stability.py

paper:
	cd paper && latexmk -pdf main.tex

clean:
	cd paper && latexmk -C || true
