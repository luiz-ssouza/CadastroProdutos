#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:36:39 2017

@author: luiz
"""

#Banco 2
import sqlite3

class Banco():
	def __init__(self):
		self.conexao = sqlite3.connect('banco.db')
		self.createTable()
	
	def createTable(self):
		c = self.conexao.cursor()
		c.execute("""create table if not exists usuarios (
                       id_item integer primary key autoincrement ,
                       cod text,
                       item text,
                       qtd text)""")
		self.conexao.commit()
		c.close()