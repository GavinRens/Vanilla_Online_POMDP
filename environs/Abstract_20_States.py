import random

env_name = 'Abstract_20_States'

class POMDP:
    def __init__(self, States, Actions, Observations, Stochasticity_Factor=0):
        self.S = States
        self.A = Actions
        self.Z = Observations
        self.SF = Stochasticity_Factor

    def Reward(self, a, s):
        if s == 's14':
            return 20
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
                if ss == 's10':
                    return self.SF
                if ss == 's1':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's2':
                    return self.SF
                if ss == 's1':
                    return 1 - self.SF

        if s == 's2':
            if a == 'a':
                if ss == 's9':
                    return self.SF
                if ss == 's2':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's3':
                    return self.SF
                if ss == 's2':
                    return 1 - self.SF

        if s == 's3':
            if a == 'a':
                if ss == 's8':
                    return self.SF
                if ss == 's3':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's4':
                    return self.SF
                if ss == 's3':
                    return 1 - self.SF

        if s == 's4':
            if a == 'a':
                if ss == 's7':
                    return self.SF
                if ss == 's4':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's5':
                    return self.SF
                if ss == 's4':
                    return 1 - self.SF

        if s == 's5':
            if a == 'a':
                if ss == 's6':
                    return self.SF
                if ss == 's5':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's5':
                    return self.SF
                if ss == 's5':
                    return 1 - self.SF

        if s == 's6':
            if a == 'a':
                if ss == 's15':
                    return self.SF
                if ss == 's6':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's6':
                    return self.SF
                if ss == 's6':
                    return 1 - self.SF

        if s == 's7':
            if a == 'a':
                if ss == 's14':
                    return self.SF
                if ss == 's7':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's6':
                    return self.SF
                if ss == 's7':
                    return 1 - self.SF

        if s == 's8':
            if a == 'a':
                if ss == 's13':
                    return self.SF
                if ss == 's8':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's7':
                    return self.SF
                if ss == 's8':
                    return 1 - self.SF

        if s == 's9':
            if a == 'a':
                if ss == 's12':
                    return self.SF
                if ss == 's9':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's8':
                    return self.SF
                if ss == 's9':
                    return 1 - self.SF

        if s == 's10':
            if a == 'a':
                if ss == 's11':
                    return self.SF
                if ss == 's10':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's9':
                    return self.SF
                if ss == 's10':
                    return 1 - self.SF

        if s == 's11':
            if a == 'a':
                if ss == 's16':
                    return self.SF
                if ss == 's11':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's12':
                    return self.SF
                if ss == 's11':
                    return 1 - self.SF

        if s == 's12':
            if a == 'a':
                if ss == 's17':
                    return self.SF
                if s == 's12':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's13':
                    return self.SF
                if ss == 's12':
                    return 1 - self.SF

        if s == 's13':
            if a == 'a':
                if ss == 's18':
                    return self.SF
                if ss == 's13':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's14':
                    return self.SF
                if ss == 's13':
                    return 1 - self.SF

        if s == 's14':
            if a == 'a':
                if ss == 's19':
                    return self.SF
                if ss == 's14':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's15':
                    return self.SF
                if ss == 's14':
                    return 1 - self.SF

        if s == 's15':
            if a == 'a':
                if ss == 's20':
                    return self.SF
                if ss == 's15':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's15':
                    return self.SF
                if ss == 's15':
                    return 1 - self.SF

        if s == 's16':
            if a == 'a':
                if ss == 's16':
                    return self.SF
                if ss == 's16':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's17':
                    return self.SF
                if ss == 's16':
                    return 1 - self.SF

        if s == 's17':
            if a == 'a':
                if ss == 's17':
                    return self.SF
                if ss == 's17':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's18':
                    return self.SF
                if ss == 's17':
                    return 1 - self.SF

        if s == 's18':
            if a == 'a':
                if ss == 's18':
                    return self.SF
                if ss == 's18':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's19':
                    return self.SF
                if ss == 's18':
                    return 1 - self.SF

        if s == 's19':
            if a == 'a':
                if ss == 's19':
                    return self.SF
                if ss == 's19':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's20':
                    return self.SF
                if ss == 's19':
                    return 1 - self.SF

        if s == 's20':
            if a == 'a':
                if ss == 's1':
                    return self.SF
                if ss == 's1':
                    return 1 - self.SF
            if a == 'b':
                if ss == 's1':
                    return self.SF
                if ss == 's1':
                    return 1 - self.SF

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

    States = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16',
              's17', 's18', 's19', 's20']
    Actions = ['a', 'b']
    Observations = ['u', 'v', 'w', 'x']

    initial_state = 's1'
    initial_belief = {'s1': 1, 's2': 0, 's3': 0, 's4': 0, 's5': 0, 's6': 0, 's7': 0, 's8': 0, 's9': 0, 's10': 0,
                      's11': 0, 's12': 0, 's13': 0, 's14': 0, 's15': 0, 's16': 0, 's17': 0, 's18': 0, 's19': 0, 's20': 0}

    M = POMDP(States, Actions, Observations)

    return initial_state, initial_belief

