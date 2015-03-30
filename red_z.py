import 	MySQLdb

con = MySQLdb.connect(user='root', passwd='root',db='red_z')

#id_caixa_set = input("Digite o ID do caixa: ")
def update_banco():

	c = con.cursor()

	gt_final = c.execute('select grande_total_final from red_z.reducaoz where caixa_caixa_id_oid = 18')
	lista_gt_final =  c.fetchall()
	id_red =  c.execute('select reducaoz_id from red_z.reducaoz where caixa_caixa_id_oid = 18')
	lista_reducaoz_id = c.fetchall()

	cont_gt_final = 0
	cont_id_reducaoz = 1
	'''
	print len(lista_gt_final)
	print lista_reducaoz_id
	'''
	for cont_gt_final in range(len(lista_gt_final)-1):
		update = 'update red_z.reducaoz set grande_total_inicial =%f  where reducaoz_id = %i'%(lista_gt_final[cont_gt_final][0], lista_reducaoz_id[cont_id_reducaoz][0])
		c.execute(update)
		con.commit()

		cont_gt_final +=1
		cont_id_reducaoz += 1
	#g = (e[0][0])
	#print e
#c.execute('update red_z.reducaoz set grande_total_inicial = %f where reducaoz_id = 6'%g)
#con.commit()

update_banco()

