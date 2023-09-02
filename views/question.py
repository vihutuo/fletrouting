import flet as ft
from flet_route import Params,Basket

def QuestionView(page:ft.Page,params:Params,basket:Basket):
  
    def submit_clicked(e):
      page.snack_bar = ft.SnackBar(ft.Text(f"Hello {tb1.value}"))
      page.snack_bar.open = True
      #page.add(ft.Text("Sss"))
      page.update()
    
    print(params)
    print(basket)
    t1 = ft.Text("This Is Question View. You selected category " +  params.category)
    tb1 = ft.TextField(label = "Enter your name")
    b1 = ft.FilledButton("Submit", on_click=submit_clicked)
  
    b2 = ft.ElevatedButton("Go Index View", on_click=lambda _: page.go("/"))
  
    return ft.View(
        "/question/:category",
        controls=[t1,tb1,b1,b2]
    )