def CurvHor(R, A): 
    import numpy as np
    import matplotlib.pylab as plt
    def tan(grados):
        return np.tan(np.radians(grados))
    def sen(grados):
        return np.sin(np.radians(grados))
    pi = np.pi
    theta = np.linspace(0, np.pi/2, 30)
    
#Calculos
    LC = A*pi*R/180
    Sbt = R*tan(A/2)
    Ext = Sbt*tan(22.5)
    B = Sbt*sen(A/2)
    OM = B-Ext
    C = 2*R*sen(A/2)
    
    plt.annotate ('', (R, 0), (0, R), arrowprops={'arrowstyle':'-'})
    plt.annotate ('', (R, 0), (R, R), arrowprops={'arrowstyle':'-'})
    plt.annotate ('', (R, R), (0, R), arrowprops={'arrowstyle':'-'})
    
    x = np.cos(theta)
    y = np.sin(theta)
    z = x*R
    w = y*R

    plt.plot(z,w)
    plt.axis("equal")
    plt.show()

    return "Longitud de curva",LC, "Subtangente",Sbt, "Externa",Ext, "Ordenada media",OM, "Cuerda",C
