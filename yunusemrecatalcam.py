import numpy


matrix=numpy.loadtxt(raw_input("dosya ismi (.txt): "))


for y in range(1,12):
 for x in range(1,13):
     if matrix[y,x]==2:
         startx=x
         starty=y
         
print startx,starty 

while True:

    ydec=starty-1
    yinc=starty+1
    xdec=startx-1
    xinc=startx+1
    
    if matrix[starty,xinc]==3:
        startx=xinc
        print(startx,starty,"ov,buldum")
        break
    elif matrix[starty,xdec]==3:
        startx=xdec
        print(startx,starty,"ov,buldum")
        break
    elif matrix[ydec,startx]==3:
        starty=ydec
        print(startx,starty,"ov,buldum")
        break
    elif matrix[yinc,startx]==3:
        starty=yinc
        print(startx,starty,"ov,buldum")
        break
    
    elif matrix[ydec,startx]==0:        #0 arama
        starty=ydec
        matrix[starty,startx]=8
    elif matrix[yinc,startx]==0:
        starty=yinc
        matrix[starty,startx]=8
    elif matrix[starty,xinc]==0:
        startx=xinc
        matrix[starty,startx]=8
    elif matrix[starty,xdec]==0:
        startx=xdec
        matrix[starty,startx]=8
    elif matrix[yinc,startx]==8:     #8 arama
        matrix[starty,startx]=1
        starty=yinc
    elif matrix[ydec,startx]==8:
        matrix[starty,startx]=1
        starty=ydec
    elif matrix[starty,xinc]==8:
        matrix[starty,startx]=1
        startx=xinc
    elif matrix[starty,xdec]==8:
        matrix[starty,startx]=1
        startx=xdec
    else:
        break
    #print matrix
    print startx,starty
    
gn=input("YEC")


