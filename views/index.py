import flet as ft
from flet_route import Params,Basket


def IndexView(page:ft.Page,params:Params,basket:Basket):
    def check_item_clicked(e):
        print("Clicked")
    print(params)
    print(basket)
   
    app_bar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,on_click=check_item_clicked),
            ft.IconButton(ft.icons.FILTER_3),
            
        ],
    )
    #put your images under assets folder
    img1 = ft.Image(
        src="images/m1.jpg",        
        height=300,
        fit=ft.ImageFit.CONTAIN,
     )


    return ft.View(
        "/",
        controls=[
            app_bar,
            ft.Text("This Is Index View"),
            ft.ElevatedButton("Sports", on_click=lambda _: page.go("/question/1")),
          ft.ElevatedButton("Science", on_click=lambda _: page.go("/question/2")),
          img1
        ]
    )