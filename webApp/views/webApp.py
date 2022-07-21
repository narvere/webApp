from flask import Blueprint, render_template, url_for, redirect, request


webApp = Blueprint('webApp', __name__)

@webApp.route('/')  # предоставление главной страницы
def index():
    return render_template('index.html')