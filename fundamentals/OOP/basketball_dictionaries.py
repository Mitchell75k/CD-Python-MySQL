# challenge 1: Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

class Player:
    new_team = []
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]
        Player.new_team.append(self.name)



# challenge 2: Create a new Player object for each player in the players list.
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???


player_kevin = Player(kevin) 
print(player_kevin.name, player_kevin.age, player_kevin.position, player_kevin.team)

player_jason = Player(jason)

player_kyrie = Player(kyrie)

# challenge 3: Make a list of Player instances from a list of dictionaries
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
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
},

{
    "name": "Damian Lillard", 
    "age":33, 
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
},

{
    "name": "Joel Embiid", 
    "age":32, 
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
}
]

new_team = []

def add_2_new_list(list):
    for player in list:
        new_team.append(player["name"])
    return new_team

print(add_2_new_list(players)) #this is the function call to the add_2_new_list function, which takes in the players list as an argument

print(new_team)