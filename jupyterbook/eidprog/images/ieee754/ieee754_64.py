from pyx import canvas, path, style, text, unit

text.set(text.LatexRunner)
unit.set(xscale=0.8)

b = 0.8

c = canvas.canvas()
offset = 0
c.stroke(path.rect(offset, 0, b, b))
c.stroke(path.path(path.moveto(offset+0.1*b, -0.1),
                   path.lineto(offset+0.1*b, -1.2),
                   path.lineto(offset+0.3*b, -1.2)), [style.linewidth.thin])
c.text(offset+0.2*b, -1.1, r"\sffamily Vorzeichen")
c.text(0.5*b, 1.1*b, r"\sffamily 1 Bit", [text.halign.center])
c.text(0.5*b, 0.5*b, r"\sffamily S", [text.halign.center, text.valign.middle])
offset = 1.2*b
c.stroke(path.path(path.moveto(offset+0.5*b, b),
                   path.lineto(offset, b),
                   path.lineto(offset, 0),
                   path.lineto(offset+0.5*b, 0)))
c.stroke(path.path(path.moveto(offset+0.1*b, -0.1),
                   path.lineto(offset+0.1*b, -0.7),
                   path.lineto(offset+0.3*b, -0.7)), [style.linewidth.thin])
c.text(offset+0.2*b, -0.6, r"\sffamily Exponent")
offset = offset+0.5*b
c.stroke(path.line(offset, 0, offset+b, 0), [style.linestyle.dotted])
c.stroke(path.line(offset, b, offset+b, b), [style.linestyle.dotted])
c.text(offset+0.5*b, 1.1*b, r"\sffamily 11 Bits", [text.halign.center])
c.text(offset+0.5*b, 0.5*b, r"\sffamily E",
       [text.halign.center, text.valign.middle])
offset = offset+b
c.stroke(path.path(path.moveto(offset, b),
                   path.lineto(offset+0.5*b, b),
                   path.lineto(offset+0.5*b, 0),
                   path.lineto(offset, 0)))
offset = offset+0.7*b
c.stroke(path.path(path.moveto(offset+0.5*b, b),
                   path.lineto(offset, b),
                   path.lineto(offset, 0),
                   path.lineto(offset+0.5*b, 0)))
c.stroke(path.path(path.moveto(offset+0.1*b, -0.1),
                   path.lineto(offset+0.1*b, -0.7),
                   path.lineto(offset+0.3*b, -0.7)), [style.linewidth.thin])
c.text(offset+0.2*b, -0.6, r"\sffamily Mantisse")
offset = offset+0.5*b
c.stroke(path.line(offset, 0, offset+5*b, 0), [style.linestyle.dotted])
c.stroke(path.line(offset, b, offset+5*b, b), [style.linestyle.dotted])
c.text(offset+2.5*b, 1.1*b, r"\sffamily 52 Bits", [text.halign.center])
c.text(offset+2.5*b, 0.5*b, r"\sffamily T",
       [text.halign.center, text.valign.middle])
offset = offset+5*b
c.stroke(path.path(path.moveto(offset, b),
                   path.lineto(offset+0.5*b, b),
                   path.lineto(offset+0.5*b, 0),
                   path.lineto(offset, 0)))

c.writePDFfile()
c.writeGSfile(device="pnggray", resolution=600)
