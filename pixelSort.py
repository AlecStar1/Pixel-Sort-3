

#? IDEA:
#? WHHAT IF WE THREAD THE IMAGE DOWN THE MIDDLE
#? LIKE WE ALREADY GOT IT FOR EACH LINE BUT WE SPLIT EM IN 2 
# ?AND IF 1 SIDE ENDS BEFORE THE OTHER IT MESSAGES IT TELLING IT NEEDS TO CALCULATE AGAIN


from PIL import Image
import threading
im = Image.open("bee.png")
rah = im.convert('RGB')
rgb_im = rah.load()
width, height = im.size
thresh = 100
fn = lambda x : 255 if x > thresh else 0
r = im.convert('L').point(fn, mode='1')
blackwhite = r.load()
r.show()

def comparePixels(p1, p2):
    return biggetchan(p1[0], p1[1]) > biggetchan(p2[0], p2[1])
        
    return getHue(p1[0], p1[1]) < getHue(p2[0], p2[1])

def biggestChannel(x,y):
    a =""
    big = max(rgb_im[x,y][1], rgb_im[x,y][2], rgb_im[x,y][0])
    r, g, b = rgb_im[x,y]
    if r == big:
        return 'r'
    elif g == big:
        return 'g'
    else:
        return 'b'
def biggetchan(x,y):
    return max(rgb_im[x,y][1], rgb_im[x,y][2], rgb_im[x,y][0])
    

    return 

def getHue(x,y):
    red, green, blue = rgb_im[x,y]
    min2 = min(min(red, green), blue)
    max2 = max(max(red, green), blue)
    if (min2 == max2):
        return 0
    hue = 0
    if (max2 == red):
        hue = (green - blue) / (max2 - min2)
    elif (max2 == green):
        hue = 2 + (blue - red) / (max2 - min2)
    else:
        hue = 4 + (red - green) / (max2 - min2)
    hue = hue * 60
    if (hue < 0):
        hue = hue + 360
    return round(hue)

frame = []
def thready(h):
    f = True
    goOver = 0
    while f and goOver<2000:
        f = False
        goOver += 1
        print("Line "+str(h)+" \tLoop: "+ str(goOver))
        for j in range(width-1):   
            if(blackwhite[j,h] == blackwhite[j+1,h]):
                if (comparePixels([j,h],[j+1,h])):
                    temp = rgb_im[j+1,h]
                    rgb_im[j+1,h] = rgb_im[j,h]
                    rgb_im[j,h] = temp
                    f = True
            
        # frame.append(rah.copy())

threads = list()
import threading
for index in range(height):
        x = threading.Thread(target=thready, args=(index,))
        threads.append(x)
        x.start()
for index, thread in enumerate(threads):
        thread.join()
        print("line %d done out of %d",index,range(height))
# frame[0].save('out.gif', save_all=True, append_images=frame)
rah.show()
f = rah.copy()
f.save('outIMAGE.png')
