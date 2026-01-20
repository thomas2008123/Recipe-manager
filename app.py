from flask import Flask, render_template, request, redirect, url_for
import db
from setup_db import setup_database

app = Flask(__name__)

setup_database()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recipes", methods=["GET", "POST"])
def view_recipes():
    if request.method == "POST":
        # Handle search
        if request.form.get('action') == 'search':
            keyword = request.form.get("recipeSearch")
            recipes = db.search_recipes(keyword)
            return render_template("viewRecipes.html", recipes=recipes, search_results=recipes)
        # Handle show all
        elif request.form.get('action') == 'showAll':
            recipes = db.get_all_recipes()
            return render_template("viewRecipes.html", recipes=recipes)
    recipes = db.get_all_recipes()
    print(recipes)
    return render_template("viewRecipes.html", recipes=recipes)

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        description = request.form.get("description")
        servings = request.form.get("servings")
        calories = request.form.get("calories")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")

        # Convert numeric fields safely
        servings = int(servings) if servings else 0
        calories = int(calories) if calories else 0

        # Insert into database
        db.add_recipe(name, description, servings, calories, ingredients, instructions)

        # Redirect to recipe list
        return redirect(url_for("view_recipes"))

    # GET request shows form
    return render_template("addRecipe.html")

if __name__ == "__main__":
    app.run(debug=True)
