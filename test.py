# affiche "hello world"
print("hello world")

# variables
variable_1 = "une variable"
variable_2 = "une deuxième variable"
print(variable_1)
print(variable_2)

# liste
plateformes_sociales = ["facebook", "messenger", "twitter", "snapchat", "LinkedIn"]
langage_de_programmation = "PYTHON"
# Affiche "twitter"
print(plateformes_sociales[2])
# Affiche la lettre "T" qui est l'indice [2] de la chaîne de caractères "PYTHON"
print(langage_de_programmation[2])
# Affiche la lettre "i" qui est l'indice [2] de la chaîne de caractères "twitter" contenu dans un array ou twitter est à l'index [2];
print(plateformes_sociales[2][2])


# les methodes
# Ajoute "discord" à la fin de la liste
plateformes_sociales.append("discord")
print(plateformes_sociales)
# Enlève "snapchat" de la liste
plateformes_sociales.remove("snapchat")
print(plateformes_sociales)
# Affiche la longueur de la liste
print(len(plateformes_sociales))
# Trie la liste par ordre alphabétique ( les majuscules sont placées avant les minuscules, et les nombres avant les majuscules ).
plateformes_sociales.sort()
print(plateformes_sociales)

# les tuples
# S'écrit comme une liste sauf que les crochets [] sont remplacés par des parenthèses ()
# La principale différence est que les tuples sont immuables ! ( ce sont toujours des listes ! )
exmples_tuples = (1, 2, 3, 4, 5)


# Les dictionnaires ( équivalant aux objets en js )
nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne d'Arc",
    "nom_de_campagne": "Campagne nous aimons les chiens",
    "date_de_début": "01/01/2020",
    "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}
# Ou bien
taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
# Ou encore en utilisant la fonction dict()
# taux_de_conversion = dict()
# taux_de_conversion['facebook'] = 3.4
# taux_de_conversion['instagram'] = 1.2
print(taux_de_conversion)