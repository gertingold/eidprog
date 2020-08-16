all:
	python create_unicode_tex.py
	xelatex unicode.tex
	pdfcrop unicode.pdf unicode_cropped.pdf
	pdftk unicode_cropped.pdf cat 2 output u0000.pdf
	pdftk unicode_cropped.pdf cat 3 output u0080.pdf
	pdftk unicode_cropped.pdf cat 9 output u0380.pdf
	pdftk unicode_cropped.pdf cat 70 output u2200.pdf
	convert -density 300 u0000.pdf u0000.png
	convert -density 300 u0080.pdf u0080.png
	convert -density 300 u0380.pdf u0380.png
	convert -density 300 u2200.pdf u2200.png

clean:
	rm unicode.tex unicode.aux unicode.log unicode.pdf unicode_cropped.pdf
