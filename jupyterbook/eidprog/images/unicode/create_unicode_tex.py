def make_table(datei, hexbase):
    cell = "|>{\\PreserveBackslash\\centering}p{12mm}"
    datei.write("\\noindent\n\\begin{tabular}{%s|}\n\\hline\n" % (cell*8))
    for lsb in range(16):
        datei.write("\\rowcolor{grau1}\n")
        for msb in range(8):
            hexcode = hexbase << 7
            hexcode = hexcode + (msb << 4)
            hexcode = hexcode + lsb
            if msb == 7:
                end = "\\\\\n"
            else:
                end = " &\n"
            datei.write("{\\footnotesize\\sffamily U+%04X} %s" %
                        (hexcode, end))
        datei.write("\\rowcolor{grau2}\n")
        for msb in range(8):
            hexcode = hexbase << 7
            hexcode = hexcode + (msb << 4)
            hexcode = hexcode + lsb
            if msb == 7:
                end = "\\\\\n"
            else:
                end = " &\n"
            datei.write("{\\footnotesize\\sffamily %s} %s" %
                        (get_hex_string(hexcode), end))
        datei.write("\\vrule width 0pt height 5mm depth 2mm\n")
        for msb in range(8):
            hexcode = hexbase << 7
            hexcode = hexcode + (msb << 4)
            hexcode = hexcode + lsb
            if msb == 7:
                end = "\\\\\\hline\n"
            else:
                end = " &\n"
            ccodes(datei, hexcode, end)
    datei.write("\\end{tabular}\n\n")


def ccodes(datei, hexcode, end):
    controlcodes = {0x00: "NUL", 0x01: "SOH", 0x02: "STX", 0x03: "ETX",
                    0x04: "EOT", 0x05: "ENQ", 0x06: "ACK", 0x07: "BEL",
                    0x08: "BS", 0x09: "HT", 0x0A: "LF", 0x0B: "VT",
                    0x0C: "FF", 0x0D: "CR", 0x0E: "SO", 0x0F: "SI",
                    0x10: "DLE", 0x11: "DC1", 0x12: "DC2", 0x13: "DC3",
                    0x14: "DC4", 0x15: "NAK", 0x16: "SYN", 0x17: "ETB",
                    0x18: "CAN", 0x19: "EM", 0x1A: "SUB", 0x1B: "ESC",
                    0x1C: "FS", 0x1D: "GS", 0x1E: "RS", 0x1F: "US",
                    0x20: "SP", 0x7F: "DEL", 0x80: "XXX", 0x81: "XXX",
                    0x82: "BPH", 0x83: "NBH", 0x84: "IND", 0x85: "NEL",
                    0x86: "SSA", 0x87: "ESA", 0x88: "HTS", 0x89: "HTJ",
                    0x8A: "VTS", 0x8B: "PLD", 0x8C: "PLU", 0x8D: "RI",
                    0x8E: "SS2", 0x8F: "SS3", 0x90: "DCS", 0x91: "PU1",
                    0x92: "PU2", 0x93: "STS", 0x94: "CCH", 0x95: "MW",
                    0x96: "SPA", 0x97: "EPA", 0x98: "SOS", 0x99: "XXX",
                    0x9A: "SCI", 0x9B: "CSI", 0x9C: "ST", 0x9D: "OSC",
                    0x9E: "PM", 0x9F: "APC", 0xA0: "NBSP", 0xAD: "SHY"}
    if hexcode in controlcodes:
        datei.write("\\colorbox{cc}{%s} %s" % (controlcodes[hexcode], end))
    else:
        datei.write("\\symbol{%i} %s" % (hexcode, end))


def get_hex_string(hexcode):
    if hexcode <= 0x7f:
        return "%02X" % hexcode
    if 0x80 <= hexcode <= 0x7ff:
        return "%04X" % (0xc080+((hexcode >> 6) << 8)+(hexcode & 0x3f))
    if 0x800 <= hexcode <= 0xffff:
        return "%06X" % (0xe08080+((hexcode >> 12) << 16) +
                         ((hexcode & 0xfc0) << 2) +
                         (hexcode & 0x3f)
                         )
    else:
        return 0

datei = open("unicode.tex", "w")
datei.write("""%!TEX TS-program = xetex
%!TEX encoding = UTF-8 Unicode
\\documentclass{article}
\\usepackage{xunicode}
\\usepackage{fontspec}
\\usepackage{xltxtra}
\\usepackage{colortbl}
\\setromanfont[Mapping=tex-text]{FreeSerif}
\\definecolor{grau1}{rgb}{0.7,0.7,0.7}
\\definecolor{grau2}{rgb}{0.9,0.9,0.9}
\\definecolor{cc}{rgb}{0.7,0.7,0.7}
\\begin{document}
\\pagestyle{empty}
\\newcommand{\\PreserveBackslash}[1]{\\let\\temp=\\\\#1\\let\\\\=\\temp}
\\renewcommand{\\arraystretch}{0.8}
""")

for n in range(0x5a):
    make_table(datei, n)

datei.write("\\end{document}\n")
datei.close()
