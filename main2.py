import numpy as np
import pandas as pd

# Cargar el dataset desde un archivo CSV
file_path = '/Users/joseluismac/PycharmProjects/pythonProject/dataset.csv'  # Actualiza la ruta al archivo CSV
data = pd.read_csv(file_path)

# Seleccionar la variable 'Sleep Duration'
sleep_duration = data['Sleep Duration']

# Determinar el número de clases utilizando la regla de Sturges
n_clases = int(np.ceil(1 + 3.322 * np.log10(len(sleep_duration))))

# Calcular la tabla de frecuencia y los intervalos
tabla_frecuencia, bins = np.histogram(sleep_duration, bins=n_clases)
intervalos = pd.IntervalIndex.from_breaks(bins)

# Calcular el punto medio (marca de clase) de cada intervalo
marca_clase = intervalos.map(lambda x: x.mid)

# Crear un DataFrame con los intervalos de clase y la frecuencia absoluta
frecuencia_absoluta = pd.Series(tabla_frecuencia, index=intervalos)

# Calcular la suma total de frecuencias
N = frecuencia_absoluta.sum()

# Calcular la frecuencia acumulada
frecuencia_acumulada = frecuencia_absoluta.cumsum()

# Encontrar el índice del intervalo que contiene la mediana
index_mediana = np.argmax(frecuencia_acumulada >= N/2)  # Índice del primer intervalo con frecuencia acumulada mayor o igual a N/2
intervalo_mediana = intervalos[index_mediana]
L = intervalo_mediana.left
f = frecuencia_absoluta[intervalo_mediana]
F = frecuencia_acumulada.iloc[index_mediana - 1] if index_mediana > 0 else 0
c = intervalo_mediana.length

# Calcular la mediana
mediana = L + ((N/2 - F) / f) * c

# Encontrar la moda (intervalo con la mayor frecuencia absoluta)
moda_intervalo = frecuencia_absoluta.idxmax()
moda = moda_intervalo.mid

# Calcular la media aritmética
media_aritmetica = np.sum(frecuencia_absoluta * marca_clase) / N

# Calcular la varianza y desviación estándar
varianza = np.sum(frecuencia_absoluta * (marca_clase - media_aritmetica)**2) / N
desviacion_estandar = np.sqrt(varianza)

# Especificar la ruta del archivo de texto donde deseas guardar los resultados
output_file = '/Users/joseluismac/PycharmProjects/pythonProject/medidas_estadisticas.txt'

# Guardar las medidas estadísticas en el archivo de texto
with open(output_file, 'w') as f:
    f.write(f'Media aritmética: {media_aritmetica:.2f}\n')
    f.write(f'Mediana: {mediana:.2f}\n')
    f.write(f'Moda: {moda:.2f}\n')
    f.write(f'Varianza: {varianza:.2f}\n')
    f.write(f'Desviación estándar: {desviacion_estandar:.2f}\n')

print(f'Se han guardado las medidas estadísticas en: {output_file}')
