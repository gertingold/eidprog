from pyx import canvas, color, deco, path, style, text, unit


def draw_square(x, y, kante):
    c.stroke(path.rect(x, y, kante, kante),
             [style.linewidth.thick, deco.filled([color.grey(1)])])

text.set(text.LatexRunner)
unit.set(xscale=1.3)
c = canvas.canvas()

kante = 1
dist = 0.2
nrboxes = 8

c.fill(path.rect(-0.3*dist, -0.2, 5*kante+4.6*dist, kante+0.4),
       [color.grey(0.5)])
c.fill(path.rect(-0.3*dist+5*(kante+dist), -0.2, 3*kante+2.6*dist, kante+0.4),
       [color.grey(0.5)])

for n in range(nrboxes):
    x = n*(kante+dist)
    draw_square(x, 0, kante)
    c.text(x+0.5*kante, 0.5*kante, r"\texttt{%s}" % n,
           [text.halign.center, text.valign.middle])

for n in range(nrboxes+1):
    x = n*(kante+dist)
    c.stroke(path.line(x-0.5*dist, -0.5, x-0.5*dist, -0.1), [deco.earrow])
    c.text(x-0.5*dist, -0.7, r"\texttt{%s}" % n,
           [text.halign.center, text.valign.top])

c.text(2.5*kante+2*dist, kante+0.4, r"\texttt{a[0:5]}", [text.halign.center])
c.text(6.5*kante+6*dist, kante+0.4, r"\texttt{a[5:8]}", [text.halign.center])

c.writePDFfile()
c.writeGSfile(device="pnggray", resolution=600)
