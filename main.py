#importando bibliotecas 

#Tkinter
from tkinter import * 
from tkinter import Tk, ttk
from tkinter import messagebox

#pillow
from PIL import Image, ImageTk

#barra de progresso tkinter
from tkinter.ttk import Progressbar

#matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

#tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando funções da (operações_no_bd.py)
from operações_no_bd import bar_valores, inserir_categoria,visualizar_categorias, inserir_despesa, inserir_receita, tabela_dados, visualizar_despesa, visualizar_receitas, excluir_despesa, excluir_receita

#cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # azul escuro
co4 = "#403d3d"  # letra
co5 = "#e06636"  # laranja
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # ciano
co8 = "#263238"  # preta
co9 = "#e9edf5"  # cinza

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

#criando janela
janela = Tk()
janela.title('')
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#criando divisões na janela

#frame de cima (cabeçalho)
frame_cima = Frame(janela, width=900, height=50, bg=co3, relief="flat")
frame_cima.grid(row=0, column=0)

#frame do meio (corpo)
frame_meio = Frame(janela, width=900, height=350, bg=co1, relief="raised")
frame_meio.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

#frame de baixo (rodapé)
frame_baixo = Frame(janela, width=900, height=250, bg=co1, relief="flat")
frame_baixo.grid(row=2, column=0, padx=0, pady=1, sticky=NSEW)

#frame do gráfico Pie (Gráfico de pizza)
frame_grafico_pie = Frame(frame_meio, width=580, height=250, bg=co1)
frame_grafico_pie.place(x=415, y=5)


#trabalhando no frame de cima (cabeçalho)

#preparando a imagem
app_img = Image.open('logo.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

#criando o label com a imagem
app_logo = Label(frame_cima, image=app_img, text='Controle Financeiro', width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Poppins 20 bold'), bg=co1, fg=co0)
app_logo.place(x=0, y=0)

#conectando ao banco de dados--------------------------------------------------------------


#definindo tree global
global tree

#função inserir categoria  (nome inserir_categoria_b é somente para diferenciar do nome que está em operações_no_bd)--------------------------
def inserir_categoria_b():
    nome = entrada_nova_categoria.get()

    lista_inserir = [nome]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
# passando lista para a função inserir_gastos presente em operações_no_bd.py
    inserir_categoria(lista_inserir)

    messagebox.showinfo('Sucesso', 'Categoria inserida com sucesso')
    entrada_nova_categoria.delete(0, 'end')

    #coletando os valores da categoria
    categorias_funcao = visualizar_categorias()
    categorias = []

    for i in categorias_funcao:
        categorias.append(i[1])

    #atualizando lista de categorias
    combo_categoria['values'] = (categorias)   

#função inserir receitas---------------------------------------
def inserir_receita_b():
    nome = 'Receita'
    data = entrada_calendario_receita.get()
    quantia = entrada_valores_receita.get()

    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

#chamando a função inserir_receita presente em operações_no_bd.py
    inserir_receita(lista_inserir)
    messagebox.showinfo('Sucesso', 'Receita inserida com sucesso')
    entrada_calendario_receita.delete(0, 'end')
    entrada_valores_receita.delete(0, 'end')
    combo_categoria.delete(0, 'end')

#atualizando dados da tabela e gráficos
    mostrar_tabela()
    grafico_bars()
    grafico_pizza()
    bar_valores()
    porcentagem()
    resumo_total()

#função inserir despesas---------------------------------------
def inserir_despesa_b():
    nome = combo_categoria.get()

    data = entrada_calendario_despesa.get()
    quantia = entrada_valores_despesa.get()

    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

#chamando a função inserir_despesa presente em operações_no_bd.py
    inserir_despesa(lista_inserir)
    messagebox.showinfo('Sucesso', 'Receita inserida com sucesso')
    entrada_calendario_despesa.delete(0, 'end')
    entrada_valores_despesa.delete(0, 'end')
    combo_categoria.delete(0, 'end')
    #entrada_categoria.delete(0, 'end') ----------- removido pois não existe mais podendo ser adc


#atualizando dados da tabela e gráficos
    mostrar_tabela()
    grafico_bars()
    grafico_pizza()
    porcentagem()
    resumo_total()
    bar_valores()

#função excluir despesas---------------------------------------
def excluir_despesa_b():
    try:
        treeview_dados = tree.focus()
        treeview_dicionario = tree.item(treeview_dados)
        treeview_lista = treeview_dicionario['values']
        valor = treeview_lista[0]
        nome = treeview_lista[1]

        if nome == 'Receita':
            excluir_receita([valor])
            messagebox.showinfo('Sucesso', 'Receita excluída com sucesso')

            #atualizando dados da tabela e gráficos
            mostrar_tabela()
            grafico_bars()
            grafico_pizza()
            porcentagem()
            resumo_total()
            bar_valores()  


        else: 
            excluir_despesa([valor])
            messagebox.showinfo('Sucesso', 'Despesa excluída com sucesso')

            #atualizando dados da tabela e gráficos
            mostrar_tabela()
            grafico_bars()
            grafico_pizza()
            porcentagem()
            resumo_total()   
         
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item na tabela')




    







#trabalhando no frame do meio (corpo)

#criando a barra de porcentagem progressiva 
def porcentagem():
    l_nome = Label(frame_meio, text='Porcentagem de Gastos', height=1, anchor=NW, font=('poppins 15 bold'), bg=co1, fg=co0)
    l_nome.place(x=10, y=10)

#estilizando a barra de progresso
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background=co2)
style.configure('TProgressbar', thickness=25)

bar = Progressbar(frame_meio, length=180, style="black.Horizontal.TProgressbar")
bar.place(x=10, y=35)
bar['value'] = 50  # Definindo o valor da barra de progresso

#contagem de progresso da barra de porcentagem
valor = 50
l_porcentagem = Label(frame_meio, text=f'{valor:,.2f}%', anchor=NW, font=('poppins 15 bold'), bg=co1, fg=co0)
l_porcentagem.place(x=200, y=35)

#função para gráfico bars
def grafico_bars():
    lista_categorias = ['renda', 'despesas', 'saldo']
    lista_valores = [5000, 3000, 2000]
    #criando o gráfico
    figura = plt.Figure(figsize=(4,3.45), dpi=60)
    ax = figura.add_subplot(111)

    #escala automática (enable=true, axis='both', tight=none) 
    ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)
    
    #lista para coletar os dados dos plt.patches
    c = 0

    #defina rótulos de barras individuais usando a lista acima
    for i in ax.patches:
        #get_x puxa para esquerda ou direita, get_heigth empurra para cima ou para baixo
        ax.text(
            i.get_x() - .001,
            i.get_height() + .5,
            str('{:,.0f}'.format(lista_valores[c])),fontsize=17,fontstyle='italic',verticalalignment='bottom',color="#474646")
        c += 1
    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_meio)
    canva.get_tk_widget().place(x=10, y=70)

    #função de resulmo total
def resumo_total():
    valor = [500, 300, 200]

#total de renda
    l_linha = Label(frame_meio, text='', width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454',)
    l_linha.place(x=309, y=52)
    l_sumario = Label(frame_meio, text='Total De Renda Mensal   '.upper(), height=1, anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frame_meio, text='R$ {:,.2f}'.format(valor[0]), height=1, anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    l_sumario.place(x=309, y=70)

#total de despesa
    l_linha = Label(frame_meio, text='', width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454',)
    l_linha.place(x=309, y=132)
    l_sumario = Label(frame_meio, text='Total De Despesa Mensal '.upper(), height=1, anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frame_meio, text='R$ {:,.2f}'.format(valor[1]), height=1, anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    l_sumario.place(x=309, y=150)

#total de saldo
    l_linha = Label(frame_meio, text='', width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454',)
    l_linha.place(x=309, y=212)
    l_sumario = Label(frame_meio, text='Total De Saldo Em Caixa   '.upper(), height=1, anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_sumario.place(x=309, y=195)
    l_sumario = Label(frame_meio, text='R$ {:,.2f}'.format(valor[2]), height=1, anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    l_sumario.place(x=309, y=230)
    
    #função grafico pizza
def grafico_pizza():
    #fazendo figuras e atribuindo objetos ao eixo
    figura = plt.figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)
    #dados
    lista_categorias = ['renda', 'despesas', 'saldo']
    lista_valores = [500, 300, 200]

    #criando o gráfico (apenas expande a 2° fatia)

    explode = []
    for i in lista_categorias:
        explode.append(0.05) 

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_grafico_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)

#função resumo total
porcentagem()
grafico_bars()
resumo_total()
grafico_pizza()

#criando frame no frame de baixo (rodapé)
frame_renda = Frame(frame_baixo, width=350, height=220, bg=co1, )
frame_renda.grid(row=0, column=0, padx=5, pady=10)

frame_operacoes = Frame(frame_baixo, width=230, height=220, bg=co3, )
frame_operacoes.grid(row=0, column=1, padx=5, pady=10)

frame_configuracao = Frame(frame_baixo, width=230, height=220, bg=co3, )
frame_configuracao.grid(row=0, column=2, padx=5, pady=10)

#criando o label do frame de baixo (rodapé)
titulo_tabela = Label(frame_meio,text='Tabela Receitas e Despesas', anchor=NW, font=('Poppins 20 bold'), bg=co1, fg=co0)
titulo_tabela.place(x=5, y=300)

#função para mostrar tabela rendas e despesas
def mostrar_tabela():
    tabela_head = ['ID', 'Categoria', 'Data', 'Quantia']

    lista_itens = tabela_dados() 

    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended", columns=tabela_head, show="headings")
    #barra de rolagem vertical
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    #barra de rolagem horizontal
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns') 
    hsb.grid(column=0, row=1, sticky='ew') 

    hd = ['center', 'center', 'center', 'center']
    h = [30, 150, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        
        #define a largura de cada coluna do cabeçalho
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

#inserindo despesas na tabela
l_descricao = Label(frame_operacoes, text='Insira Novas Despesas', height=1, anchor=NW, font=('Poppins 10 bold'), bg=co3, fg=co1)
l_descricao.place(x=5, y=10)

#categoria
l_categoria = Label(frame_operacoes, text='Categoria', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_categoria.place(x=5, y=40)

#seleção de categoria
categoria_funcao = visualizar_categorias()
categoria = []

for i in categoria_funcao:
    categoria.append(i[1])

#combobox categoria
combo_categoria = ttk.Combobox(frame_operacoes, width=10, font=('Ivy 10'))
combo_categoria['values'] = (categoria)
combo_categoria.place(x=110, y=41)

#data da despesa
l_calendario_despesa = Label(frame_operacoes, text='Data', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_calendario_despesa.place(x=10, y=70)
entrada_calendario_despesa = DateEntry(frame_operacoes, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
entrada_calendario_despesa.place(x=110, y=71)

#valor da despesa
l_valor_despesa = Label(frame_operacoes, text='Quantia Total', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_valor_despesa.place(x=10, y=100)
entrada_valores_despesa = Entry(frame_operacoes, width=14, justify='left', relief='solid', font=('Ivy 10'))
entrada_valores_despesa.place(x=110, y=101)

#botão inserir despesa
img_add_despesa = Image.open('bt add.png')
img_add_despesa = img_add_despesa.resize((15, 15))
img_add_despesa = ImageTk.PhotoImage(img_add_despesa)
botao_inserir_despesa = Button(frame_operacoes, command=inserir_despesa_b, image=img_add_despesa, text=' Adicionar'.upper(), width=80, compound=LEFT, anchor=NW , overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_inserir_despesa.place(x=110, y=131)

#botão excluir 
l_excluir = Label(frame_operacoes, text='Excluir Ação', height=1, anchor=NW, font=('Poppins 10 bold'), bg='#CA0909', fg=co1)
l_excluir.place(x=10, y=190)

img_deletar = Image.open('bt delet.png')
img_deletar = img_deletar.resize((15, 15))
img_deletar = ImageTk.PhotoImage(img_deletar)
botao_deletar = Button(frame_operacoes, command=excluir_despesa_b, image=img_deletar, text=' Deletar'.upper(), width=80, compound=LEFT, anchor=NW , overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_deletar.place(x=110, y=190)

#inserindo receitas na tabela
l_descricao = Label(frame_configuracao, text='Insira Novas Receitas', height=1, anchor=NW, font=('Poppins 10 bold'), bg=co3, fg=co1)
l_descricao.place(x=10, y=10)

#valor da receita
l_valor_receita = Label(frame_configuracao, text='Quantia Total', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_valor_receita.place(x=10, y=40)
entrada_valores_receita = Entry(frame_configuracao, width=14, justify='left', relief='solid', font=('Ivy 10'))
entrada_valores_receita.place(x=110, y=41)

#data da receita
l_calendario_receita = Label(frame_configuracao, text='Data', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_calendario_receita.place(x=10, y=70)
entrada_calendario_receita = DateEntry(frame_configuracao, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
entrada_calendario_receita.place(x=110, y=71)

#categoria da receita
#l_categoria = Label(frame_configuracao, text='Categoria', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
#l_categoria.place(x=5, y=100)
#entrada_categoria = Entry(frame_configuracao, width=14, justify='left', relief='solid', font=('Ivy 10'))
#entrada_categoria.place(x=110, y=101)


#botão inserir receita
img_add_receita = Image.open('bt add.png')
img_add_receita = img_add_receita.resize((15, 15))
img_add_receita = ImageTk.PhotoImage(img_add_receita)
botao_inserir_receita = Button(frame_configuracao, command=inserir_receita_b, image=img_add_despesa, text=' Adicionar'.upper(), width=80, compound=LEFT, anchor=NW , overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_inserir_receita.place(x=110, y=131)

# nova categoria
l_nova_categoria = Label(frame_configuracao, text=' Nova Categoria', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_nova_categoria.place(x=5, y=160)
entrada_nova_categoria = Entry(frame_configuracao, width=14, justify='left', relief='solid', font=('Ivy 10'))
entrada_nova_categoria.place(x=110, y=161)

#botão inserir categoria nova
img_add_nova_categoria = Image.open('bt add.png')
img_add_nova_categoria = img_add_nova_categoria.resize((15, 15))
img_add_nova_categoria = ImageTk.PhotoImage(img_add_nova_categoria)
botao_inserir_nova_categoria = Button(frame_configuracao, command=inserir_categoria_b, image=img_add_nova_categoria, text=' Adicionar'.upper(), width=80, compound=LEFT, anchor=NW , overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_inserir_nova_categoria.place(x=110, y=191)

mostrar_tabela()
janela.mainloop()




#continuar aula 16
