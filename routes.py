from flask import render_template, redirect, url_for, request
from . import app, models


@app.route('/')
def accueil():
    liste_categories = models.vue_produits_categories.query.distinct('nom_categorie')
    return render_template('accueil.html', title='Bienvenue dans notre boutique',
                           liste=type(liste_categories),
                           liste_cat=liste_categories)


@app.route('/tous_produits')
def tous_produits():
    liste_produits = models.vue_produits_categories.query.all()
    return render_template('tous_produits.html', title='nos produits', liste_prod=liste_produits)


@app.route('/produits')
def catalogue_de_produits():
    return '<h2>Nos produits :</h2>'


@app.route('/produits_categorie')
def produits_categorie():
    id_categ = request.args.get('id_categorie')
    liste_produits = models.vue_produits_categories.query.filter_by(id_categorie = id_categ)
    return render_template('produits_categorie.html', title='Nos produits',produits = liste_produits, typeprod=type(liste_produits))