#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__init__.py
Description:

Author: Phat Luu
Email: trieuphat.luu@bakerhughes.com
Created on: 2024/10/28
"""

# %%
# ================================IMPORT PACKAGES====================================
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# Custom Packages
from cktest.utils.logging_config import logger as logging


db = SQLAlchemy()
bootstrap = Bootstrap()


def page_not_found(e):
    return render_template("errors/404.html"), 404


def create_app():
    # App config
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Register Extension
    db.init_app(app)
    bootstrap.init_app(app)

    # Custom Packages
    # Register apps
    with app.app_context():
        # Register blueprint
        # Custom Packages
        from cktest.main.routes import main

        app.register_blueprint(main)
        # Register error handlers
        app.register_error_handler(404, page_not_found)

        db.create_all()

        return app
