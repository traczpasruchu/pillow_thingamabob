from PIL import Image
import base64,math,keygen

def encode(infile):
    #get string for base64
    f = open('out.txt', 'w')
    r = open(infile, 'rb')
    f.truncate()
    f.write(str(base64.b64encode(r.read()))[2:-1])
    r.close()
    f.close()
    print('done getting string')

    #open test and turn into a list of tuples
    colorlist = keygen.keygen(1,4)
    infile_open = open('out.txt', 'r')
    bigstring = infile_open.read()
    infile_open.close()
    res_colorlist = []
    for c in range(len(bigstring)):
        res_colorlist.append(colorlist[ord(bigstring[c])])
    print('done adding tuples to list')

    #put list of tuples into image as rgb values
    side_len = math.floor(math.sqrt(len(res_colorlist))) + 1
    im = Image.new('RGB',(side_len,side_len),'#ffffff')
    cur_pos = 0
    for y in range(side_len):
        for x in range(side_len):
            im.putpixel((x,y),res_colorlist[cur_pos])
            cur_pos += 1
    print('done drawing image')
    im.save(infile + '.png')
    print('saved image as ' + infile + '.png')
encode('outfile.exe')