# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

fichier = "patrimoine3.csv"

for n in range(0,1301):
	url = "http://patrimoine.ville.montreal.qc.ca/inventaire/arch.php?id_archi={}".format(n)
	
	print(url)

# #aller chercher le contenu html de chaque page
	contenu = requests.get(url)
	page = BeautifulSoup(contenu.text,"html.parser")
 	# print(page)
 #FONCTIONNE JUSQU'ICI
#\n séparer avec un enter pour spliter l'adresse et description
	
	machin = []
	infoPatrimoines = page.find("td", class_="legende_gch_norm")
	infoPatrimoines = infoPatrimoines.text.split("\n")
	# print(infoPatrimoines.text.split("\n"))

# enlever les gogosses pas rapport 
	adresse = infoPatrimoines[0].strip()
	# print(adresse)
	machin.append(adresse)

	description = infoPatrimoines[1].strip()
	# print(description)
	machin.append(description)


	urlimage = page.img["src"]
	urlimage = "http://patrimoine.ville.montreal.qc.ca/"+urlimage
	# print(urlimage)
	machin.append(urlimage)


	print(machin)


	loud = open(fichier,"a")
	lary = csv.writer(loud)
	lary.writerow(machin)

               




	# for urlPatrimoine in urlPatrimoines:
			
	#  	try:
	#  		patrimoines = []
	#  		url2 = urlPatrimoines.a["href"]
				
	#  		print(url2)
				
	 			# patrimoines.append(url2)

	 			# contenu2=requests.get(url2)
	 			# page2=BeautifulSoup(contenu2.text,"html.parser")

	 			# # titre=page2.find("h1", id="lblTitre".text
	 			# # 	print(titre)
	 			# # 	patrimoines.append(titre)

	 			# Adresse=page2.find("td", class_="legende_gch_norm").text
	 			# 	print(Adresse)
	 			# 	patrimoines.append(Adresse)

	# 			Description=page2.find("span", id="lblPalaisTitre").text
	# 				print(Description)
	# 				patrimoines.append(Description)

	# 			print(patrimoines)

	# 			loud = open(fichier,"a")
	# 			lary = csv.writer(loud)
	# 			lary.writerow(patrimoines)

	# 		except:
	# 		 	print("Nada")


# 	url2 = "http://services.justice.gouv.qc.ca" + url2
			# 	#print(url2)

			# 	contenu2 = requests.get(url2)
			# 	page2 = BeautifulSoup(contenu2.text,"html.parser")
			# 	#print(url2)


			# 	titre = page2.title.text.split("|")[0].strip()
			
			# 	patrimoines.append(titre)
			# 	print(url2)