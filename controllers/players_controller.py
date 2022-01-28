from models.player import Player
from flask import Flask, redirect, render_template, request
from flask import Blueprint
from repositories import player_repository
from repositories import team_repository
import pdb

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", all_players = players)