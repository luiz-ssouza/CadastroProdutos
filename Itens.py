#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:40:06 2017

@author: luiz
"""

from BancoDados import Banco

class itens(object):
	def __init__(self, id_item = 0, cod = "", item = "", qtd = 0):
		self.info = {}
		self.id_item = id_item
		self.cod = cod
		self.item = item
		self.qtd = qtd
	
	def insertItem(self):
		
		banco = Banco()
		try:
			c = banco.conexao.cursor()
			c.execute("insert into itens (cod, item, qtd) values ('" + self.cod + "', '" + self.item + "', '" + self.qtd +"' )")
			banco.conexao.commit()
			c.close()
			
			return "Usuário cadastrado com sucesso!"
		except:
			return "Ocorreu um erro na inserção do usuário"
		
	def updateItem(self):
		
		banco = Banco()
		try:
			c = banco.conexao.cursor()
			c.execute("update itens set cod = '" + self.cod + "', item = '" + self.item + "', qtd = '" + self.qtd +  "' where id_item = " + self.id_item + " ")
			banco.conexao.commit()
			c.close()
			return "Usuário atualizado com sucesso!"
		except:
			return "Ocorreu um erro na alteração do usuário"
		
	def deleteItem(self):
		banco = Banco()
		try:
			c = banco.conexao.cursor()
			c.execute("delete from itens where id_item = " + self.id_itemo + " ")
			banco.conexao.commit()
			c.close()
			return "Usuário excluído com sucesso!"
		except:
			return "Ocorreu um erro na exclusão do usuário" 

	def selectItem(self, id_item):
		
		banco = Banco()
		try:
			c = banco.conexao.cursor()
			c.execute("select * from itens where id_item = " + id_item + "  ")
			
			for linha in c:
				self.idusuario = linha[0]
				self.nome = linha[1]
				self.telefone = linha[2]
				self.email = linha[3]
				self.usuario = linha[4]
				self.senha = linha[5]
				
				c.close()
			return "Busca feita com sucesso!"
		
		except:
			return "Ocorreu um erro na busca do usuário"
  