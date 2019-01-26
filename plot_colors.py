#!/usr/bin/env python

# Some custom colors for matplotlib using RGB codes 
# of latex xcolor colors

from collections import OrderedDict

#convert un-normalised RGB code to hex-string
def rgb2hex(*args):
    return '#%02x%02x%02x' % args

plot_colors = [
    ("red"          , (255,0,0)     ),
    ("dodgerblue"   , (0,128,255)   ),
    ("forest-green" , (40,139,41)   ),
    ("gold"         , (254,213,48)  ),
    ("orange"       , (253,165,41)  ),
    ("magenta"      , (252,40,252)  ),
    ("turquoise"    , (74,224,209)  ),
    ("indigo"       , (128,0,128)   ),
    ("purple"       , (147,112,219) ),
    ("navy"         , (2,12,125)    ),
    ("firebrick"    , (204,0,0)     ),
    ("royalblue"    , (66,108,221)  ),
    ("chartreuse"   , (130,253,79)  ),
    ("goldenrod"    , (218,165,32)  ),
    ("burntorange"  , (255,69,0)    ),
    ("violet"       , (235,134,235) ),
    ("spring-green" , (0,250,154)   ),
    ("salmon"       , (248,128,118) ),
    ("aquamarine"   , (133,254,212) ),
    ("skyblue"      , (138,207,233) ),
    ("sandybrown"   , (253,161,103) )
]

plot_colors = [(name, rgb2hex(*code)) for (name, code) in plot_colors]
