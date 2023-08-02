# Lecteur des pdfs
 ce script python est réalisé  pour la lecture des pdfs graces aux librairies pyttsx3 et PyPDF2, il lit des pdfs en anglais pour le moment et je pense l'améliorer en ajoutant d'autres langues avec le temps
 # Proceder :
 ## Création d'un environnement virtuel
   créer un repertoire dans un disque au choix de votre ordinateur, exemple: dans mon cas Lecteur, puis placer vous dans le repertoire
   ```bash
      cd Lecteur 
      ```
  Faite la commande suivante pour créer votre environnement
  ```bash
      python -m venv env_lecteur 
      ```
  Puis clonner le projet à l'aide de votre git:
  ```bash
      git clone https://github.com/Ben-musampa/Lecteur_des_pdfs.git
      ```
  activer l'environement
  ```bash
      env_lecteur\scripts\activate
      ```
  En suite se positionner dans le projet clonné 
  ```bash
      cd Lecteur_des_pdfs 
      ```
  puis
  ```bash
      cd Lecteur 
      ```
 ## Installation des librairies
   ```bash
      pip install -r requirement.txt
      ```
  puis lancer le script python en indiquqnt le chemin du pdf dans le script `main.py` la ligne `lecteur = PyPDF2.PdfFileReader(livre)` puis lancez votre script avec la commande:
   ```bash
      python main.py
      ```
