margin = 40
strokeThickness = 60
g = CurrentGlyph()
f = CurrentFont()


# print(g.box) # grabs bounds of glyph

help(g)

for g in f:
    g.prepareUndo("decompose")
    g.decompose()
    g.update()
    g.performUndo()

for g in f:
    g.prepareUndo("draw box")

    g.width = 1000

    print(g.leftMargin, g.rightMargin)

    evenMargin = (g.leftMargin + g.rightMargin) / 2

    print(evenMargin)

    g.leftMargin = evenMargin
    g.rightMargin = evenMargin

    print(g.leftMargin, g.rightMargin)



    # g.scaleBy((0.5), origin=(g.width/2, f.info.xHeight/2))
    scaleFactor = 0.65

    # move caps into middle of 1000 UPM
    # diff = 1000 - capHeight
    # equalTopBottomMargin = diff/2
    # move down by descender, then up by equalTopBottomMargin
    # move down 250, move up 100
    # THEN scale, with origin at equalTopBottomMargin + capHeight/2
    
    
    g.scaleBy((scaleFactor), origin=(g.width/2, f.info.capHeight * scaleFactor - (f.info.capHeight * scaleFactor  / 2)))

    bottomLeft = (0+margin,f.info.descender+margin)
    topLeft = (0+margin,f.info.ascender-margin)
    topRight = (g.width-margin,f.info.ascender-margin)
    bottomRight = (g.width-margin,f.info.descender+margin)

    print(bottomLeft, topLeft, topRight,bottomRight)

    pen = g.getPen()

    pen.moveTo((bottomLeft[0],bottomLeft[1]))
    pen.lineTo((topLeft[0],topLeft[1]))
    pen.lineTo((topRight[0],topRight[1]))
    pen.lineTo((bottomRight[0],bottomRight[1]))


    pen.closePath()

    pen = g.getPen()

    pen.moveTo((bottomLeft[0]+strokeThickness,bottomLeft[1]+strokeThickness))
    pen.lineTo((bottomRight[0]-strokeThickness,bottomRight[1]+strokeThickness))
    pen.lineTo((topRight[0]-strokeThickness,topRight[1]-strokeThickness))
    pen.lineTo((topLeft[0]+strokeThickness,topLeft[1]-strokeThickness))


    pen.closePath()

    g.update()
    g.performUndo()