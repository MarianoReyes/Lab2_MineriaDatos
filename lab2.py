import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

url = 'breast-cancer-wisconsin.data'

names = ['id', 'clump_thickness', 'uniformity_of_cell_size', 'uniformity_of_cell_shape', 'marginal_adhesion', 'single_epithelial_cell_size',
         'bare_nuclei', 'bland_chromatin', 'normal_nucleoli', 'mitoses', 'class']

df = pd.read_csv(url, names=names)

# Analisis Exploratorio
# 1.1
'''
print(df.head())
print(df.dtypes)
'''
# 1.3
'''
# Histogramas
plt.hist(df['clump_thickness'])
plt.title('Distribución de clump_thickness')
plt.xlabel('clump_thickness')
plt.ylabel('Frecuencia')
plt.show()
'''
'''
# Diagramas de caja
sns.boxplot(x='class', y='clump_thickness', data=df)
plt.title('Distribución de clump_thickness según la clase')
plt.xlabel('class')
plt.ylabel('clump_thickness')
plt.show()
'''
'''
# Gráficos de dispersión
plt.scatter(df['uniformity_of_cell_size'], df['uniformity_of_cell_shape'])
plt.title('Relación entre uniformity_of_cell_size y uniformity_of_cell_shape')
plt.xlabel('uniformity_of_cell_size')
plt.ylabel('uniformity_of_cell_shape')
plt.show()
'''
'''
# Gráfico de densidad
sns.kdeplot(df['mitoses'], shade=True)
plt.title('Distribución de mitoses')
plt.xlabel('mitoses')
plt.ylabel('Densidad')
plt.show()
# Calcular el número de casos por cada clase
class_count = df['class'].value_counts()

# Graficar los valores en un gráfico de pie
labels = ['Benigno', 'Maligno']
colors = ['lightblue', 'pink']
plt.pie(class_count, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Proporción de casos')
plt.show()
'''
# 1.4
'''
# Seleccionar solo las columnas numéricas
numeric_cols = df.drop(['class'], axis=1).select_dtypes(include='number')

# Calcular la matriz de correlación
corr_matrix = numeric_cols.corr()

# Visualizar la matriz de correlación con un mapa de calor
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de correlación de las variables numéricas')
plt.show()
'''
# 1.5
'''
# Gráfico de barras
plt.figure(figsize=(8, 6))
sns.countplot(x="bare_nuclei", data=df)
plt.title('Distribución de la variable "bare nuclei"')
plt.xlabel('bare nuclei')
plt.ylabel('Número de casos')
plt.show()

# Tabla de frecuencia
bare_nuclei_freq = df['bare_nuclei'].value_counts()
print('Tabla de frecuencia de la variable "bare nuclei":\n')
print(bare_nuclei_freq)

# Tabla de proporción
bare_nuclei_prop = df['bare_nuclei'].value_counts(normalize=True)
print('\nTabla de proporción de la variable "bare nuclei":\n')
print(bare_nuclei_prop)
'''
# 1.6
'''
# Eliminar filas con valores nulos
df = df.dropna()

# Eliminar outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Guardar dataframe resultante en un nuevo archivo CSV
df.to_csv('cleaned_data.csv', index=False)
'''
