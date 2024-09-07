import requests

from models import User, Game, Player, Move

class HttpClient:
    def __init__(self):
        self.host = "https://f18e4325-89f0-4357-b6a4-2221454d52fb-00-24sehfqtbpqxn.janeway.replit.dev/"

    def get_user(self, user_id: str) -> User | None:
        try:
            response = requests.get(f"{self.host}/get_user?user_id={user_id}").json()
            if response["status"] != 200:
                return None

            return User(**response["body"]["user"])
        except:
            return None

    def get_active_game_by_user_id(self, user_id: str) -> tuple[Game, list[Player], list[Move]] | None:
        try:
            response = requests.get(f"{self.host}/get_active_game_by_user_id?user_id={user_id}").json()
            if response["status"] != 200:
                return None

            game = Game(**response["body"]["game"])
            players = [Player(**user) for user in response["body"]["users"]]
            moves = [Move(**move) for move in response["body"]["moves"]]

            return game, players, moves
        except:
            return None

    def get_game_info(self, game_id: int) -> tuple[Game, list[Player], list[Move]] | None:
        try:
            response = requests.get(f"{self.host}/get_game_info?game_id={game_id}").json()
            if response["status"] != 200:
                return None

            game = Game(**response["body"]["game"])
            players = [Player(**user) for user in response["body"]["users"]]
            moves = [Move(**move) for move in response["body"]["moves"]]

            return game, players, moves
        except:
            return None

    def join_game(self, user_id: str) -> tuple[Game, list[Player]] | None:
        try:
            response = requests.get(f"{self.host}/join_game?user_id={user_id}").json()
            if response["status"] != 200:
                return None

            game = Game(**response["body"]["game"])
            users = [Player(**user) for user in response["body"]["users"]]

            return game, users
        except:
            return None

    def leave_game(self, user_id: str, game_id: str) -> bool:
        try:
            response = requests.get(f"{self.host}/leave_game?user_id={user_id}&game_id={game_id}").json()

            return response["status"] == 200
        except:
            return False

    def make_move(self, user_id: str, game_id: int, row: int, col: int, sign: str) -> Move | None:
        try:
            url = f"{self.host}/make_move?user_id={user_id}&game_id={game_id}&row={row}&col={col}&sign={sign}"
            response = requests.get(url).json()
            if response["status"] != 200:
                return None

            return Move(**response["body"]["move"])
        except:
            return None
