import pymysql.cursors

try:
    con = pymysql.connect(user="test", password="test", host="127.0.0.1",
                          database="IMedical", port=3306)
except:
   pass


def registro(datos):
    try:
        with con.cursor() as cursor:
            sql = "SELECT matricula, clave from usuario where matricula =%s"
            cursor.execute(sql, datos)
            query = cursor.fetchall()

            return query
    except:
        pass


def consultasector():
    try:
        with con.cursor() as cursor:
            sql = "SELECT idsec, NombreSec from Sector where idsec"
            cursor.execute(sql)
            query = cursor.fetchall()

            return query
    except:
        pass

def consultatodo():
    try:
        with con.cursor() as cursor:
            sql = "SELECT idprod, idsec , NombreProd from Producto, Sector where FKidsec = idsec"
            cursor.execute(sql)
            query = cursor.fetchall()

            con.close()
            cursor.close()

            return query
    except:
        pass


if __name__== "__main__":
    print(consultatodo())
    #l = registro("1")
    #print(str(l[0]).split()[1])


