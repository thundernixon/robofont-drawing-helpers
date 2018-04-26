
# NOT YET WORKING

f = CurrentFont()
g= CurrentGlyph()

help(g)

startSegment = 1

for c in g:
    # print(c)
    for s in c:
        # print(s)
        for a in s:
            if a.selected == True:
                # print(a)
                help(a)
                print(a.x)
                a
                startSegment = s.index
                print(startSegment)
        # if c is the current contour
        if 'startSegment':in vars()
            c._setStartSegment(startSegment)
        # help(c._setStartSegment)

# g._setStartSegment(startSegment)
g.contours._setStartSegment(startSegment)