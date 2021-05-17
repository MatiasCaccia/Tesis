import pymysql

conn = pymysql.connect(host = 'db4free.net', user = 'elmatiascege', passwd = 'EstebanLombera', db = 'ruidourbano')

def crearTabla(p_f,p_t,filtro,detector,mn,dd,hh,mm,ss):
    myCursor = conn.cursor()
    nombre_Tabla = str(p_f) + str(p_t) + str(filtro) + str(detector) + "_2021_" + str(mn) + "_"+ str(dd) + "_" + str(hh) +"_"+ str(mm)+"_"+ str(ss)
    if filtro == 'O':
        myCursor.execute("CREATE TABLE " + str(p_f) + str(p_t) + str(filtro) + str(detector) +
                         "_2021_" + str(mn) + "_"+ str(dd) + "_" + str(hh) +"_"+ str(mm)+"_"+ str(ss) +"""
            (
            f31 REAL,
            f63 REAL,
            f125 REAL,
            f250 REAL,
            f500 REAL,
            f1000 REAL,
            f2000 REAL,
            f4000 REAL,
            f8000 REAL,
            Global REAL,
            SoundExpLVL REAL,
            Lpeak REAL,
            Lmax REAL,
            Lmin REAL,
            hora REAL,
            min REAL,
            seg REAL,
            Temp REAL,
            CPU REAL,
            RAM REAL,
            MEMO REAL
            )
            """)
    else:
        myCursor.execute("CREATE TABLE " + str(p_f) + str(p_t) + str(filtro) + str(detector) +
                         "_2021_" + str(mn) + "_"+ str(dd) + "_" + str(hh) +"_"+ str(mm)+"_"+ str(ss) +"""
            (
            f25 REAL,
            f31 REAL,
            f40 REAL,
            f50 REAL,
            f63 REAL,
            f80 REAL,
            F100 REAL,
            f125 REAL,
            f160 REAL,
            f200 REAL,
            f250 REAL,
            f315 REAL,
            f400 REAL,
            f500 REAL,
            f630 REAL,
            f800 REAL,
            f1000 REAL,
            f1250 REAL,
            f1600 REAL,
            f2000 REAL,
            f2500 REAL,
            f3150 REAL,
            f4000 REAL,
            f5000 REAL,
            f6300 REAL,
            f8000 REAL,
            f10000 REAL,
            Global REAL,
            SoundExpLVL REAL,
            Lpeak REAL,
            Lmax REAL,
            Lmin REAL,
            hora REAL,
            min REAL,
            seg REAL,
            Temp REAL,
            CPU REAL,
            RAM REAL,
            MEMO REAL
            )
            """)
    conn.commit()
    conn.close()
    return nombre_Tabla, print("Tabla creada")