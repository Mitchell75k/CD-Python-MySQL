players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
},

{
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
},

{
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
},

{
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
},

{
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
}
]

new_team = []

# challenge 1: Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    #  challenge 3: Make a list of Player instances from the players dictionaries

def add_2_new_list(players_list): # this function takes in the players list as an argument
    for player in players: #this loops through the players list
        new_team.append(player["name"]) # this adds the name of the player to the new_team list from the players list
    return new_team # this returns the new_team list to the function

# challenge 2: Create a new Player object for each player in the players list.


player_kevin = Player(players[0])

player_jason = Player(players[1])

player_kyrie= Player(players[2])

player_damian = Player(players[3])

player_joel = Player(players[4])

#these are the instances of the Player class, which takes in the 'players' list as an argument

print(add_2_new_list(players)) #this is the function call to the add_2_new_list function, which takes in the players list as an argument

print(new_team)