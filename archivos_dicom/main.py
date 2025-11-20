from codigo import ProcesadorDICOM
import pandas as pd



def main():
    #Crea el entorno interactivo
    procesador = ProcesadorDICOM()

    ruta= input("Ingrese la ruta del directorio que contiene los archivos DICOM: ")

    procesador.cargar_archivos(ruta)

    dataframe= procesador.crear_dataframe_metadatos()

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 300)
    pd.set_option('display.expand_frame_repr', False)

    print("\n===== DATAFRAME DE METADATOS =====\n")
    print(dataframe.to_string(index=True))
    return dataframe


if __name__ == "__main__":
    df=main()
    
    #Nota: para que la tabla se visualice bien abrir en el explorador de variables 
