# polarisationS
mesurer différents types de polarisation en France

étudier les répondants polarisés et regaredr les détermiannt socio-économiques des polarisés 
étude des repondants choisissant des réponses polarisées dans les variables ordo inter et ratio 

## Pourquoi cette approche 
applicable à d'aute jeux de données que de l'ESS 

## TODO 
- implementer les 3 mesures de polarisation de l'article 
- identifer les variables pertinentes 
- Visualiser les données 

filtre dataset France
drop variable varaince zero

(ALTair) seaborn 

## ALler plus loin :
regarder ou la france se situe ? 
dans le temps ? d'autres pays ? 



ecrire cr sur typst 
outil figure -> legende 

regarder valeur mediane plutot que 0.5 pour polar enjeux


agréger sur des enjeux 
- immigration
- droits des femmes
- enjeux globaux -> faire un score 



+ comparaison avec les autres pays 
+ recherche des variables -> homme/femme, age, jsp 
    - France puis autres pays 

- regarder si les personnes les plus à polarisée idéologiquement sont les meme sur des enjeux 
- comparaison avec quel graph ? 
- attribution d'une note de polarisation idélogique 
- selectionner par tranche de score 



T/F sur les min max -> pol immi new column 
- regarder caractériqtiques 
- profils tendance à prendre des choix extremes -> variagles socio-eco


Helper function 
demande le input au user 
beautifulsoup4 -> HTML
 script pour regarder le html 
 -> rentrer mquestion -> modalité + description 
 créer un data frame id colones à garder 

 drop columns à 1771

 df_fr.isna()


 section enjeux 
 section SES 
 assigner un label 
 enjeux 
 - est-ce que on est sur un vrai 0






 # Newstart

division entre 7 part (EG,G,CG,C,CD,D,ED)
 - attribution du label dans une colonne 
 - repartition de EG, ED
 - personnes qui n'ont pas répondu GD ? -> label pour regarder leurs réponses 
 - Enjeu immigration -> pourquoi somme ? 
 - Enjeu misogynie 
 - Enjeu valeurs ? LGBT ?
 - Variables montrant la polarisation // Variable expliquant la polarisation 
 - Nv Diplome, Age, Genre, Cat d'agglomeration 
    - Sous tab avec genre
 - Attitude de vote (regarder elections dispo)

 - renormaliser après avoir changé les variables immi pour avoir 0 et 1 en minmax


 + Regarder l'autoplacement gauche-droite des individus polarisés sur des enjeux politiques 
 + Comparer l'opinion d'individus polarisés sur un enjeux sur les autres enjeux
 + Placer artificiellement les personnes qui n'ont pas répondu 


Est-ce que les individus qui ont choisi de ne pas se placer sur un axe gauche-droite sont des personnes qui ne souhaitent pas se placer sur une axe "republicain" et donc implique une polarisation sur des enjeux 

Quelle caractérisation politique des individus qui ne se projettent pas sur l'axe "républicain" gauche-droite ? 


Les non-répondants sur l'échelle gauche-droite cachent derrière un rejet du placement républicain une polarisation réactionnaire

 - Regarder autre que la France ? 

- Créer 0/1 pour NR 
- prendre des variables de polarisations 
- regarder les variables explicatives

expliquer le choix de NR par une polarisation sur des enjeux 
expliquer le choix de NR par des variables socio-demographique 

-> statsmodel