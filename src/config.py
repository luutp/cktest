#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
config.py
Description:

Author: Phat Luu
Email: trieuphat.luu@bakerhughes.com
Created on: 2024/10/28

"""

# %%
# ================================IMPORT PACKAGES====================================

# Standard Packages
import os
import sys

from dotenv import load_dotenv


script_dir = os.path.dirname(sys.argv[0])
dotenv_filepath = os.path.join(script_dir, ".env")
load_dotenv(dotenv_filepath)


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # Filepath
    APP_DIR = script_dir
    PROJECT_ROOT = os.path.dirname(APP_DIR)
    STATIC_DIR = os.path.join(APP_DIR, "static")
    UPLOAD_DIR = os.path.join(STATIC_DIR, "upload")
