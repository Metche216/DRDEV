from flask import Blueprint, render_template

index = Blueprint('index', __name__, template_folder='templates')


@index.route ('/', defaults={'page':'index'})



@index.route('/<page>')
def show_page(page):
    return render_template(f'{page}.html')