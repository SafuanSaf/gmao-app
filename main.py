"""
main.py
=======
Point d'entrée de l'application GMAO Flask.
Lance le serveur et enregistre tous les blueprints.
"""

from flask import Flask, session
from config import SECRET_KEY

# ── Import des blueprints (un par module fonctionnel) ──────────────────────────
from routes.auth_routes     import auth_bp
from routes.menu_routes     import menu_bp
from routes.ajouter_routes  import ajouter_bp
from routes.consulter_routes import consulter_bp
from routes.modifier_routes import modifier_bp
from routes.remplacer_routes import remplacer_bp
from routes.effacer_routes  import effacer_bp

# ── Création de l'application ──────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = SECRET_KEY

# ── Enregistrement des blueprints ──────────────────────────────────────────────
app.register_blueprint(auth_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(ajouter_bp)
app.register_blueprint(consulter_bp)
app.register_blueprint(modifier_bp)
app.register_blueprint(remplacer_bp)
app.register_blueprint(effacer_bp)

# ── Lancement ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
