import pymssql
import time

while 1:
	conn = pymssql.connect("116.193.220.12", "apu", "Sel12345", "cuet_meter")
	cursor = conn.cursor()
	cursor2 = conn.cursor()
	cursor3 = conn.cursor()

	device_id = '2'

	with open('onemindata.txt', 'r') as f:
		lines = f.read().splitlines()
		last_line = lines[-1]
		data = last_line.split(",")
		pulse = data[0]
		datetime = data[1]
	
		cursor.execute("select * from instadata where Id='"+device_id+"'")
		for row in cursor:
			id = row[0]
			status = row[1]
			#print(id)
			#print(status)
			#print('------------')
			if status == '1' and id == device_id:
				querystring = "insert into datatable (Id, DateTime, Pulse) values ('"+device_id+"','"+datetime+"','"+pulse+"')"
				print(querystring)
				cursor2.execute(querystring)
				print('data inserted')
				cursor3.execute("update instadata set Status='0' where Id='"+device_id+"'")
				conn.commit()

			else:
				print('no data calling')
		conn.close()
		time.sleep(15.0)
