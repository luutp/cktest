#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run.py
Description:

Author: Phat Luu
Email: trieuphat.luu@bakerhughes.com
Created on: 2024/10/28

"""

# %%
# ================================IMPORT PACKAGES====================================

# Custom Packages
from cktest import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8080)
