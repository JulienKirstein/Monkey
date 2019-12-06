from PIL import Image
import numpy as np
import json
import os

pathRight = "scanRight"
pathLeft = "scanLeft"
directoryRight = os.listdir(pathRight)
directoryLeft = os.listdir(pathLeft)

laser_x_tot = []
laser_y_tot = []
laser_z_tot = []
for i in range(0, len(directoryRight)):
    laser_x = []
    laser_y = []
    laser_z = []

    imRight = Image.open(pathRight + "\\" + directoryRight[i])
    imRight = np.array(imRight)

    imLeft = Image.open(pathLeft + "\\" + directoryLeft[i])
    imLeft = np.array(imLeft)

    c = 0
    while c < len(imRight):
        d = 0
        while d < len(imRight[c]):
            listeRight = imRight[c][d]
            if 255 + 80 <= sum(listeRight) <= 255 + 300:
                if i <= len(directoryRight)/2 - 1:
                    laser_x += [d]
                else:
                    laser_z += [d]
                    laser_y += [c]
            listeLeft = imLeft[c][d]
            if 255 + 80 <= sum(listeLeft) <= 255 + 300:
                if i <= len(directoryRight)/2 - 1:
                    laser_z += [1920-d]
                    laser_y += [c]
                else:
                    laser_x += [d]
            d += 1
        c += 1

    laser_x_tot += [laser_x]
    laser_y_tot += [laser_y]
    laser_z_tot += [laser_z]

lasers = {"laser_x_tot": laser_x_tot, "laser_y_tot": laser_y_tot, "laser_z_tot": laser_z_tot}
open("lasers.txt", "w").write(json.dumps(lasers))
