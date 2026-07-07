import torch
import torch.nn as nn
import torch.nn.functional as F

# The core of the DQN 

class NeuralNetwork(nn.Module):

    def __init__(self, input_size, hidden_size=128, output_size=4):
        super().__init__()

        # input_size example. radius 2 => 5*5 fields => 25 + {hunger, lenght, lifetime} => 28
        # hidden_size amopunt of nurons in the hidden layer (64 and 256 can be tested)
        # output_size 4 possible action (up, down, left, right)

        self.linear1 = nn.Linear(input_size, hidden_size) # Output=Input×Gewicht+Bias (28 → 128)
        self.linear2 = nn.Linear(hidden_size, hidden_size) # komplex relation learning (128 → 128)
        self.linear3 = nn.Linear(hidden_size, output_size) # find the resulting output (128 → 4)


    # the way the Network takes

    def forward(self, x):

        # check input
        if len(x.shape) == 1:
            x = x.unsqueeze(0)

        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = self.linear3(x)

        return x

# return how good each action is 