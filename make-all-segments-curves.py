g = CurrentGlyph()

for contour in g:
    # set prevPoint to -1 (?)
    startPoint = -1
    
    for segment in contour:
        
        if segment.offCurve == []:
            print(contour[startPoint].onCurve)
            
            print("straight segment")
            print(segment.onCurve)
            
            # calculate 1/3 between startPoint and endPoint
            # append offCurve points a 1/3 and 2/3 between prevPoint and current point
            
            
            print("================")
        # segment.offCurve
        # print(segment.offCurve)
        else:
            print("curved segment")
            print("================")
            
        startPoint += 1