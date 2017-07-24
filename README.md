# doggo

utilisation
GOTO: goto file permet de lister tous les chemins d'accès vers un fichier ou répertoire de nom file. Le programme demande à l'utilisateur un nombre qui correspond au chemin désiré. Il est possible de quitter en entrant q à la place d'un nombre. Si l'objet recherché est un fichier, Doggo nous place dans le répertoire contenant ce fichier.
GOBACK: goback est un affichage d'historique de dossiers visités avec goto. Cet historique est créé avec la commande goto sous le nom de directories.txt.
DOGGO: doggo -mem int cette commande permet de choisir le nombre int de chemins dont Doggo doit se souvenir pour l'utilisation de la commande goback.

options
-mem: changement de la mémoire de chemins. Peut être utilisé sans opération (via doggo -mem) ou directement suite a l'opération ( via goto file -mem)
-lvl: choix d'une recherche à un endroit précis. Le niveau 0 correspond au dossier actuel (goto file -lvl 0) le niveau 1 correspond au dossier parent (./..) et ainsi de suite.
-t: affichage supplémentaire du type de l'élément qui se trouve en fin de chemin:
goto '*' il y a possibilité de cherche des fichiers dont le nom est incomplet. ATTENTION: pour faire fonctionner la commande, les simple-quotes sont essentiels. Par exemple goto 'doggo*' permet de retrouver tous les fichiers commençant par doggo :
