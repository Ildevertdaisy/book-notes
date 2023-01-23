
@app.cli.command('db_create') est un décorateur qui indique à Flask qu'une fonction suivante est un commande de ligne d'interface (CLI) nommée "db_create".
db.create_all() crée toutes les tables de la base de données qui ont été définies dans les modèles de l'application.
print('Database created!') imprime un message indiquant que la base de données a été créée.