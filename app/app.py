from flask import Flask, render_template, request
from friends_locations import *
from friends_map import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    nickname = request.form.get("nickname")
    bearer_token = request.form.get("bearer_token")
    try:
        if nickname and bearer_token:
            locations_of_friends_list = get_locations_of_friends(
                nickname, bearer_token)
            generate_map(add_coordinates_to_list(locations_of_friends_list))
            return render_template("twitter_friends_map.html")
        return render_template("failure.html")
    except:
        return render_template("failure.html")


if __name__ == "__main__":
    app.run()
