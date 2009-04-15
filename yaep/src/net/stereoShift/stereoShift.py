'''
Created on Apr 13, 2009

@author: HP_Administrator
'''
import Image
import PIL
import random
import Matrix

leftImage = Image.open("C:\Documents and Settings\HP_Administrator\My Documents\workspace\processing\shiftStereo\shiftStereo\data\image0521L.bmp")
rightImage = Image.open("C:\Documents and Settings\HP_Administrator\My Documents\workspace\processing\shiftStereo\shiftStereo\data\image0521R.bmp")
    
def colorCompare( c1, c2):
    (r1,b1,g1) = c1
    (r2,b2,g2) = c2
    return (r1-r2)^2 + (b1-b2)^2 + (g1-g2)^2

SAMPLE_COUNT = 100;
def imageCompare( dx, dy, dt):
    rtn = 0.0;
    for i in range(0, SAMPLE_COUNT, 1):
        xp = yp = -1
        while((xp, yp) > rightImage.size or xp < 0 or yp < 0):
            x = random.uniform(0, leftImage.size[0])
            y = random.uniform(0, leftImage.size[1])
            xp = x + dx
            yp = y + dy
            lcolor = leftImage.getpixel((x,y))
            rcolor = rightImage.getpixel((xp, yp))
            rtn += colorCompare(lcolor, rcolor)
        print(xp, yp);                
    rtn = rtn / SAMPLE_COUNT;
    return rtn;  

if __name__ == '__main__':
    #leftImage.show()
    #rightImage.show()
    print(imageCompare(0,0,0))
    


