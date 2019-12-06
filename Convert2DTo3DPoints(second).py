import json
import time

lasers = json.loads(open("lasers.txt", "r").read())

laser_y_tot = lasers["laser_y_tot"]
laser_z_tot = lasers["laser_z_tot"]

global x
x = []
y = []
z = []

corre = []
co = []
coe = 65
coe2 = 65
for i in range(0, int(len(laser_y_tot)/2)):
    corre = [-coe/2-i*coe] + corre + [-coe2/2-i*coe2]
    co = [coe/2+i*coe] + co + [-coe/2-i*coe]
print(corre)

cst = 0
while cst < len(laser_y_tot):
    if cst not in [-1]:
        if (len(laser_y_tot[cst]) > 0) & (len(laser_z_tot[cst]) > 0):
            c = 0
            while c < len(laser_z_tot[cst]):
                    x1 = laser_z_tot[cst][c]
                    y1 = laser_y_tot[cst][c]
                    correction = 0
                    try:
                        correction = abs(min(laser_z_tot[cst]) - min(laser_z_tot[-cst - 1]))
                    except:
                        pass

                    if cst < int(len(laser_y_tot)/2):

                        X = co[cst]
                        Y = -y1
                        Z = (corre[cst]-x1)

                        x += [X]
                        y += [Y]
                        z += [Z]

                        x += [-10 + co[-cst-1]]
                        y += [Y]
                        z += [Z]
                    else:
                        X = co[cst]
                        Y = -y1
                        Z = (corre[cst] - x1)

                        x += [X]
                        y += [Y]
                        z += [Z + correction]

                        x += [-10 + co[-cst - 1]]
                        y += [Y]
                        z += [Z + correction]
                    c += 1
    cst += 1

avant = time.time()

lasers = {"x": x, "y": y, "z": z}
open("points.txt", "w").write(json.dumps(lasers))
