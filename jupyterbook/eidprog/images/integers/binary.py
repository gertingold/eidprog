from pyx import canvas, path, text, trafo


def makebinaries(number, y0):
    size = 0.4
    dist = 0.1
    for n in range(32):
        c.stroke(path.rect(n*size+(n/8)*dist, y0, size, size))
        c.text((n+0.5)*size+(n/8)*dist, y0+0.07,
               r"\sffamily %i" % ((number >> 31-n) & 1),
               [text.halign.center])

    if number >> 31:
        c.text(32.2*size+5*dist, y0+0.07,
               r"\sffamily = -%i" % ((number ^ 0xffffffff)+1))
    else:
        c.text(32.2*size+5*dist, y0+0.07, r"\sffamily = %i" % number)

    p = path.path(path.moveto(0.2*size, size+0.03),
                  path.lineto(0.2*size, size+0.07),
                  path.lineto(3.8*size, size+0.07),
                  path.lineto(3.8*size, size+0.03))
    for n in range(4):
        c.stroke(p, [trafo.translate(n*(8*size+dist), y0)])
        c.text(n*(8*size+dist)+2*size, size+0.14+y0,
               r"\sffamily %X" % ((number >> ((3-n)*8+4)) & 15),
               [text.halign.center])
        c.stroke(p, [trafo.translate(n*(8*size+dist)+4*size, y0)])
        c.text(n*(8*size+dist)+6*size, size+0.14+y0,
               r"\sffamily %X" % ((number >> ((3-n)*8)) & 15),
               [text.halign.center])

text.set(text.LatexRunner)
c = canvas.canvas()
number = 0x6cd8932f

makebinaries(number, 1.5)
makebinaries((number ^ 0xffffffff)+1, 0)

c.writePDFfile()
c.writeGSfile(device="pnggray", resolution=800)
