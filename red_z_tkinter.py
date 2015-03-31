# coding=UTF-8
from Tkinter import *
import MySQLdb
from datetime import datetime



class Passwords:

	def __init__(self,toplevel):
		self.frame1=Frame(toplevel)
		self.frame1.pack()
		self.frame2=Frame(toplevel)
		self.frame2.pack()
		self.frame3=Frame(toplevel)
		self.frame3.pack()
		self.frame4=Frame(toplevel)
		self.frame4.pack()
		self.frame5=Frame(toplevel)
		self.frame5.pack()
		self.frame6=Frame(toplevel,pady=10)
		self.frame6.pack()

		fonte1=('Verdana','10','bold')
		Label(self.frame1,text='Usuario: ',
		font=fonte1,width=20).pack(side=LEFT)
		self.usuario=Entry(self.frame1,width=10,
		font=fonte1)
		self.usuario.focus_force()
		self.usuario.pack(side=LEFT)

		Label(self.frame2,text='Senha: ',
		font=fonte1,width=20).pack(side=LEFT)
		self.senha=Entry(self.frame2,width=10,show='*',
		font=fonte1)
		self.senha.pack(side=LEFT)

		Label(self.frame3,text='Nome do Banco: ',
		font=fonte1,width=20).pack(side=LEFT)
		self.banco=Entry(self.frame3,width=10,
		font=fonte1)
		self.banco.pack(side=LEFT)

		Label(self.frame4,text='Ip do servidor: ',
		font=fonte1,width=20).pack(side=LEFT)
		self.ip_servidor=Entry(self.frame4,width=10,
		font=fonte1)
		self.ip_servidor.pack(side=LEFT)

		Label(self.frame5,text='ID do caixa: ',
		font=fonte1,width=20).pack(side=LEFT)
		self.id_caixa=Entry(self.frame5,width=10,
		font=fonte1)
		self.id_caixa.pack(side=LEFT)

		self.confere=Button(self.frame6, font=fonte1, text='Executar',
		bg='pink', command=self.execute_sql)
		self.confere.pack()
		self.msg=Label(self.frame6,font=fonte1, height=3,text='Aperte em executar')
		self.msg.pack()

	
	def execute_sql(self):

		nome_arquivo = str(	datetime.now())[0:10]
		arq = open(nome_arquivo, 'a')
		
		try:
			user_banco = self.usuario.get()
			senha = self.senha.get()
			banco = self.banco.get()
			ip_servidor = self.ip_servidor.get()
			caixa = (self.id_caixa.get())
			id_caixa = int(caixa)

			arq.write('%s usuario do banco = %s,  senha do banco = %s, nome do banco = %s, servidor = %s, id do caixa = %s  \n'%(str(datetime.now())[0:19],
				user_banco, senha, banco, ip_servidor, caixa))

		
			con = MySQLdb.connect(user = user_banco, passwd = senha, db = banco, host = ip_servidor)

			c = con.cursor()

			gt_final = c.execute('select grande_total_final from %s.reducaoz where caixa_caixa_id_oid = %i' %(banco, id_caixa))
			lista_gt_final =  c.fetchall()
			id_red =  c.execute('select reducaoz_id from %s.reducaoz where caixa_caixa_id_oid = %i' %(banco,id_caixa))
			lista_reducaoz_id = c.fetchall()

			cont_gt_final = 0
			cont_id_reducaoz = 1
			for cont_gt_final in range(len(lista_gt_final)-1):
				update = 'update %s.reducaoz set grande_total_inicial =%f  where reducaoz_id = %i'%(banco, 
					lista_gt_final[cont_gt_final][0], lista_reducaoz_id[cont_id_reducaoz][0])
				c.execute(update)
				con.commit()
				arq.write(str(datetime.now())[0:19] + ' ' + update + '\n')
				cont_gt_final +=1
				cont_id_reducaoz += 1

			self.msg['text']='Concluido'
			self.msg['fg']='darkgreen'
			
			arq.write(str(datetime.now())[0:19] + ' ' + 'Update realizado com sucesso \n' )
		except Exception as erro:
			arq.write('%s usuario do banco = %s,  senha do banco = %s, nome do banco = %s, servidor = %s, id do caixa = %s  \n'%(str(datetime.now())[0:19],
				user_banco, senha, banco, ip_servidor, caixa))
			arq.write(str(datetime.now())[0:19] + str(erro) + '\n')
		 	self.msg['text']='Favo conferir os dados'
		 	self.msg['fg']='darkred'






instancia=Tk()
Passwords(instancia)
instancia.mainloop()