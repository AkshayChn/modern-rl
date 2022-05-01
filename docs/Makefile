PROG=pdflatex
FLAGS='-output-directory pdf'

main:
	latexmk -pdf -outdir=output -halt-on-error main.tex

clean: 
	latexmk -C -pdf -outdir=output -halt-on-error main.tex
