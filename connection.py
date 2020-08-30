#####################################
##         BASE DE DATOS           ##
#####################################
import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="instabotV2"
  )
except:
  print("\033[31m[ NO SE HA PODIDO CONECTAR CON LA BASE DE DATOS ]\033[00m")