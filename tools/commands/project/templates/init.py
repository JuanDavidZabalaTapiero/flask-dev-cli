from flask import Flask

from .extensions import csrf, db, migrate


def create_app(config_class):
    app = Flask(__name__)

    # == CONFIGURACIÓN ==
    app.config.from_object(config_class)

    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    return app
