from pyx import color, deco, graph, style, unit

unit.set(xscale=1.3)

g = graph.graphxy(width=8,
                  x=graph.axis.linear(title="$x$"),
                  y=graph.axis.linear(title="$y$"))
g.plot(graph.data.file("pyx1.dat", x=1, y=2),
       [graph.style.line([style.linestyle.dashed, color.rgb(0, 0, 1)]),
        graph.style.symbol(graph.style.symbol.circle, size=0.1,
                           symbolattrs=[deco.filled([color.rgb.red]),
                                        deco.stroked([color.grey(0)])])])
g.writePDFfile()
g.writeGSfile(device="png16m", resolution=800)
