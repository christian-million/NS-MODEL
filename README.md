# Disclaimer

I am trying to replicate the simulation model presented in the following youtube video using python: https://www.youtube.com/watch?v=0ZGbIKd0XrM&vl=en

The thoughts and ideas presented in that video are not my own and all credit should go to the owner of that channel / video / content. I am using the thoughts and ideas in that video educationally - as a prompt to improve my skills in python.

# Overview

This is an offshoot of a school assignment [here]().

This repository packages the simulation specific code into a package that can be used on its own, or plugged into another GUI / API.

# Installation

```python
pip install --upgrade git+https://github.com/christian-million/NS-MODEL.git
```

# Usage

```python
from ns_model import Model

test_model = Model()

test_model.run()

print(test_model.pop_sum)
```

# TODO

Improvements that need to be made:

- Do not remove dead agents *during* a `for` loop

- Restructure so that all moves are evaluated first, then executed simultaneously

- Look for opportunities to reduce run time / improve efficiency


# Parameter Descriptions

## Settings

- `N_AGENTS`: The initial population size of the model

- `N_FOOD`: The amount of food available on each new `day`

- `N_DAYS`: How many `days` the model will run

- `DAILY_STEPS`: How many `steps` are available in each `day`

## Environment

- `PREDATOR_RATIO`: The percent difference in `size` between `Agents` that dictates who is prey / predator. (e.g., `Agent` A is 20% larger than `Agent` B. `Agent` A is a predator to `Agent` B)

- `FOOD_SIZE`: How big is the food. This impacts an Agents ability to `sense` the food.

- `FOOD_VALUE`: How nutritious is the food.

- `EAT_DIST`: How close an `Agent` has to be in order to eat the food / other `Agent`.

- `HEIGHT`: The Y value of the environment grid

- `WIDTH`: The X value of the environment grid

- `HEADING_MOD`: When `wandering` how many degrees (+-) can an `Agents` `heading` change

- `STEP_BUFFER`: How many steps Agents will allow themselves to begin heading home. If it will take X steps to get home, the agent will start heading home at X + STEP_BUFFER steps remaining.

## Mutation

- `MUTATION_RATE`: How likely is a mutation during reproduction

- `REPRODUCTION_MOD`: What percentage of energy (relative to it's own) must a Agent eat in order to reproduce.  

- `SPEED`: Speed of initial cohort of Agents (Distance traveled in 1 step)

- `SIZE`: Size of initial cohort of Agents (Radius of body)

- `SENSE`: Sense of initial cohort of Agents (Radius of detection)

- `SPEED_MOD`: What percentage can speed increase/decrease on mutation

- `SIZE_MOD`: What percentage can size increase/decrease on mutation

- `SENSE_MOD`: What percentage can sense increase/decrease on mutation

- `SPEED_ALLOW`: Allow speed mutations?

- `SIZE_ALLOW`: Allow size mutations?

- `SENSE_ALLOW`: Allow sense mutations?
