from flask import render_template, request, redirect, url_for
from . import main


#views
@main.route('/')
def index():
   """
   Function that returns the index page
   """
   return render_template('index.html')