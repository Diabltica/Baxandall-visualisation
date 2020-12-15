import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
from math import log10
from math import sqrt
from math import pi


R=22000
R4 = 10000
Rv = 100000
C = 47 * (10 ** -9)
C2 = 560 * (10 ** -12)

a0 = None
a50 =None
a100 =None

licorne = 0


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)

'''
def H(x):
    return [20 * log10( abs((1+2*pi*i*C2*(R4+Rv*(1-x)))/(1+2*pi*i*C2*(R4+Rv*x)))) for i in range(20, 20_001)]
def T(x):
    k = -(Rv*(1-x) + R)/(R+x*Rv)
    T1 = (Rv*(1-x)+R)/(R*Rv*C)
    T2 =(x*Rv+R)/(R*Rv*C)
    return [20 * log10( abs((k*(1+i/T1)*1/(1+i/T2)))) for i in range(20, 20_001)]
'''

def G(y,x):
    k = -(Rv*(1-x) + R)/(R+x*Rv)
    T1 = (Rv*(1-x)+R)/(R*Rv*C)
    T2 =(x*Rv+R)/(R*Rv*C)
    return [20 * log10( abs((k*(1+i/T1)*1/(1+i/T2))))+20*log10(abs((1+2*pi*i*C2*(R4+Rv*(1-y)))/(1+2*pi*i*C2*(R4+Rv*y)))) for i in range(20, 20_001)]

def Affichage():
    plt.axis([20,20_000,-15,15])
    plt.xscale('log')


    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))

    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    plt.legend(loc='upper right')





F = list(range(20, 20_001))

c = int (input("choisir une valeur  -- 1 \n valeur par défaut -- 2\n choix :"))

if c == 1:
    a=0.5
    xval = a
    yval = a
    a0= G(a,a)

    y = np.array(a0)
    x = np.array(F)
    
    p,=plt.plot(x, y,color='blue')
    Affichage()

    axSlider1 = plt.axes([0.1,0.2,0.8,0.05])
    SlideB = Slider(axSlider1,'a RV1',0,1,0.5,'%.2f')

    axSlider2 = plt.axes([0.1,0.1,0.8,0.05])
    SlideH =Slider(axSlider2,'a RV2',0,1,0.5,'%.2f',color='green')

    axButton1 = plt.axes([0.1,0.9,0.1,0.1])
    btn1 = Button(axButton1,'Reset')



    def val_updateH(val):
        global yval
        yval= SlideH.val
        p.set_ydata(G(yval,xval))
        plt.draw()
        
    SlideH.on_changed(val_updateH)

    def val_updateB(val1):
        global xval
        xval= SlideB.val
        p.set_ydata(G(yval,xval))
        plt.draw()
        
    SlideB.on_changed(val_updateB)
    def Reset(event):
        SlideH.reset()
        SlideB.reset()
        
    btn1.on_clicked(Reset)
    
elif c==2:
    a0= G(0,0)
    a50 = G(0.5,0.5)
    a100 = G(1,1)
    
    y = np.array(a0)
    x = np.array(F)
    plt.plot(x, y,color='blue',label="alpha = 0")

    p = np.array(a50)
    plt.plot(x, p,color='red',label="alpha = 50")

    l = np.array(a100)
    plt.plot(x, l,color='green',label="alpha = 100")
    Affichage()
else:
    print("Entrée invalide")
    licorne = 1







if licorne == 0:
    plt.show()


