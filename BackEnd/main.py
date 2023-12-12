
from DBSystem.DBsystem import *





class Application:
    def __init__(self):
        self.dbsystem = DBsystem()

    def run(self):
        self.dbsystem.create_tables()


if __name__ == '__main__':
    Aplication = Application()
    Aplication.run()
    app.run(debug=True)

