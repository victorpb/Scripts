# coding=UTF-8

import 	MySQLdb

user_banco = raw_input('Digite o usuário do banco: ')

senha = raw_input('Digite a senha do banco: ')

banco = raw_input('Digite o nome do banco de dados: ')

ip_servidor = raw_input('Digite o ip da máquina do MySQL: ')

id_caixa = input('Digite o ID do caixa: ')
#string_conexao_banco = ('user = %s , passwd = %s , db = %s, host = %s'%(user_banco, senha, banco, ip_servidor)

con = MySQLdb.connect(user = user_banco, passwd = senha, db = banco, host = ip_servidor)

def update_banco(id_caixa, banco):

	c = con.cursor()

	gt_final = c.execute('select grande_total_final from %s.reducaoz where caixa_caixa_id_oid = %i' %(banco, id_caixa))
	lista_gt_final =  c.fetchall()
	id_red =  c.execute('select reducaoz_id from %s.reducaoz where caixa_caixa_id_oid = %i' %(banco,id_caixa))
	lista_reducaoz_id = c.fetchall()

	cont_gt_final = 0
	cont_id_reducaoz = 1
	
	#print len(lista_gt_final)
	#print lista_reducaoz_id
	
	for cont_gt_final in range(len(lista_gt_final)-1):
		update = 'update %s.reducaoz set grande_total_inicial =%f  where reducaoz_id = %i'%(banco, lista_gt_final[cont_gt_final][0], lista_reducaoz_id[cont_id_reducaoz][0])
		c.execute(update)
		con.commit()

		cont_gt_final +=1
		cont_id_reducaoz += 1
	#g = (e[0][0])
	#print e
#c.execute('update red_z.reducaoz set grande_total_inicial = %f where reducaoz_id = 6'%g)
#con.commit()

update_banco(id_caixa,banco)

