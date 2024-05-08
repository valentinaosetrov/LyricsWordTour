# **Projet Lyrics Wor(L)d Tour**
## Réalisé par Sandra Jagodzińska et Valentina Osetrov
### M2 TAL INALCO 2023/24 - Techniques Web

Notre application vous offre la possibilité d'explorer les endroits évoqués dans les paroles des chansons de Taylor Swift. La base de données est organisée par album, vous offrant ainsi une immersion visuelle dans l'univers de chaque album. Cependant, même si vous n'êtes pas encore Swiftie, vous pouvez saisir les paroles d'une chanson de votre choix (en anglais) et découvrir les lieux correspondants sur la carte du monde.

---

Au préalable, il est nécessaire de télécharger le modèle anglais de traitement par spaCy (qui permet d'analyser les chansons non présentes dans la base de données)

```bash
python -m spacy download en_core_web_sm
```

---

Pour lancer l'application, il faut cloner ce répertoire dans le terminal :
```bash
git clone https://github.com/valentinaosetrov/LyricsWordTour.git
```
Ensuite, il faut se placer dans le répertoire du projet : 
```bash
cd LyricsWordTour/projet
```
Enfin, une fois dans le répertoire, pour lancer l'application il suffit de lancer uvicorn avec :
```bash
uvicorn main:app --reload
```

Le terminal vous indiquera l'url à copier-coller dans le navigateur. De préférence, optez pour Google Chrome qui permet la meilleure représentation visuelle. 

En raison de l'utilisation d'une API open source (OpenStreetMap) pour afficher les lieux sur la carte du monde, il est possible que des délais surviennent en raison des limites d'utilisation.
