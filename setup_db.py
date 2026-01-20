import os
import sqlite3

# Absolute path to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FOLDER = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_FOLDER, "my_database.db")

def setup_database():
    # Ensure the database folder exists
    os.makedirs(DB_FOLDER, exist_ok=True)

    # Connect to the SQLite database (creates file if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            RecipeID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            servings INTEGER,
            calories INTEGER,
            ingredients TEXT,
            instructions TEXT
        )
    """)

    # Insert sample data only if table is empty
    cursor.execute("SELECT COUNT(*) FROM recipes")
    count = cursor.fetchone()[0]

    if count == 0:
        sample_recipes = [
            ("Spaghetti Bolognese", "Classic Italian pasta", 4, 650,
            "Spaghetti, beef, tomato sauce", "Cook pasta, cook sauce, combine"),
            
            ("Chicken Curry", "Spicy curry", 3, 550,
            "Chicken, curry paste, coconut milk", "Cook chicken, add sauce"),

            ("Beef Stir Fry", "Quick Asian-style stir fry", 2, 500,
            "Beef, bell peppers, soy sauce, garlic", "Stir fry beef, add vegetables, add sauce"),

            ("Vegetable Omelette", "Healthy breakfast omelette", 1, 300,
            "Eggs, onion, bell pepper, spinach", "Beat eggs, cook vegetables, add eggs"),

            ("Grilled Salmon", "Simple grilled salmon fillet", 2, 450,
            "Salmon, olive oil, lemon, salt", "Season salmon, grill until cooked"),

            ("Caesar Salad", "Classic Caesar salad", 2, 350,
            "Lettuce, croutons, parmesan, Caesar dressing", "Mix ingredients, add dressing"),

            ("Beef Tacos", "Mexican-style tacos", 3, 600,
            "Ground beef, taco shells, lettuce, cheese", "Cook beef, assemble tacos"),

            ("Tomato Soup", "Comforting tomato soup", 4, 250,
            "Tomatoes, onion, garlic, cream", "Cook vegetables, blend, simmer"),

            ("Pancakes", "Fluffy breakfast pancakes", 4, 400,
            "Flour, eggs, milk, sugar", "Mix batter, cook on griddle"),

            ("Fried Rice", "Easy leftover rice dish", 3, 550,
            "Rice, eggs, vegetables, soy sauce", "Stir fry eggs, add rice and vegetables")
        ]

        cursor.executemany("""
            INSERT INTO recipes
            (name, description, servings, calories, ingredients, instructions)
            VALUES (?, ?, ?, ?, ?, ?)
        """, sample_recipes)
        conn.commit()
        print("Sample data inserted into database.")
    else:
        print("Database already has data, skipping sample insertion.")

    conn.close()
    print(f"Database setup complete at {DB_PATH}")

# Allow standalone execution
if __name__ == "__main__":
    setup_database()
