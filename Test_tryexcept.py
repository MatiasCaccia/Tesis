import numpy as np
import pymysql
import time
import os
import psutil

def get_cpu_temp():
    result = 0.0
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        line = f.readline().strip()
    if line.isdigit():
        result = float(line) / 1000
    return result

def subirDatos(tiempo,contador,mn,dd):
    q = np.load('/home/pi/Documents/2020_'+str(mn)+'/'+str(dd)+'.npy')
    #valores = contador*tiempo - contador # ACA MATI!!
    valores = (contador + 1) *tiempo
    asdf = q[(valores*-1):]
    sumita = asdf
    sumita1 = 10**(0.1*sumita)
    sumita2 = np.array([sum(x) for x in zip(*sumita1)])
    sumita3 = list(10*np.log10(sumita2/len(sumita)))
    Lpico = 0
    Nmax = 0
    Nmin = 0
    for n in range(0,len(asdf)):
        if asdf[n][-6] > Lpico:
            Lpico = asdf[n][-6]
        if asdf[n][-5] > Nmax:
            Nmax = asdf[n][-5]
        if asdf[n][-4] < Nmax:
            Nmin = asdf[n][-4]
    sumita3[-4] = Nmin
    sumita3[-5] = Nmax
    sumita3[-6] = Lpico
    sumita3[-3:-1] = asdf[-1][-3:-1]
    sumita3[-1] = asdf[-1][-1]
    Temp = np.around(get_cpu_temp(),2)
    sumita3.append(Temp)
    Perf_CPU = np.around(psutil.cpu_percent(),2)
    sumita3.append(Perf_CPU)
    Perf_RAM = np.around(psutil.virtual_memory().percent,2)
    sumita3.append(Perf_RAM)
    Perf_MEMO = np.around(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,2)
    sumita3.append(Perf_MEMO)
    # Guardar los datos en el archivo de contingencias
    files = np.load('contingencia.npy')
    if files.size == 0:
        files = sumita3
    else:
        files = np.vstack((files, sumita3))
    np.save('contingencia.npy',files)
    """
        Comienza a subir los datos a la red
    """
    #start = time.time()
    try:
        conn = pymysql.connect(host = 'db4free.net', user = 'elmatiascege', passwd = 'EstebanLombera', db = 'ruidourbano')
        # Cargar los datos de contingencia.npy
        sumita3 = np.load('contingencia.npy')
        cols = ("f31","f63","f125","f250","f500","f1000","f2000","f4000","f8000","Global","Lpeak","Lmax","Lmin","hora","min","seg","Temp","CPU","RAM","MEMO")
        for i in range(len(sumita3)):
            a = dict(zip(cols,sumita3[i]))
            myCursor = conn.cursor()
            sql = 'INSERT INTO Sensor2 ({fields}) VALUES ({values});'
            fields = ', '.join(a.keys())
            values = ', '.join(['"{0}"'.format(value) for value in a.values()])
            composed_sql = sql.format(fields=fields, values=values)
            myCursor.execute(composed_sql)   
            print("Tabla actualizada")
            conn.commit()
        conn.close() 
        # Borrar los datos que estan en contingencia.npy
        np.save('contingencia.npy',[])
    except:
        print('Error de conection')
        #Cargar los datos en
    return
