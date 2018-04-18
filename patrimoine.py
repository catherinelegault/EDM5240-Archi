# coding: utf-8


import csv
import requests
from bs4 import BeautifulSoup

# VARIABLE AVEC NOTRE URL DE DÉPART
url1 = "http://patrimoine.ville.montreal.qc.ca/inventaire/vignettes.php?typologie=&intervention=&arrondissement=0&debut=0&lignes=10&rangees=3"

fich = "patrimoine.csv"

entetes = {
	"User-Agent":"CLegault - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"c_legault@icloud.com"
}

contenu = requests.get(url1, headers=entetes)

page = BeautifulSoup(contenu.text,"html.parser")


#print(page)

i = 0

for ligne in page.find_all("tr"):
   
    if i != 0:


### Dans chacun des «tr» se trouve un élément html appelé «input»

        if ligne.find("input") is not None:

            ### Ces éléments «input» contiennent un attribut, «onclick», qui contient l'info qui m'intéresse (un nombre entre parenthèses)
            ### Mais «onclick», pour une raison que j'ignore, ne répond pas quand on demande «ligne.input["onclick"]»
            ### Il faut donc recourir à une autre méthode.
            ### Je vous expliquais que BS4 mettait tous les attributs et leurs valeurs dans un dictionnaire
            ### On va donc chercher les valeurs de ce dictionnaire au moyen des méthodes .attrs et .values()
            ### Et on les met dans une liste

            valeurs = ligne.input.attrs.values()

### On crée une boucle pour consulter tous les items de cette liste

            for valeur in valeurs:


                if "OuvrirPopupDetailDemandePatrimoine" in valeur:
                    #print(valeur)

# ### Je vais chercher le nombre entre parenthèses qui me permet de passer à l'étape suivante
                    
                    valeur = valeur.split("(")
                    valeur = valeur[1].split(")")
                    valeur = valeur[0]
                    #print(valeur)

# ### On peut maintenant ajouter cette valeur à l'hyperlien de la fenêtre «popup» qui contient l'info que tu veux moissonner
# ### La suite ressemble beaucoup à ce que avais fait
# ### Mais je complète

                     lien = "http://patrimoine.ville.montreal.qc.ca/inventaire/arch.php?id_archi={}".format(valeur)
                     print(lien)

                     contenu2 = requests.get(lien, headers=entetes)
                     page2 = BeautifulSoup(contenu2.text, "html.parser")

                     recours = []

                     recours.append(lien)

#                     for item in page2.find_all("tr"):
#                         # print(item.text.strip())
#                     #     if item.td is not None and "Étape de la demande" in item.td.text.strip() and "Détails d'une demande" not in item.td.text.strip():
#                     #         # print(item.td.find_next("td").text.strip())
#                     #         recours.append(item.td.find_next("td").text.strip())
#                     #     if item.td is not None and "Palais" in item.td.text.strip() and "Détails d'une demande" not in item.td.text.strip():
#                     #         # print(item.td.find_next("td").text.strip())
#                     #         recours.append(item.td.find_next("td").text.strip())
#                     #     if item.td is not None and "Date de dépôt de la demande d’autorisation" in item.td.text.strip() and "Détails d'une demande" not in item.td.text.strip():
#                     #         # print(item.td.find_next("td").text.strip())
#                     #         recours.append(item.td.find_next("td").text.strip())
#                     #     if item.td is not None and "Nº de dossier" in item.td.text.strip() and "Détails d'une demande" not in item.td.text.strip():
#                     #         # print(item.td.find_next("td").text.strip())
#                     #         recours.append(item.td.find_next("td").text.strip())
#                     #     if item.td is not None and "Objet de la demande" in item.td.text.strip() and "Détails d'une demande" not in item.td.text.strip():
#                     #         # print(item.td.find_next("td").text.strip())
#                     #         recours.append(item.td.find_next("td").text.strip())
#                     #     if item.td is not None and "Intitulé de la cause" in item.td.text.strip() and "Détails d'une demande" not in item.td.text.strip():
#                     #         # print(item.td.find_next("td").text.strip())
#                     #         recours.append(item.td.find_next("td").text.strip())
#                     #     if item.td is not None and "Description du groupe qui intente l'action" in item.td.text.strip() and "Détails d'une demande" not in item.td.text.strip():
#                     #         # print(item.td.find_next("td").text.strip())
#                     #         recours.append(item.td.find_next("td").text.strip())

#                      #print(recours)

### Je décommente, plus bas, ton inscription dans ton fichier CSV
### Et je l'indente comme il faut

### Si tu le veux, tu pourrais aussi aller chercher les autres infos contenues dans la page, comme le nom des avocats («procureurs»)

        # lien = ligne.a["href"]
        # hyperlien = "http://services.justice.gouv.qc.ca/dgsj/rrc/Demande/" + lien
        # print(hyperlien)

        # contenu2 = requests.get(hyperlien, headers=entetes)
        # page2 = BeautifulSoup(contenu2.text, "html.parser")
        
        # recours = []
        
        # recours.append(hyperlien)

        # for item in page2.find_all("tr"):
        # # print(item)
        
        
        #     if item.td is not None:
        #         recours.append(item.td.text)
            
        #     # SINON (SI C'EST DU NÉANT), AJOUTE «None» À NOTRE LISTE
        #     else:
        #         recours.append(None)
        
        # print(recours)
        
       
                    # achille = open(fich,"a")
                    # talon = csv.writer(achille)
                    # talon.writerow(recours)

        #print(lien)
        
        
        

        
        
        
        
        
        
    # ON AUGMENTE NOTRE COMPTEUR DE 1
    # i =+ 1