from tkinter import * 
#Importar libreria matplotlib para mostrar gráficos de la contabilizacion de predicción
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pandas import DataFrame

def grafica_barras_circular(x,y):

        root = Tk()
        #root.configure(background='black')
        root.title("Gráficos")
        framecontenedor = Frame(width="600", height="130", bg="#28E469")
        framecontenedor.pack(side="top", anchor='n', padx=1, pady=1)
        #------- Sección Gráficos
        framegraficos = Frame(bg="#949292", width="215", height="620")
        framegraficos.pack (side="bottom", anchor='n',padx=1,pady=1)

        #Gráfico 
        Data1 = {'Clases': x, 'Encuesta': y}
        df1 = DataFrame(Data1, columns= ['Ciudades', '# Usuarios'])
        df1 = df1[['Clases', 'Encuesta']].groupby('Clases').sum()
        grafico1 = plt.Figure(figsize=(6,5), dpi=50)
        barras = grafico1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(grafico1, framegraficos)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        df1.plot(kind='bar', legend=True, ax=barras)
        barras.set_title('Cantidad Por Ciudades')

        #Grafico #2
        explode = (0.01, 0.01, 0.01)
        grafico2 = plt.Figure(figsize=(6,5), dpi=50)
        circulo = grafico2.add_subplot(111)
        circulo.pie(y, explode=explode, labels=x, autopct='%1.1f%%', shadow=True, startangle=90)
        pie1 = FigureCanvasTkAgg(grafico2, framegraficos) 
        pie1.get_tk_widget().pack()
        circulo.set_title("Gráfico Circular - Porcentajes Totales")

        root.mainloop()

