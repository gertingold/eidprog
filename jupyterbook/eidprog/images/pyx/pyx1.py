from pyx import graph

g = graph.graphxy(width=8)
g.plot(graph.data.file("pyx1.dat", x=1, y=2))
g.writePDFfile()
g.writeGSfile(device="pnggray", resolution=800)
