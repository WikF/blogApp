from database import Database
from models.blog import Blog
from menu import Menu
__author__ = "wiktor"

Database.initialize()

menu = Menu()
menu.run_menu()


