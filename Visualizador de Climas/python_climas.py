import requests
import tkinter as tk

janela = tk.Tk()

# ----- entrys -----
entry_1 = tk.Entry(janela)
entry_1.insert(0, 'Recife')

chave = '5ee3c16cd323296e8f660dfabebd0ccc'
cidade = tk.StringVar(janela, 'Recife')
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade.get()}&appid={chave}&lang=pt_br'
site = requests.get(link).json()


def atualizar_dados():
    global link, site, tempo, temperatura, pressao, humidade
    cidade.set(entry_1.get())
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade.get()}&appid={chave}&lang=pt_br'
    site = requests.get(link).json()
    tempo.set(site['weather'][0]['description'])
    temperatura.set(f"{site['main']['temp'] - 273.15:.2f}°C")
    pressao.set(f"{site['main']['pressure']} hPa")
    humidade.set(f"{site['main']['humidity']} g/kg")
    # print(link, '\n', site['weather'][0]['description'])


tempo = tk.StringVar(janela, site['weather'][0]['description'])
temperatura = tk.StringVar(janela, f"{site['main']['temp'] - 273.15:.2f}°C")
pressao = tk.StringVar(janela, f"{site['main']['pressure']} hPa")
humidade = tk.StringVar(janela, f"{site['main']['humidity']} g/kg")

# front end
fonte = 'Calibri 12 bold'
fonte2 = 'Calibri 12'

# ----- janela opções -----
janela_x_pos = int(janela.winfo_screenwidth()/2 - 100)
janela_y_pos = int(janela.winfo_screenheight()/2 - 200)

janela.title('Info_Clim')
janela.configure(bg='#87CEFA')
janela.resizable(False, False)
janela.iconbitmap('globo1.ico')
janela.geometry(f'+{janela_x_pos}+{janela_y_pos}')
# ----- labels -----
# titulos
label_1 = tk.Label(janela, text='Local: ', font=fonte, bg='#87CEFA')
label_2 = tk.Label(janela, text='Clima: ', font=fonte, bg='#87CEFA')
label_3 = tk.Label(janela, text='Temperatura: ', font=fonte, bg='#87CEFA')
label_4 = tk.Label(janela, text='pressão: ', font=fonte, bg='#87CEFA')
label_5 = tk.Label(janela, text='Humidade: ', font=fonte, bg='#87CEFA')
# informações
label_6 = tk.Label(janela, textvariable=tempo, font=fonte2, bg='#87CEFA')
label_7 = tk.Label(janela, textvariable=temperatura, font=fonte2, bg='#87CEFA')
label_8 = tk.Label(janela, textvariable=pressao, font=fonte2, bg='#87CEFA')
label_9 = tk.Label(janela, textvariable=humidade, font=fonte2, bg='#87CEFA')

# ----- buttons -----
button_1 = tk.Button(janela, text='Verificar',
                     font=fonte,
                     bg='green',
                     fg='white',
                     command=lambda: atualizar_dados()
                     )
# ----- organizar -----
# titulos
label_1.grid(row=0, column=0, stick=tk.W)
label_2.grid(row=2, column=0, stick=tk.W)
label_3.grid(row=3, column=0, stick=tk.W)
label_4.grid(row=4, column=0, stick=tk.W)
label_5.grid(row=5, column=0, stick=tk.W)
# buttons
button_1.grid(row=1, column=1)
# entrys
entry_1.grid(row=0, column=1, stick=tk.W)
# informações
label_6.grid(row=2, column=1, stick=tk.W)
label_7.grid(row=3, column=1, stick=tk.W)
label_8.grid(row=4, column=1, stick=tk.W)
label_9.grid(row=5, column=1, stick=tk.W)

janela.mainloop()
