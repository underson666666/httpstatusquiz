from flask import Flask, render_template
import csv
import random
import sys
import os

sys.path.append(os.path.dirname(__file__))
from const import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    all_choises = get_status_code_list()
    choises = get_choise(all_choises, CHOISE_COUNT)
    answer = get_answer(choises)

    return render_template("index.html", choises=choises, answer=answer)


def get_status_code_list():
    choises = list()
    with open(OUTPUT_FILE_NAME, "r") as f:
        rows = csv.DictReader(f)

        for row in rows:
            choises.append(row)
    return choises


def get_choise(choises, count):
    return random.sample(choises, count)


def get_answer(choises):
    return random.choice(choises)["code"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

