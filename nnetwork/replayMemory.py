from collections import deque
import random

# A collection of past moves to give the DQN experiences

class ReplayMemory:

    # how mutch do you want to "remember"
    def __init__(self, capacity=100_000):

        self.memory = deque(maxlen=capacity)

    # I was in state A and did Action A'. I got this reward and went to state b
    # call after each turn
    def push(self, state, action, reward, next_state, done):

        self.memory.append(
            (state, action, reward, next_state, done)
        )

    # find a random experiences
    # giving th leatest would be counter productiv
    def sample(self, batch_size):

        return random.sample(self.memory, batch_size)

    def __len__(self):

        return len(self.memory)


#
#1. play alot of steps.
#2. gain experiences.
#3. use 64 to train the next gen.
#