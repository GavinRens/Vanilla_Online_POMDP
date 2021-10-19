import random

env_name = 'Abstract_4_States'

class POMDP:
    def __init__(self, States, Actions, Observations, Stochasticity_Factor=0):
        self.S = States
        self.A = Actions
        self.Z = Observations
        self.SF = Stochasticity_Factor

    def Reward(self, a, s):
        if s == 's6':
            return 10
        else:
            return -1

    def ExpectedReward(self, a, b):
        r = 0
        for s, p in b.items():
            r += p * self.Reward(a, s)
        return r

    def T(self, s, a, ss):
        if s == 's1':
            if a == 'a':
                if ss == 's1':
                    return self.SF
                elif ss == 's2':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's1':
                    return 1
        if s == 's2':
            if a == 'b':
                if ss == 's2':
                    return self.SF
                elif ss == 's3':
                    return 1 - self.SF
            if a == 'a':
                if ss == 's2':
                    return 1
        if s == 's3':
            if a == 'a':
                if ss == 's3':
                    return self.SF
                elif ss == 's4':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's3':
                    return 1
        if s == 's4':
            if a == 'b':
                if ss == 's4':
                    return self.SF
                elif ss == 's5':
                    return 1 - self.SF
            if a == 'a':
                if ss == 's4':
                    return 1
        if s == 's5':
            if a == 'a':
                if ss == 's5':
                    return self.SF
                elif ss == 's6':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's5':
                    return 1
        if s == 's6':
            if a == 'b':
                if ss == 's6':
                    return self.SF
                elif ss == 's1':
                    return 1 - self.SF
            if a == 'a':
                if ss == 's1':
                    return 1

        return 0

    def SampleNextState(self, s, a):
        rand = random.uniform(0, 1)
        # print('rand:', rand)
        mass = 0
        for ss in self.S:
            mass += self.T(s, a, ss)
            # print('mass:', mass)
            # print("ss:", ss)
            if rand <= mass:
                return ss, self.T(s, a, ss)

    def O(self, z, a, s):
        if z == 'u':
            return 0.1
        if z == 'v':
            return 0.2
        if z == 'w':
            return 0.3
        if z == 'x':
            return 0.4

    def SampleObservation(self, a, s):
        mass = 0
        rand = random.uniform(0, 1)
        for z in self.Z:
            mass += self.O(z, a, s)
            if rand <= mass:
                return z





# Initialize system state and agent belief
def initializeStateAndBelief():
    global M

    States = ['s1', 's2', 's3', 's4', 's5', 's6']
    Actions = ['a','b']
    Observations = ['u', 'v', 'w', 'x']

    initial_state = 's1'
    initial_belief = {'s1':1, 's2':0, 's3':0, 's4':0, 's5':0, 's6':0}

    M = POMDP(States, Actions, Observations, 0.1)

    return initial_state, initial_belief
