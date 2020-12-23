from .agents import Agent, Food
from random import shuffle
import json
import os


def get_defaults(verbose=False):
    '''Returns a dictionary of default parameters'''
    location = os.path.dirname(os.path.realpath(__file__))
    my_file = os.path.join(location, 'defaults.json')
    with open(my_file) as f:
        p = json.load(f)
        params = {key: value.get("value") for key, value in p.items()}

    # Return parameters with descriptions and min/max values
    if verbose:
        return p

    return params


class Model:
    '''Initializes, Runs, and Captures the interactions between Agents and Food'''
    def __init__(self, params=None):
        if params is None:
            params = get_defaults()

        self.params = params
        self.agents = []
        self.agent_count = 0
        self.food = []
        self.food_count = 0
        self.current_day = 0
        self.remaining_steps = self.params["DAILY_STEPS"]

        # Data Capture Attributes
        self.data = {"pop_sum": {"day": [], "agents": []},
                     "attr_sum": {"day": [], "avg_speed": [], "avg_size": [], "avg_sense": []},
                     "agent_data": {"id": [], "birthday": [], "deathday": [],
                                    "speed": [], "size": [], "sense": [],
                                    "reproduced": [], "food_eaten": [], "agents_eaten": []},
                     "food_data": {"id": [], "birthday": [], "deathday": []}}

        # Initialize original cohort of agents
        for i in range(self.params["N_AGENTS"]):
            self.agents.append(Agent(self, params['SPEED'], params['SIZE'], params['SENSE']))

        # Initialize original cohort of food
        self.restore_food()

    def restore_food(self):
        '''Determines how much food to add each day and adds it.'''
        remaining_food = 0

        # Count the number of living foods
        if self.food:
            for food in self.food:
                if food.alive:
                    remaining_food += 1

        # Add food up to N_FOOD amount
        for i in range(self.params["N_FOOD"] - remaining_food):
            new_food = Food(self)
            self.food.append(new_food)

    def step(self):
        '''Execute each living agents 'step' method'''
        for agent in self.agents:
            if agent.alive:
                agent.step()

    def day(self):
        '''Runs, resets, and captures the actions of each day'''
        # Let any applicable agents reproduce
        for agent in self.agents:
            if agent.reproduce:
                agent.birth()
                agent.reproduce = False

        # Reset remaining steps each day
        self.remaining_steps = self.params["DAILY_STEPS"]

        # Capture # of Alive Agents
        living_agents = 0
        speeds = []
        size = []
        sense = []
        for agent in self.agents:
            if agent.alive:
                living_agents += 1
                speeds.append(agent.speed)
                size.append(agent.size)
                sense.append(agent.sense)

        self.data["pop_sum"]["day"].append(self.current_day)
        self.data["pop_sum"]["agents"].append(living_agents)

        # Average Speed, but return 0 if no agents (i.e., all are dead)
        avg_speed = sum(speeds) / len(speeds) if len(speeds) else 0
        avg_size = sum(size) / len(size) if len(size) else 0
        avg_sense = sum(sense) / len(sense) if len(sense) else 0

        self.data["attr_sum"]["day"].append(self.current_day)
        self.data["attr_sum"]["avg_speed"].append(avg_speed)
        self.data["attr_sum"]["avg_size"].append(avg_size)
        self.data["attr_sum"]["avg_sense"].append(avg_sense)

        # Let agents move around and capture their movement
        for i in range(self.params["DAILY_STEPS"]):
            self.step()
            self.remaining_steps -= 1

        # After each agent has moved, let them reset
        for agent in self.agents:
            agent.end_day()

        # Reorder the Agents to reduce repeated bias
        shuffle(self.agents)

        # Restore the environments food to N_FOOD
        self.restore_food()

    def run(self):
        '''Runs the model for N_DAYS'''
        for day in range(self.params["N_DAYS"]):
            self.day()
            self.current_day += 1

        for agent in self.agents:
            if agent.alive:
                self.data["agent_data"]["id"].append(agent.id)
                self.data["agent_data"]["birthday"].append(agent.birthday)
                self.data["agent_data"]["deathday"].append(-1)
                self.data["agent_data"]["speed"].append(agent.speed)
                self.data["agent_data"]["size"].append(agent.size)
                self.data["agent_data"]["sense"].append(agent.sense)
                self.data["agent_data"]["reproduced"].append(agent.data['reproduced'])
                self.data["agent_data"]["food_eaten"].append(agent.data['food_eaten'])
                self.data["agent_data"]["agents_eaten"].append(agent.data['agents_eaten'])

    def results(self):
        '''Return the results in a single object.'''
        return self.data


if __name__ == '__main__':
    test_model = Model()
    test_model.run()
    print(test_model.data["agent_data"])
