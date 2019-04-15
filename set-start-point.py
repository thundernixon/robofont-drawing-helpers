# NOTE: you can also create a hotkey for this under Preferences > Glyph View > Hot Keys > Set Start Point

glyph = CurrentGlyph()

# startSegment = 1

# for contour in glyph:
#     for segment in contour:
#         for point in segment:
#             if point.selected == True:
#                 startSegment = segment.index
#                 print(startSegment)
#             # check if startSegment was set
#             if 'startSegment' in vars():
#                 contour.setStartSegment(startSegment+1)
                
glyph = CurrentGlyph()

if len(glyph.selectedPoints) == 1:
    for contour in glyph:
        for segment in contour:
            for point in segment:
                if point.selected == True:
                    print(segment.index + 1)
                    print(len(contour))
                    print((segment.index + 1) % len(contour) )
                    startSegment = (segment.index + 1) % len(contour) 
                    contour.setStartSegment(startSegment)
                    point.selected = False
else:
    print('please select one point!')