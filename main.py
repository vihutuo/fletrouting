import flet as ft
from flet_route import Routing,path
from views.index import IndexView # Here IndexView is imported from views/index_view.py
from views.question import QuestionView # Here NextView is imported from views/next_view.py
def main(page: ft.Page):
    app_routes = [
        path(
            url="/", # Here you have to give that url which will call your view on mach
            clear=True, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
            view=IndexView # Here you have to pass a function or method which will take page,params and basket and return ft.View (If you are using function based view then you just have to give the name of the function.)
            ), 
        path(url="/question/:category", clear=False, view=QuestionView),
    ]

    Routing(
        page=page, # Here you have to pass the page. Which will be found as a parameter in all your views
        app_routes=app_routes, # Here a list has to be passed in which we have defined app routing like app_routes
        )
    page.go(page.route)

ft.app(target=main,assets_dir="assets")