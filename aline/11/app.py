import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import math

# Funções matemáticas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    else:
        return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: Raiz quadrada de número negativo"
    else:
        return math.sqrt(a)

# Funções de memória
memoria = None

def adicionar_memoria(valor):
    global memoria
    memoria = valor

def limpar_memoria():
    global memoria
    memoria = None

def consultar_memoria():
    return memoria

# Interface gráfica principal
app = tk.Tk()
app.title("Calculadora Avançada")

# Funções básicas
frame_basico = ttk.LabelFrame(app, text="Funcionalidades Básicas")
frame_basico.grid(row=0, column=0, padx=10, pady=5)

btn_soma = ttk.Button(frame_basico, text="Soma")
btn_soma.grid(row=0, column=0, padx=5, pady=5)

btn_subtracao = ttk.Button(frame_basico, text="Subtração")
btn_subtracao.grid(row=0, column=1, padx=5, pady=5)

btn_multiplicacao = ttk.Button(frame_basico, text="Multiplicação")
btn_multiplicacao.grid(row=1, column=0, padx=5, pady=5)

btn_divisao = ttk.Button(frame_basico, text="Divisão")
btn_divisao.grid(row=1, column=1, padx=5, pady=5)

# Funções avançadas
frame_avancado = ttk.LabelFrame(app, text="Funcionalidades Avançadas")
frame_avancado.grid(row=1, column=0, padx=10, pady=5)

btn_potencia = ttk.Button(frame_avancado, text="Potência")
btn_potencia.grid(row=0, column=0, padx=5, pady=5)

btn_raiz_quadrada = ttk.Button(frame_avancado, text="Raiz Quadrada")
btn_raiz_quadrada.grid(row=0, column=1, padx=5, pady=5)

# Funções de memória
frame_memoria = ttk.LabelFrame(app, text="Funcionalidades de Memória")
frame_memoria.grid(row=2, column=0, padx=10, pady=5)

btn_adicionar_memoria = ttk.Button(frame_memoria, text="Adicionar à Memória")
btn_adicionar_memoria.grid(row=0, column=0, padx=5, pady=5)

btn_consultar_memoria = ttk.Button(frame_memoria, text="Consultar Memória")
btn_consultar_memoria.grid(row=0, column=1, padx=5, pady=5)

btn_limpar_memoria = ttk.Button(frame_memoria, text="Limpar Memória")
btn_limpar_memoria.grid(row=1, column=0, padx=5, pady=5)

# Funções de Engenharia Civil
frame_engenharia = ttk.LabelFrame(app, text="Funcionalidades de Engenharia Civil")
frame_engenharia.grid(row=0, column=1, rowspan=3, padx=10, pady=5)

btn_calculos_estruturais = ttk.Button(frame_engenharia, text="Cálculos Estruturais")
btn_calculos_estruturais.grid(row=0, column=0, padx=5, pady=5)

btn_topografia = ttk.Button(frame_engenharia, text="Topografia")
btn_topografia.grid(row=1, column=0, padx=5, pady=5)

# Funções para funções matemáticas
frame_matematica = ttk.LabelFrame(app, text="Funcionalidades Matemáticas")
frame_matematica.grid(row=3, column=0, padx=10, pady=5)

btn_transformada_fourier = ttk.Button(frame_matematica, text="Transformada de Fourier")
btn_transformada_fourier.grid(row=0, column=0, padx=5, pady=5)

btn_integral_numerica = ttk.Button(frame_matematica, text="Integração Numérica")
btn_integral_numerica.grid(row=0, column=1, padx=5, pady=5)

btn_derivada_numerica = ttk.Button(frame_matematica, text="Derivada Numérica")
btn_derivada_numerica.grid(row=1, column=0, padx=5, pady=5)

# Funções para hidráulica e saneamento
frame_hidraulica = ttk.LabelFrame(app, text="Funcionalidades de Hidráulica e Saneamento")
frame_hidraulica.grid(row=3, column=1, padx=10, pady=5)

btn_fluxo_tubulacao = ttk.Button(frame_hidraulica, text="Fluxo em Tubulação")
btn_fluxo_tubulacao.grid(row=0, column=0, padx=5, pady=5)

btn_fluxo_canal = ttk.Button(frame_hidraulica, text="Fluxo em Canal")
btn_fluxo_canal.grid(row=0, column=1, padx=5, pady=5)

# Eventos de botões (ainda a serem implementados)
def on_btn_click():
    messagebox.showinfo("Aviso", "Esta funcionalidade ainda será implementada.")

btn_soma.config(command=on_btn_click)
btn_subtracao.config(command=on_btn_click)
btn_multiplicacao.config(command=on_btn_click)
btn_divisao.config(command=on_btn_click)
btn_potencia.config(command=on_btn_click)
btn_raiz_quadrada.config(command=on_btn_click)
btn_adicionar_memoria.config(command=on_btn_click)
btn_consultar_memoria.config(command=on_btn_click)
btn_limpar_memoria.config(command=on_btn_click)
btn_calculos_estruturais.config(command=on_btn_click)
btn_topografia.config(command=on_btn_click)
btn_transformada_fourier.config(command=on_btn_click)
btn_integral_numerica.config(command=on_btn_click)
btn_derivada_numerica.config(command=on_btn_click)
btn_fluxo_tubulacao.config(command=on_btn_click)
btn_fluxo_canal.config(command=on_btn_click)

app.mainloop()
