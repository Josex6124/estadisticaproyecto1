import numpy as np
import pandas as pd

# Cargar el dataset desde un archivo CSV
file_path = '/Users/joseluismac/PycharmProjects/pythonProject/dataset.csv'
data = pd.read_csv(file_path)

# Seleccionar la variable 'Sleep Duration'
sleep_duration = data['Sleep Duration']

# Determinar el número de clases utilizando la regla de Sturges
n_clases = int(np.ceil(1 + 3.322 * np.log10(len(sleep_duration))))

# Crear la tabla de frecuencia
tabla_frecuencia, bins = np.histogram(sleep_duration, bins=n_clases)

# Crear un DataFrame con los intervalos de clase y la frecuencia absoluta
intervalos = pd.IntervalIndex.from_breaks(bins)
frecuencia_absoluta = pd.Series(tabla_frecuencia, index=intervalos)

# Calcular la frecuencia acumulada y la marca de clase
frecuencia_acumulada = frecuencia_absoluta.cumsum()
marca_clase = frecuencia_absoluta.index.map(lambda x: x.mid)

# Crear la tabla de frecuencia completa
tabla_frecuencia_df = pd.DataFrame({
    'Intervalo de Clase': frecuencia_absoluta.index,
    'Frecuencia Absoluta': frecuencia_absoluta,
    'Frecuencia Acumulada': frecuencia_acumulada,
    'Marca de Clase': marca_clase
})

# Especificar la ruta del archivo de texto donde deseas guardar el resultado
output_file = '/Users/joseluismac/PycharmProjects/pythonProject/tabla_frecuencia.txt'

# Guardar el DataFrame en el archivo de texto
with open(output_file, 'w') as f:
    f.write(tabla_frecuencia_df.to_string(index=False))

print(f'Se ha guardado la tabla de frecuencia en: {output_file}')

