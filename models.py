from . import app, db
from flask_sqlalchemy import SQLAlchemy

class vue_produits_categories(db.Model):
    id_produit = db.Column(db.Integer,primary_key=True)
    nom_produit = db.Column(db.String(25),nullable=False)
    description = db.Column(db.String(200),nullable=True)
    prix_produit = db.Column(db.Float(10),nullable=True)
    nom_categorie = db.Column(db.String(30),nullable=False)
    image = db.Column(db.String(30),nullable=True,default='default.jpg')
    id_categorie = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id_produit} : {self.nom_produit} : {self.description} : {self.prix_produit} : {self.image} : {self.nom_categorie}'


