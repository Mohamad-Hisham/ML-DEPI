from pathlib import Path

COLS_DROP = ["PassengerId", "Name", "Ticket",]

FILE_PATH = str(Path(__file__).resolve().parent.parent / "data" / "Titanic.csv")