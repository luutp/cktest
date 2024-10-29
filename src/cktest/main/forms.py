#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
forms.py
Description:

Author: Phat Luu
Email: trieuphat.luu@bakerhughes.com
Created on: 2024/10/28
"""

# %%
# ================================IMPORT PACKAGES====================================

from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length
from wtforms.validators import Regexp
from wtforms.validators import ValidationError


class uploadFirmwareForm(FlaskForm):
    filefield_firmware = FileField(
        "Update .bin File",
        validators=[FileRequired(), FileAllowed(["bin", "pdf", "jpg"])],
    )
    submit = SubmitField("Update Firmware")
