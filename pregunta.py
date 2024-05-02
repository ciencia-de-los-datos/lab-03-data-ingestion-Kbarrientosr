"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():

    filename = "clusters_report.txt"
    with open (filename, "r") as file:
        lines_df = file.readlines()

    datos = []
    
    for line in lines_df[4:]:
        word = line.strip()
        word = word.split()
        
        if len(word)>0 and word[0].isdigit():
            cluster = int(word[0])
            cantidad_de_palabras_clave = int(word[1])
            porcentaje_de_palabras_clave = float(word[2].replace(",","."))
            principales_palabras_clave = " ".join(word[3:]).replace(",", ", ").replace("%","").replace("  ", " ").replace("   "," ").replace("    "," ").replace(".","")
            principales_palabras_clave = principales_palabras_clave.strip()   
            datos.append({"cluster": cluster, "cantidad_de_palabras_clave": cantidad_de_palabras_clave, "porcentaje_de_palabras_clave": porcentaje_de_palabras_clave, "principales_palabras_clave": principales_palabras_clave})
    
        elif len(word)>0:
            principales_palabras_clave = " ".join(word[0:]).replace(",", ", ").replace("%","").replace("  ", " ").replace("   "," ").replace("    "," ").replace(".","")
            principales_palabras_clave = principales_palabras_clave.strip()
            datos.append({"cluster": cluster, "cantidad_de_palabras_clave": cantidad_de_palabras_clave, "porcentaje_de_palabras_clave": porcentaje_de_palabras_clave, "principales_palabras_clave": principales_palabras_clave})

    df = pd.DataFrame(datos)
    df = df.groupby(["cluster", "cantidad_de_palabras_clave","porcentaje_de_palabras_clave"])["principales_palabras_clave"].agg(lambda x: " ".join(x.astype(str))).reset_index()
        
    return df
