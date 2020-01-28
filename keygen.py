from random import sample,seed
def keygen(defin,seednumber):
    seed(seednumber)
    colorlist = []
    colordict = {}
    redlist = sample(range(256),256)
    greenlist = sample(range(256),256)
    bluelist = sample(range(256),256)
    for i in range(256):
        colorlist.append(((redlist[i],greenlist[i],bluelist[i])))
    if defin == 'l' or defin == 1:
        return colorlist
    elif defin == 'd' or defin == 2:
        for i in range(len(colorlist)):
            colordict.update({colorlist[i] : i + 1})
        return colordict