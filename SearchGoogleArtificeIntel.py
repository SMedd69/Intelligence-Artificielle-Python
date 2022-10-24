import pywhatkit as pw //importation de la librairie pywhatkit que je nomme pw

try:
    pw.search("pywhatkit") //Tapez le(s) mot(s) clé(s) de votre recherche
    print("Recherche...") //Texte qui affiche la recherche qui est effectué
    
except:
    print("An unknown error occurred") // Texte à afficher en cas d erreurs
