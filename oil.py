def menu1():
	print("################################################################################")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                  Welcome                                     #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("################################################################################")


def menu2():
	print("################################################################################")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                  รายการ                                      #")
	print("#                                                                              #")
	print("#                     1.Gasoline 95  ราคา 29.16 BAHT                           #")
	print("#                     2.Gasoline 91  ราคา 25.30 BAHT                           #")
	print("#                     3.Gasohol 91   ราคา 21.68 BAHT                           #")
	print("#                     4.Gasohol E20  ราคา 20.2  BAHT                           #")
	print("#                     5.Gasohol 95   ราคา 21.2  BAHT                           #")
	print("#                     6.Diesel       ราคา 21.1  BAHT                           #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("################################################################################")


def menu3():
	print("################################################################################")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                ชนิดการทำงาน                                   #")
	print("#                                                                              #")
	print("#                           1.คำนวนจากเงินเป็นลิตร                                #")
	print("#                           2.คำนวนจากลิตรเป็นเงิน                                #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("################################################################################")


def menu4():
	print("################################################################################")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                             กรุณาใส่จำนวน                                      #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("################################################################################")



def menu5():
	print("################################################################################")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                           ออกจากโปรแกรมหรือไม่                                 #")
	print("#                                                                              #")
	print("#                            1.ออกจากโปรแกรม                                   #")
	print("#                            2.เริ่มโปรแกรมใหม่                                   #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("#                                                                              #")
	print("################################################################################")




while True:
	menu1()
	b = input("++กดEnterเพื่อดำเนินการต่อ++")
	
	a = 0
	while not(a in [1, 2, 3, 4, 5, 6]):
		menu2()
		b = input("เลือกเชื้อเพลิง :")
		if b.isnumeric():
			a = int(b)
		else:
			a = 0

	g = 0
	while not(g in [1, 2]):		
		menu3()
		f = input("เลือกการคำนวณ : ")
		if f.isnumeric():
			g = int(f)
		else:
			g = 0
	
		
		menu4()
		if g == 1 :
			c = input("ใส่จำนวนเงิน :")
			y = float(c)
			if a == 1 :
				t = y/29.16
				print('total = ' ,format(t),'LITER')
			elif a == 2 :
				t = y/25.30
				print('total = ' ,format(t),'LITER')
			elif a == 3 :
				t = y/21.68
				print('total = ' ,format(t),'LITER')
			elif a == 4 :
				t = y/20.2
				print('total = ' ,format(t),'LITER')
			elif a == 5:
				t = y/21.2
				print('total = ' ,format(t),'LITER')
			elif a == 6:
				t = y/21.1
				print('total = ' ,format(t),'LITER')
			else :
				print('ไม่สามารถคำนวณได้')
					
		if g == 2 :
			c1 = input("ใส่จำนวนลิตร :")
			y = float(c1)
			if a == 1 :
				t = y*29.16
				print('total = ' ,format(t),'BATH')
			elif a == 2 :
				t = y*25.30
				print('total = ' ,format(t),'BATH')
			elif a == 3 :
				t = y*21.68
				print('total = ' ,format(t),'BATH')
			elif a == 4 :
				t = y*20.2
				print('total = ' ,format(t),'BATH')
			elif a == 5 :
				t = y*21.2
				print('total = ' ,format(t),'BATH')
			elif a == 6 :
				t = y*21.1
				print('total = ' ,format(t),'BATH')
			else :
				print('ไม่สามารถคำนวณได้')

	a = 0
	while not(a in [1, 2]):
		menu5()
		b = input("ออกจากโปรแกรมหรือไม่ :")
		if b.isnumeric():
			a = int(b)
			
		else :
			a = 0
	if a == 1 :
		break
			









