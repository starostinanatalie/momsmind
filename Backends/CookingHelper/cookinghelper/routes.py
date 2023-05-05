from flask import render_template, flash, redirect, url_for
from cookinghelper import cooking_helper


@cooking_helper.route('/')
@cooking_helper.route('/index')
def index():
    user = {'username': 'Natalie'}
    return render_template('index.html', title="Home", user=user)
