#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:54:10 2017

@author: luiz
"""

from Itens import itens
from tkinter import *

class Application:
	def __init__(self, master=None):
		self.fonte = ("Verdana", "8")
		
		self.container1 = Frame(master)
		self.container1["pady"] = 10
		self.container1.pack()
		
		self.container2 = Frame(master)
		self.container2["padx"] = 20
		self.container2["pady"] = 5
		self.container2.pack()
		self.container3 = Frame(master)
		self.container3["padx"] = 20
		self.container3["pady"] = 5
		self.container3.pack()
		self.container4 = Frame(master)
		self.container4["padx"] = 20
		self.container4["pady"] = 5
		self.container4.pack()
		self.container5 = Frame(master)
		self.container5["padx"] = 20
		self.container5["pady"] = 5
		self.container5.pack()
		self.container8 = Frame(master)
		self.container8["padx"] = 20
		self.container8["pady"] = 10
		self.container8.pack()
		self.container9 = Frame(master)
		self.container9["pady"] = 15
		self.container9.pack()
		
		self.titulo = Label(self.container1, text="Informe os dados :")
		self.titulo["font"] = ("Calibri", "9", "bold")
		self.titulo.pack ()
		
		self.lblid_item = Label(self.container2, text="id Item:", font=self.fonte, width=10)
		self.lblid_item.pack(side=LEFT)
		
		self.txtid_item = Entry(self.container2)
		self.txtid_item["width"] = 10
		self.txtid_item["font"] = self.fonte
		self.txtid_item.pack(side=LEFT)
		
		self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
		self.btnBuscar["command"] = self.buscarUsuario
		self.btnBuscar.pack(side=RIGHT)
		
		self.lblcod = Label(self.container3, text="Cod:", font=self.fonte, width=10)
		self.lblcod.pack(side=LEFT)
		
		self.txtcod = Entry(self.container3)
		self.txtcod["width"] = 25
		self.txtcod["font"] = self.fonte
		self.txtcod.pack(side=LEFT)
		
		self.lblitem = Label(self.container4, text="Item:", font=self.fonte, width=10)
		self.lblitem.pack(side=LEFT)
		
		self.txtitem = Entry(self.container4)
		self.txtitem["width"] = 25
		self.txtitem["font"] = self.fonte
		self.txtitem.pack(side=LEFT)
		
		self.lblqtd= Label(self.container5, text="Quantidade:", font=self.fonte, width=10)
		self.lblqtd.pack(side=LEFT)
		
		self.txtqtd = Entry(self.container5)
		self.txtqtd["width"] = 25
		self.txtqtd["font"] = self.fonte
		self.txtqtd.pack(side=LEFT)
		
		
		self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
		self.bntInsert["command"] = self.inserirItem
		self.bntInsert.pack (side=LEFT)
		
		self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
		self.bntAlterar["command"] = self.alterarItem
		self.bntAlterar.pack (side=LEFT)

		self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
		self.bntExcluir["command"] = self.excluirItem
		self.bntExcluir.pack(side=LEFT)
		
		self.lblmsg = Label(self.container9, text="")

		self.lblmsg["font"] = ("Verdana", "9", "italic")
		self.lblmsg.pack()
		
	def inserirItem(self):
		
		user = itens()
		
		user.cod = self.txtcod.get()
		user.item = self.txtitem.get()
		user.qtd = self.txtqtd.get()
		
		self.lblmsg["text"] = user.insertItem()
		
		self.txtid_item.delete(0, END)
		self.txtcod.delete(0, END)
		self.txtitem.delete(0, END)
		self.txtqtd.delete(0, END)
	
	def alterarItem(self):
		
		user = itens()
		
		user.id_item = self.txtid_item.get()
		user.cod = self.txtcod.get()
		user.item = self.txtitem.get()
		user.qtd = self.txtqtd.get()
		
		self.lblmsg["text"] = user.updateItem()
		
		self.txtid_item.delete(0, END)
		self.txtcod.delete(0, END)
		self.txtitem.delete(0, END)
		self.txtqtd.delete(0, END)
		
		
	def excluirItem(self):
		
		user = itens()
		
		user.id_item = self.txtid_item.get()
		
		self.lblmsg["text"] = user.deleteItem()
		
		self.txtid_item.delete(0, END)
		self.txtcod.delete(0, END)
		self.txtitem.delete(0, END)
		self.txtqtd.delete(0, END)
		
	def buscarUsuario(self):
		
		user = itens()
		
		id_item = self.txtid_item.get()
		
		self.lblmsg["text"] = user.selectItem(id_item)
		
		self.txtid_item.delete(0, END)
		self.txtid_item.insert(INSERT, user.id_item)
		
		self.txtcod.delete(0, END)
		self.txtcod.insert(INSERT, user.cod)
		
		self.txtitem.delete(0, END)
		self.txtitem.insert(INSERT,user.item)
		
		self.txtqtd.delete(0, END)
		self.txtqtd.insert(INSERT, user.qtd)
 
root = Tk()
Application(root)
root.mainloop()