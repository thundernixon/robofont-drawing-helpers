# purpose: place a grid of guides on all glyphs
# stretch: let users dictate grid density either by UPM divisions or by distance, starting from origin

f = CurrentFont()
g = CurrentGlyph()
UPM = f.info.unitsPerEm


## Set grid size or number of divisions in UPM2
# gridSize = 25
divisions = 20
gridSize = int(round(UPM / divisions))


# clear existing guides in glyph
def clearGuides():
    for guide in g.guides:
        g.removeGuide(guide)

clearGuides()

# add vertical guides
for x in range(0, g.width+gridSize, gridSize):
    g.addGuide((x, 0),90)
    
# add horizontal guides
for y in range(0, UPM, gridSize):
    startAt = f.info.descender
    startAt += y
    g.addGuide((0, startAt),0)
    
# make guides magnetic
for guide in g.guides:
    # prevent vertical guides from being far more "magnetic"
    if guide.angle == 90:
        guide.magnetic = 0
    else:
        guide.magnetic = 0
    
    
    
    