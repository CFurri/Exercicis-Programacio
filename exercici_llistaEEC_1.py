

#Fer un programa que donada una quantitat de diners en euros, sense decimals, digui quants bitllets de 500, de 200, de 100, de 50, de 20, de 10, de 5 i monedes de 2 i de 1 se li corresponen.

quant_diners = int(input("Digues una quantitat de diners: "))

bitllet_500 = quant_diners // 500
quant_diners = quant_diners - (500 * bitllet_500)

bitllet_200 = quant_diners // 200
quant_diners = quant_diners - (200 * bitllet_200)

bitllet_100 = quant_diners // 100
quant_diners = quant_diners - (100 * bitllet_100)

bitllet_50 = quant_diners // 50
quant_diners = quant_diners - (50 * bitllet_50)

bitllet_20 = quant_diners // 20
quant_diners = quant_diners - (20 * bitllet_20)

bitllet_10 = quant_diners // 10
quant_diners = quant_diners - (10 * bitllet_10)

bitllet_5 = quant_diners // 5
quant_diners = quant_diners - (5 * bitllet_5)

bitllet_2 = quant_diners // 2
quant_diners = quant_diners - (2 * bitllet_2)

bitllet_1 = quant_diners // 1
quant_diners = quant_diners - (1 * bitllet_1)






print(bitllet_500)
print(bitllet_200)
print(bitllet_100)
print(bitllet_50)
print(bitllet_20)
print(bitllet_10)
print(bitllet_5)
print(bitllet_2)
print(bitllet_1)

#Opció 2 (i molt millor)

quant_diners = int(input("Digues una quantitat de diners: "))

bitllet_500 = quant_diners // 500
quant_diners = quant_diners % 500

bitllet_200 = quant_diners // 200
quant_diners = quant_diners % 200

bitllet_100 = quant_diners // 100
quant_diners = quant_diners % 100

bitllet_50 = quant_diners // 50
quant_diners = quant_diners % 50

bitllet_20 = quant_diners // 20
quant_diners = quant_diners % 20

bitllet_10 = quant_diners // 10
quant_diners = quant_diners % 10

bitllet_5 = quant_diners // 5
quant_diners = quant_diners % 5

bitllet_2 = quant_diners // 2
quant_diners = quant_diners % 2

bitllet_1 = quant_diners // 1
quant_diners = quant_diners % 1

print(bitllet_500)
print(bitllet_200)
print(bitllet_100)
print(bitllet_50)
print(bitllet_20)
print(bitllet_10)
print(bitllet_5)
print(bitllet_2)
print(bitllet_1)






