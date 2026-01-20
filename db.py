import sqlite3
from setup_db import DB_PATH

def get_all_recipes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    conn.close()
    return recipes

def add_recipe(name, description, servings, calories, ingredients, instructions):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO recipes
        (name, description, servings, calories, ingredients, instructions)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, description, servings, calories, ingredients, instructions))
    conn.commit()
    conn.close()

def search_recipes(keyword):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.row_factory = sqlite3.Row
    cursor.execute("""
        SELECT * FROM recipes
        WHERE name LIKE ? OR description LIKE ? OR ingredients LIKE ?
    """, (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    results = cursor.fetchall()
    conn.close()
    return results