from PyQt5.QtWidgets import QMessageBox
from json import load

data = load(open("../static/themes.json", mode="r", encoding="utf-8"))
settings_file = load(open("../data/settings.json", mode="r", encoding="utf-8"))

active_theme = settings_file["active_theme"]

window = (f"background-color: rgb({data[active_theme]['background-color']});")

button = (f"background-color: rgba({data[active_theme]['button-background-color']}, 210);"
          f"color: rgb({data[active_theme]['button-text-color']});"
          f"border: {data[active_theme]['widget-border']};"
          f"border-radius: {data[active_theme]['border-radius']};")

widget = (f"background-color: rgb({data[active_theme]['widget-background']});"
          f"border: {data[active_theme]['widget-border']} solid;"
          f"border-radius: {data[active_theme]['border-radius']};")

tree_widget = (f"background-color: rgb({data[active_theme]['button-background-color']});"
               f"border: {data[active_theme]['widget-border']} solid;"
               f"border-radius: {data[active_theme]['border-radius']};")
