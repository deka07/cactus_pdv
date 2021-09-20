import sqlite3

class Banco_db:

   def conectar_db(self):
      self.banco = sqlite3.connect('adailto.db')
      self.cursor = self.banco.cursor()


   def select_db(self):  
      self.conectar_db()
      self.cursor.execute("SELECT * fROM tb_produtos")
      self.cursor.fetchall()
      self.cursor.close()

   def add_produto(self):
      pass
