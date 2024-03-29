import sqlite3
from pathlib import Path

from db_create_table import create_tables


def get_all_files(data_dir: Path):
    paths = []
    categories = sorted(data_dir.glob("*"))

    for i in range(len(categories)):
        sub_categories = sorted(categories[i].glob("*"))

        for j in range(len(sub_categories)):
            images = sorted(sub_categories[j].rglob("*.png"))
            paths.extend(images)

    return paths

def fill_db(paths):
    with sqlite3.connect('product_cards.db') as con:
        cursor = con.cursor()
        for i in range(len(paths)):
            cursor.execute("INSERT INTO images (category, type, name)\
                            VALUES (?, ?, ?)", (paths[i].parts[-3:-2][0],
                                                   paths[i].parts[-2:-1][0],
                                                   paths[i].parts[-1:][0],
                                                  ))

def main():
    create_tables()
    data_dir = Path("/".join(Path.cwd().parts[:-1])) / "data" / "data"
    paths = get_all_files(data_dir)
    fill_db(paths)

if __name__ == '__main__':
    main()

