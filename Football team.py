class Team:
    '''Creates a Team object.'''

    team_list = set()

    def __init__(self, name):
        '''Creates the team 'name' and adds it to the 'team_list\''''
        self.players = set()
        self.name = name
        self.team_list.add(self.name)

    def add_player(self, known_name):
        '''Adds a player to a particular football team.'''
        if known_name not in Player.all_players:
            print(f"Sorry, the player known as {known_name} does not exit. Please create it first.")
        else:
            self.players.add(known_name)
            print(f'{known_name} has been added to the list.')

    def __repr__(self):
        '''Returns that the object is a football team and the players that belong to it.'''
        return f"{self.name} is a football club. All these players play for {self.name}:\n{self.players}"


class Player:
    '''Creates a Player object'''

    all_players = set()

    def __init__(self, known_name, team = None, role = None):
        '''Creates a player, relates it to a team and sets the role in the pitch.
        It adds the player to the all_players list.'''

        if team not in Team.team_list:
            print(f"Sorry, {team} team does not exit. Please create it first.")
        else:
            Player.all_players.add(known_name)
            self.known_name = known_name
            self.role = role
            self.team = team

    def __repr__(self):
        '''Returns information about the player. Whether is active or not and which team he plays for.'''
        if self.team == None and self.role == None:
            return f"{self.known_name} is a free player with no role set."
        elif self.team != None and self.role == None:
            return f"{self.known_name} plays for {self.team} but has no role set."
        elif self.team == None and self.role != None:
            return f"{self.known_name} is a {self.role} that does not play for any team."
        else:
            return f"{self.known_name} plays for {self.team} as a {self.role}."

