def net_adress(ipl,mask):
    maskb = str("1"*mask+"0"*(32-mask)) 
    mlst = [int(maskb[i:i+8],2) for i in range(0,len(maskb),8)]
    return [ipl[i]&mlst[i] for i in range(4)]

def broadcast(ntadr,mask):
    maskb = str("0"*mask+"1"*(32-mask))
    inv = [int(maskb[i:i+8],2) for i in range(0,len(maskb),8)]
    return [ntadr[i]|inv[i] for i in range(4)]

def available(mask,ipl):
    if ipl[0] > 0 and ipl[0] < 128:
        sb = mask - 8
        hb = 32 - mask
        snets = 2**sb
        hosts = 2**hb - 2
    elif ipl[0] > 127 and ipl[0] < 192:
        sb = mask - 16
        hb = 32 - mask
        snets = 2**sb
        hosts = 2**hb - 2
    elif ipl[0] > 191 and ipl[0] < 224:
        sb = mask - 24
        hb = 32 - mask
        snets = 2**sb
        hosts = 2**hb - 2
    else:
        print(" class d or e ")
    return snets,hosts

def subrange(ntadr,bdcst):
    ntadr[-1] = ntadr[-1]+1
    bdcst[-1] = bdcst[-1]-1
    ntadr = [str(x) for x in ntadr]
    bdcst = [str(x) for x in bdcst]
    return ".".join(ntadr)+"-"+".".join(bdcst)
