def CurvHor(Name, G, M, S): 
    import numpy as np
    import matplotlib.pylab as plt
    import pandas as pd
    def tan(grados):
        return np.tan(np.radians(grados))
    def sen(grados):
        return np.sin(np.radians(grados))
    pi = np.pi
    theta = np.linspace(0, np.pi/2, 30)
    
#Se calculan los grados minutos y segundos del angulo de deflexion
    Ang = (G + (M * 1/60) + (S * 1/3600))

#Se lee el archivo CSV de donde se extraeran los datos.    
    nom = Name+".csv"
    datos = pd.read_csv(nom)
    
#Se acomodan los datos de menor a mayor para poder extraer los datos menores de la curva.    
    menor = (datos.sort_values(by='x'))
    p1x = menor.iloc[0,0]
    p1y = menor.iloc[0,1]

#Se acomodan los datos de mayor a menor para poder extraer los datos mayores de la curva.    
    mayor = (datos.sort_values(by='x',ascending=False))
    p2x = mayor.iloc[0,0]
    p2y = mayor.iloc[0,1]
    
#Se emplea la formula de la distancia entre dos puntos para poder calcular la Cuerda de la curva.    
    C = np.sqrt((p2x-p1x)**2 +(p2y-p1y)**2)
    
#Calculos
    R = C/(sen(Ang/2)*2)
    LC = Ang*pi*R/180
    Sbt = R*tan(Ang/2)
    Ext = Sbt*tan(Ang/4)
    B = Sbt*sen(Ang/2)
    OM = B-Ext
    
    plt.annotate ('', (R, 0), (0, R), arrowprops={'arrowstyle':'-'})
    plt.annotate ('', (R, 0), (R, R), arrowprops={'arrowstyle':'-'})
    plt.annotate ('', (R, R), (0, R), arrowprops={'arrowstyle':'-'})
    
    xp = np.cos(theta)
    yp = np.sin(theta)
    z = xp*R
    w = yp*R

    plt.plot(z,w)
    plt.axis("equal")
    plt.show()

    return "Longitud de curva",LC, "Subtangente",Sbt, "Externa",Ext, "Ordenada media",OM, "Radio",R, "Cuerda",C
