import os


# a variable partie entiere du nombre
# b partie decimale du nombre
nombre = str( float (input( "entrez votre nombre", )) )


nombre_décomposé = nombre.split(".")


a = nombre_décomposé[0]

b = nombre_décomposé[1]

précision = int(input("nombre de chiffre apres la virgule:", ))

b = list(b)

del b[ précision: ]

b = "".join(b)

nombre_a_afficher = []

nombre_a_afficher.append(a)

nombre_a_afficher.append(",")

nombre_a_afficher.append(b)

nombre_a_afficher = "".join(nombre_a_afficher) 

print (nombre_a_afficher)


os.system ("Pause")

#correction


"""
def afficher_flottant(flottant):
    """"""Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule""""""
    
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])

"""