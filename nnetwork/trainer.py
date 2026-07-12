import torch
import torch.nn as nn
import torch.optim as optim
from copy import deepcopy


# It compares what the network believes (Q-value) with what it is actually supposed to learn (target Q-value), and then adjusts the network’s weights accordingly.
# Is the connection between ReplayMem and NeuralNetworkk
class Trainer:

    def __init__(
        self,
        model,
        learning_rate=0.001, # can be varied to high results in gaps to low = no progress
        gamma=0.99
    ):
        # the network that learns and changes
        self.policy_net = model

        # to copy the modle (gives advantages in training)
        self.target_net = deepcopy(model) 


        self.target_net.eval()

        self.gamma = gamma

        self.update_counter = 0
        self.target_update = 1000

        # after 1000 training cycles Policy Network --> Target Network

        # To change the weighs of the Network
        self.optimizer = optim.Adam(
            self.policy_net.parameters(), # all parameters off the Network
            lr=learning_rate
        )

        # A lotery function
        self.criterion = nn.MSELoss() # Mean Squared Error

    # One complete lerning step
    # batch is from the replay example batch = memory.sample(64)
    def train_step(self, batch):

        # states to tensor(a batch)
        states = torch.stack([
            torch.as_tensor(s, dtype=torch.float32)
            for s, _, _, _, _ in batch
        ])

        # collect actions 
        # in Form [top right bottom left]
        actions = torch.tensor([
            a for _, a, _, _, _ in batch
        ],dtype=torch.long)

        # possible reward of action
        rewards = torch.tensor([
            r for _, _, r, _, _ in batch
        ], dtype=torch.float32)

        # possible state of action after execution
        next_states = torch.stack([
            torch.as_tensor(ns, dtype=torch.float32)
            for _, _, _, ns, _ in batch
        ])

        dones = torch.tensor([
            d for _, _, _, _, d in batch
        ], dtype=torch.bool)

        #
        # Q(s,a)
        #

        current_q = self.policy_net(states)

        current_q = current_q.gather(
            1,
            actions.unsqueeze(1)
        ).squeeze(1)

        #
        # max_a Q(s',a)
        #

        with torch.no_grad():


            next_q = self.target_net(next_states)

            max_next_q = next_q.max(dim=1)[0]

            target_q = rewards + self.gamma * max_next_q # Bellman-Gleichung

            target_q[dones] = rewards[dones] # after death

        #
        # Gradient Descent
        #

        loss = self.criterion(
            current_q,
            target_q
        )

        self.optimizer.zero_grad()

        loss.backward()

        self.optimizer.step()

        self.update_counter += 1

        if self.update_counter >= self.target_update:

            self.target_net.load_state_dict(
            self.policy_net.state_dict()
            )

            self.target_net.eval()

            self.update_counter = 0

        return loss.item()



#Der komplette Ablauf als Bild
#ReplayMemory
#
#(state, action, reward, next_state, done)
#
#              |
#              v
#
#          Trainer
#
#              |
#       ----------------
#       |              |
#       v              v
#
# Policy Network   Target Network
#
# "Was denke ich?" "Was ist das Ziel?"
#
#       |
#       v
#
#    Loss berechnen
#
#       |
#       v
#
#   Backpropagation
#
#       |
#       v
#
# Policy Network verbessert sich