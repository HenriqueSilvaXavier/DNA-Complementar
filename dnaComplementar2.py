DNA=input("Digite o código genético: ")
DNA3=""
DNA2=[]
for n in DNA:
	DNA2.append(n)
for n in range(0, len(DNA)):
	if DNA2[n]=="A":
		DNA2[n]="T"
	elif DNA2[n]=="T":
		DNA2[n]="A"
	elif DNA2[n]=="G":
		DNA2[n]="C"
	elif DNA[n]=="C":
		DNA2[n]="G"
for n in DNA2:
	DNA3="{}{}".format(DNA3, n)
print("Complementar:", DNA3)