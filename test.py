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