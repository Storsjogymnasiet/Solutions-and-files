from nicegui import ui
moves = ["sten", "sax", "påse"]

def validate_move(player_1, player_2):
    if player_1 == player_2:
        return "Oavgjort"
    elif player_1 == "sten" and player_2 == "sax":
        return "Spelare 1 vinner!"
    elif player_1 == "sax" and player_2 == "påse":
        return "Spelare 1 vinner!"
    elif player_1 == "påse" and player_2 == "sten":
        return "Spelare 1 vinner!"
    else:
        return "Spelare 2 vinner!"
    
ui.label(text=f"{validate_move("sten", "sax")}")

ui.run(native=True)