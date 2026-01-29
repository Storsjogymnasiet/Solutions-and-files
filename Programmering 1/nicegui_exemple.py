from nicegui import ui

def calculate_fahrenheit(celsius):
    if type(celsius) is not float:
        return
    fahrenheit = (celsius * 1.8) + 32
    fahrenheit = round(fahrenheit, 1)
    result_label.text = f"Det blir: {fahrenheit}°F"

ui.label("Skriv in temperatures i celsius")
ui.number("Celsius",
        on_change= lambda e: calculate_fahrenheit(e.value))

result_label = ui.label("Skriv in temperaturen")

ui.run(native=True)