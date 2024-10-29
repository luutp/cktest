#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
routes.py
Description:

Author: Phat Luu
Email: trieuphat.luu@bakerhughes.com
Created on: 2024/10/28
"""

# Standard Packages
# %%
# ================================IMPORT PACKAGES====================================
import os
import sys

# Data Analytics
import pandas as pd
import random

from flask import Blueprint
from flask import current_app
from flask import flash
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import send_file
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from werkzeug.utils import secure_filename

# Custom Packages
from cktest import db
from cktest.main.forms import uploadFirmwareForm
from cktest.utils import fileIO


script_dir = os.path.abspath(os.path.dirname(__file__))

main = Blueprint("main", __name__)

# Sample DataFrame setup
groceries = [
    "Apple",
    "Orange",
    "Milk",
    "Chicken",
    "Broccoli",
    "Bread",
    "Eggs",
    "Spinach",
    "Juice",
    "Carrot",
]
categories = [
    "Fruit",
    "Fruit",
    "Drink",
    "Meat",
    "Vegetable",
    "Bakery",
    "Dairy",
    "Vegetable",
    "Drink",
    "Vegetable",
]

availability = [random.choice(["Yes", "No"]) for _ in range(10)]  # Random availability

# DataFrame with sample data
df = pd.DataFrame(
    {"Grocery": groceries, "Category": categories, "Available": availability}
)
# Available categories for dropdown
category_options = ["Fruit", "Drink", "Meat", "Vegetable", "Bakery", "Dairy"]


@main.route("/", methods=["GET", "POST"])
def home():
    return render_template("public/home.html")


@main.route("/submit_input_list", methods=["POST"])
def submit_input_list():
    global df  # Use the global DataFrame to update data

    grocery_list = request.form.get("inputList")

    # Split the list by newline and remove any empty entries
    groceries = [item.strip() for item in grocery_list.splitlines() if item.strip()]

    # Example: Create a DataFrame with the groceries
    data = {
        "Grocery": groceries,
        "Category": ["Uncategorized"] * len(groceries),
        "Available": ["No"] * len(groceries),
    }
    df = pd.DataFrame(data)

    # For demonstration, print the DataFrame to the console
    print(df)
    return render_template(
        "public/home.html",
        data=df.to_dict(orient="records"),
        categories=category_options,
    )


@main.route("/submit_results", methods=["POST"])
def submit_results():
    global df
    # Update the DataFrame based on form submission
    for i, row in enumerate(request.form.getlist("grocery")):
        df.at[i, "Category"] = request.form.getlist("category")[i]
        df.at[i, "Available"] = "Yes" if f"available_{i}" in request.form else "No"
    available_df = df[df["Available"] == "Yes"]
    category_dict = available_df.groupby("Category")["Grocery"].apply(list).to_dict()
    # Export to Excel
    file_path = os.path.join(script_dir, "product_mapping.xlsx")
    df.to_excel(file_path, index=False)
    # return send_file(file_path, as_attachment=True)
    return render_template(
        "public/home.html",
        data=df.to_dict(orient="records"),
        categories=category_options,
    )


@main.route("/about")
def about():
    return render_template("public/about.html", title="About")
