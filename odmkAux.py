# -*- coding: utf-8 -*-
###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#header begin------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################

#__::((odmkAux.py))::__

#Tools for plotting
#LaTex function dictionary
#color definitions


###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#header end--------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################


###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#main begin------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################


import os


#//////////////////////////////////////////////////////////////////////////////
#Clear console / workspace-----------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def clr():
    '''Clears the spyder shell'''
    os.system('cls')
    return None
    
clr()

def clrvar():
    '''Clears all the variables from the spyder workspace'''

    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue
        if 'func' in str(globals()[var]): continue
        if 'module' in str(globals()[var]): continue

        del globals()[var]

clrvar()


#//////////////////////////////////////////////////////////////////////////////
#Plotting: setup & definitions begin-------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Create dictionary of math text examples:
odmk_pyLaTeX = {
    0: r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = "
    r"U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} "
    r"\int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ "
    r"U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_"
    r"{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$",

    1: r"$f(t) = e^{-t}*cos(2\pi t)$",

    2: r"$g(x) = A*exp \left ( -\frac{(x-\mu )^{2}}{2*\sigma ^{2}} \right ) +d$",

    3: r"$g(x) = A*exp \left ( -\frac{(x-\mu )^{2}}{2*\sigma ^{2}} \right ) +d$",

    4: r"$\frac{3}{4},\ \binom{3}{4},\ \stackrel{3}{4},\ "
    r"\left(\frac{5 - \frac{1}{x}}{4}\right),\ \ldots$",

    5: r"$\sqrt{2},\ \sqrt[3]{x},\ \ldots$",

    6: r"$\mathrm{Roman}\ , \ \mathit{Italic}\ , \ \mathtt{Typewriter} \ "
    r"\mathrm{or}\ \mathcal{CALLIGRAPHY}$",

    7: r"$\acute a,\ \bar a,\ \breve a,\ \dot a,\ \ddot a, \ \grave a, \ "
    r"\hat a,\ \tilde a,\ \vec a,\ \widehat{xyz},\ \widetilde{xyz},\ "
    r"\ldots$",

    8: r"$\alpha,\ \beta,\ \chi,\ \delta,\ \lambda,\ \mu,\ "
    r"\Delta,\ \Gamma,\ \Omega,\ \Phi,\ \Pi,\ \Upsilon,\ \nabla,\ "
    r"\aleph,\ \beth,\ \daleth,\ \gimel,\ \ldots$",

    9: r"$\coprod,\ \int,\ \oint,\ \prod,\ \sum,\ "
    r"\log,\ \sin,\ \approx,\ \oplus,\ \star,\ \varpropto,\ "
    r"\infty,\ \partial,\ \Re,\ \leftrightsquigarrow, \ \ldots$"}

#define colors
#http://www.rapidtables.com/web/color/RGB_Color.htm
#2014-10-16
mplot_black = (0./255., 0./255., 0./255.)
mplot_white = (255./255., 255./255., 255./255.)
mplot_red = (255./255., 0./255., 0./255.)
mplot_orange = (255/255., 165/255., 0./255.)
mplot_darkorange = (255/255., 140/255., 0./255.)
mplot_orangered = (255/255., 69/255., 0./255.)
mplot_yellow = (255./255., 255./255., 0./255.)
mplot_lime = (0./255., 255./255., 0./255.)
mplot_green = (0./255., 128./255., 0./255.)
mplot_darkgreen = (0./255., 100./255., 0./255.)
mplot_cyan = (0./255., 255./255., 255./255.)
mplot_blue = (0./255., 0./255., 255./255.)
mplot_midnightblue = (25./255., 25./255., 112./255.)
mplot_magenta = (255./255., 0./255., 255./255.)
mplot_grey = (128./255., 128./255., 128./255.)
mplot_silver = (192./255., 192./255., 192./255.)
mplot_darkgrey = (64./255., 64./255., 64./255.)
mplot_darkdarkgrey = (32./255., 32./255., 32./255.)
mplot_purple = (128./255., 0./255., 128./255.)
mplot_maroon = (128./255., 0./255., 0./255.)
mplot_olive = (128./255., 128./255., 0./255.)
mplot_teal = (0./255., 128./255., 128./255.)


#define the color map
#colors = plt.cm.bone(np.linspace(0.57, 0.9, nRows))



#Marker codes:
# '+'=>plus sign ; '.'=>dot ; 'o'=>circle ; '*'=>star ; 'p'=>pentagon
# 's'=>square ; 'x'=>x char ; 'D'=>diamond ; 'h'=>hexagon ; '^'=>triangle

#Linesytle codes:
#  '-'=>Solid line ; ':'=>dotted line ; '-.'=>dashed dotted


#***sort out this process - from odmkFibonacciSpiral.py
# build colour cycle, using a number between 0 and 100 for each colour
#colcycle=[]
#s=100/ncols
#for j in range(ndiscs):
#    colcycle.append((j%ncols)*s)

# cycle through color map colors
#collection = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=1.0)
#collection = PatchCollection(patches, cmap=matplotlib.cm.BuPu, alpha=1.0)
#collection = PatchCollection(patches, cmap=matplotlib.cm.Spectral, alpha=1.0)
#collection = PatchCollection(patches, cmap=matplotlib.cm.Set1, alpha=1.0)
#collection = PatchCollection(patches, cmap=matplotlib.cm.hsv, alpha=1.0)
#collection = PatchCollection(patches, cmap=matplotlib.cm.gist_stern, alpha=1.0)
#collection = PatchCollection(patches, cmap=matplotlib.cm.gist_ncar, alpha=1.0)
#collection = PatchCollection(patches, cmap=matplotlib.cm.Accent, alpha=1.0)
#collection = PatchCollection(patches, cmap=matplotlib.cm.Dark2, alpha=1.0)

#collection.set_array(np.array(colcycle))
#ax.add_collection(collection)

'''
cnames = {
'aliceblue':            '#F0F8FF',
'antiquewhite':         '#FAEBD7',
'aqua':                 '#00FFFF',
'aquamarine':           '#7FFFD4',
'azure':                '#F0FFFF',
'beige':                '#F5F5DC',
'bisque':               '#FFE4C4',
'black':                '#000000',
'blanchedalmond':       '#FFEBCD',
'blue':                 '#0000FF',
'blueviolet':           '#8A2BE2',
'brown':                '#A52A2A',
'burlywood':            '#DEB887',
'cadetblue':            '#5F9EA0',
'chartreuse':           '#7FFF00',
'chocolate':            '#D2691E',
'coral':                '#FF7F50',
'cornflowerblue':       '#6495ED',
'cornsilk':             '#FFF8DC',
'crimson':              '#DC143C',
'cyan':                 '#00FFFF',
'darkblue':             '#00008B',
'darkcyan':             '#008B8B',
'darkgoldenrod':        '#B8860B',
'darkgray':             '#A9A9A9',
'darkgreen':            '#006400',
'darkkhaki':            '#BDB76B',
'darkmagenta':          '#8B008B',
'darkolivegreen':       '#556B2F',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'darkred':              '#8B0000',
'darksalmon':           '#E9967A',
'darkseagreen':         '#8FBC8F',
'darkslateblue':        '#483D8B',
'darkslategray':        '#2F4F4F',
'darkturquoise':        '#00CED1',
'darkviolet':           '#9400D3',
'deeppink':             '#FF1493',
'deepskyblue':          '#00BFFF',
'dimgray':              '#696969',
'dodgerblue':           '#1E90FF',
'firebrick':            '#B22222',
'floralwhite':          '#FFFAF0',
'forestgreen':          '#228B22',
'fuchsia':              '#FF00FF',
'gainsboro':            '#DCDCDC',
'ghostwhite':           '#F8F8FF',
'gold':                 '#FFD700',
'goldenrod':            '#DAA520',
'gray':                 '#808080',
'green':                '#008000',
'greenyellow':          '#ADFF2F',
'honeydew':             '#F0FFF0',
'hotpink':              '#FF69B4',
'indianred':            '#CD5C5C',
'indigo':               '#4B0082',
'ivory':                '#FFFFF0',
'khaki':                '#F0E68C',
'lavender':             '#E6E6FA',
'lavenderblush':        '#FFF0F5',
'lawngreen':            '#7CFC00',
'lemonchiffon':         '#FFFACD',
'lightblue':            '#ADD8E6',
'lightcoral':           '#F08080',
'lightcyan':            '#E0FFFF',
'lightgoldenrodyellow': '#FAFAD2',
'lightgreen':           '#90EE90',
'lightgray':            '#D3D3D3',
'lightpink':            '#FFB6C1',
'lightsalmon':          '#FFA07A',
'lightseagreen':        '#20B2AA',
'lightskyblue':         '#87CEFA',
'lightslategray':       '#778899',
'lightsteelblue':       '#B0C4DE',
'lightyellow':          '#FFFFE0',
'lime':                 '#00FF00',
'limegreen':            '#32CD32',
'linen':                '#FAF0E6',
'magenta':              '#FF00FF',
'maroon':               '#800000',
'mediumaquamarine':     '#66CDAA',
'mediumblue':           '#0000CD',
'mediumorchid':         '#BA55D3',
'mediumpurple':         '#9370DB',
'mediumseagreen':       '#3CB371',
'mediumslateblue':      '#7B68EE',
'mediumspringgreen':    '#00FA9A',
'mediumturquoise':      '#48D1CC',
'mediumvioletred':      '#C71585',
'midnightblue':         '#191970',
'mintcream':            '#F5FFFA',
'mistyrose':            '#FFE4E1',
'moccasin':             '#FFE4B5',
'navajowhite':          '#FFDEAD',
'navy':                 '#000080',
'oldlace':              '#FDF5E6',
'olive':                '#808000',
'olivedrab':            '#6B8E23',
'orange':               '#FFA500',
'orangered':            '#FF4500',
'orchid':               '#DA70D6',
'palegoldenrod':        '#EEE8AA',
'palegreen':            '#98FB98',
'paleturquoise':        '#AFEEEE',
'palevioletred':        '#DB7093',
'papayawhip':           '#FFEFD5',
'peachpuff':            '#FFDAB9',
'peru':                 '#CD853F',
'pink':                 '#FFC0CB',
'plum':                 '#DDA0DD',
'powderblue':           '#B0E0E6',
'purple':               '#800080',
'red':                  '#FF0000',
'rosybrown':            '#BC8F8F',
'royalblue':            '#4169E1',
'saddlebrown':          '#8B4513',
'salmon':               '#FA8072',
'sandybrown':           '#FAA460',
'seagreen':             '#2E8B57',
'seashell':             '#FFF5EE',
'sienna':               '#A0522D',
'silver':               '#C0C0C0',
'skyblue':              '#87CEEB',
'slateblue':            '#6A5ACD',
'slategray':            '#708090',
'snow':                 '#FFFAFA',
'springgreen':          '#00FF7F',
'steelblue':            '#4682B4',
'tan':                  '#D2B48C',
'teal':                 '#008080',
'thistle':              '#D8BFD8',
'tomato':               '#FF6347',
'turquoise':            '#40E0D0',
'violet':               '#EE82EE',
'wheat':                '#F5DEB3',
'white':                '#FFFFFF',
'whitesmoke':           '#F5F5F5',
'yellow':               '#FFFF00',
'yellowgreen':          '#9ACD32'}
'''

#//////////////////////////////////////////////////////////////////////////////
#Plotting: setup & definitions end---------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#main end------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################