#les ensembles ont pour roles de ne pas dupliquer les informations
#creation des ensembles
emails1 ={"emails1@gmail.com","emails2@gmail.com","emails3@gmail.com"}
print(emails1)
#COMME ON LE CONSTACT J'AI DUPLIQUER LE MAIL1 MAIS IL N'AFFICHE PAS LE DEUXIEME MAIL1
emails2 ={"emails1@gmail.com","emails2@gmail.com","emails3@gmail.com","emails1@gmail.com"}
print(emails2)
#Comment aujouter des elements a notre ensembles
emails1.add("email4@gamil.com")
print(emails1)