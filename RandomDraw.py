# Importer module JSON et module random
import json
import random

#FONCTIONS

# get_jso def une fonction qui va chercher une clé dans des listes (dicos) qui sont stockées dans un fichier texte jso
def get_jso(file,key): #fonction a deux parametres variables, file et key
	values = [] #variable qui définit une liste vide dans python
	with open(file) as f: #permet d’ouvrir un fichier, récupérer les infos puis le fermer. Le fichier est défini par défaut comme f
		data = json.load(f) #variable data qui indique le fichier jso f a ouvrir et le converti en python
		for entry in data: #pour indiquer les actions a faire avec les infos du fichiers
			values.append(entry[key]) #ajoute les valeurs du dico a la liste vide values
	return values #retourne la liste values pleine

# Message def une fonction qui organise les valeurs noms adj et actions dans un phrase (.format)
def message(noms,adjs,actions):
	return "Aujourd'hui tu devrais dessiner {nom} {adj} qui {action}".format(nom=noms,adj=adjs,action=actions)

# get_ramdom def une fonction qui va chercher une valeur au hasard dans une liste X
def get_random(listx):
	random_listx = random.randint(0,len(listx)-1) #variable qui va chercher une valeur au hasard dans une liste en prenant en compte les n valeurs d’une liste (de 0 a n-1)
	result = listx[random_listx] #variable qui renvoi a la valeur correspondant a la clé
	return result	

# def fonction qui utilise les fonction precedentes pour l’appliquer aux 3 listes :
def get_random_noms():
	values_noms = get_jso("noms.json","noms") #variable qui utilise la fonction get.jso pour ouvrir le fichier noms.jso et créer une liste avec les valeurs de ce ficher
	return get_random(values_noms) #retourne une valeur aléatoire de la liste python crée la ligne d’avant
def get_random_adjs():
	values_adjs = get_jso("adjs.json","adjs")
	return get_random(values_adjs)
def get_random_actions():
	values_actions = get_jso("actions.json","actions")
	return get_random(values_actions)


#Ecrire question du debut de programme, avec attente de réponse de l’utilisateur 
user_answer=input("Que voulez-vous dessiner aujourd’hui ? Taper ENTER pour recevoir un shot d’inspiration. Taper B pour quitter le programme") #imprime le resultat de la fonction message avec comme noms, adj et actions définit aléatoirement par la fonction get_ramdom

#def fonction qui définit l’action à suivre en fonction de la réponse de l’utilisateur (WHILE)
while user_answer!="B": #si la réponse de l’utilisateur n’est pas B, exécuter la suite
	print(message(get_random_noms(), get_random_adjs(), get_random_actions()))
	user_answer=input("Besoin de plus d’inspiration ? Taper ENTER pour recevoir un nouveau shot. Taper B pour quitter le programme") # renvoi ce message tant que l’utilisateur n’a pas entré B