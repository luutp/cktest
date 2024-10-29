#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

fileIO.py
Description:

Author: Phat Luu
Email: trieuphat.luu@bakerhughes.com
Created on: 2024/10/28

"""

# %%
# ================================IMPORT PACKAGES====================================

# Standard Packages
import os
import secrets
import shutil
import sys

from flask import current_app
from flask import url_for


UPLOAD_DIR = os.path.join(current_app.root_path, "uploads")


def makedir(inputDir, remove=False):
    """Summary:
    --------
    Make directory
    Inputs:
    -------
    inputDir (str): fullpath to directory to be created
    remove (bool): option to remove current existing folder
    """
    if remove is True and os.path.exists(inputDir):
        print("Remove existing folder")
        shutil.rmtree(inputDir)

    if not os.path.exists(inputDir):
        print(f"Making directory: {inputDir}")
        os.makedirs(inputDir)
    else:
        print(f"mkdir: Directory already exist: {inputDir}")


def receive_file(filefield_firmware):
    _, f_ext = os.path.splitext(filefield_firmware.filename)
    makedir(UPLOAD_DIR)
    print(f"{f_ext}", file=sys.stdout)
