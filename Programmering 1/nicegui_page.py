from nicegui import ui

@ui.page("/")
def home_page():
    ui.label("Banke Bankelito")
    ui.link("Ta ut pengar", "/withdraw")
    ui.link("Sätta in pengar", "/deposit")
    ui.link("Konto", "/account/Hasse")

@ui.page("/withdraw")
def withdraw_page():
    ui.number("Hur mycket vill du ta ut?")
    ui.button("Ta ut")

    ui.link("Gå hem", "/")

@ui.page("/deposit")
def withdraw_page():
    ui.number("Hur mycket vill du lägga in?")
    ui.button("Lägg in")

    ui.link("Gå hem", "/")

@ui.page("/account/{username}")
def account_page(username):
    ui.label(f"Hej {username}")
    ui.link("Gå hem", "/")


ui.run(native=True)