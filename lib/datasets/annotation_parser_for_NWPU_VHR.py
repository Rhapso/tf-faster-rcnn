import os

classes = ['airplane', 'ship', 'storage tank', 'baseball diamond', 'tennis court', 'basketball court', 'ground track field', 'harbor', 'bridge', 'vehicle']


def getObjects(FilePath):
    objects = []
    with open(FilePath) as f:
        for line in f.readlines():
            lineArray = line.rstrip().split(',')
            xmin = float(lineArray[0].strip('(').strip(')'))
            ymin = float(lineArray[1].strip('(').strip(')'))
            xmax = float(lineArray[2].strip('(').strip(')'))
            ymax = float(lineArray[3].strip('(').strip(')'))
            assert xmax >= xmin
            assert ymax >= ymin
            label = classes[int(lineArray[4])-1]
            # diff = lineArray[5]   ---->NWPU_VHR datasets has no diff label
            diff = 0
            objects.append({
                "wnid": label, # class name, not number
                "difficult": diff,
                "box": {
                    "xmin": xmin,
                    "ymin": ymin,
                    "xmax": xmax,
                    "ymax": ymax,
                }
            })
    return objects


def parse(filepath):
    return getObjects(filepath) 