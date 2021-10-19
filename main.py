import time
import statistics
from pathlib import Path

import environs.Abstract_4_States as env
# import environs.Abstract_20_States as env

import Vanilla_POMDP as algo


acts_executed = 0
max_episode_length = 20
trials = 5

def Trial():
    global nuof_nodes_gened
    global acts_executed
    acts_executed = 0

    Return = 0
    state, belief = env.initializeStateAndBelief()
    print('Initial state:', state)
    # print('Initial belief:', belief)

    for i in range(max_episode_length):
        action = algo.SelectAction(belief, env.M)
        # print('nuof_nodes:', algo.nuof_nodes)
        print('\naction:', action)
        reward = algo.M.Reward(action, state)
        # print('reward:', reward)
        Return += reward
        state, p = algo.M.SampleNextState(state, action)
        acts_executed += 1
        observation = algo.M.SampleObservation(action, state)
        belief = algo.BeliefUpdate(action, observation, belief)
        # print('belief', belief)

    return Return



if __name__ == "__main__":

    total_Returns = 0
    total_acts = 0
    AllReturns = []
    AllTimesPerAction = []

    for t in range(trials):
        tic = time.perf_counter()
        print('\n\n----------------------------------------------------------------')
        print('Trial', t+1)
        print('----------------------------------------------------------------')
        print(algo.Algorithm)
        print('---------------------------')
        print(env.env_name)
        print('---------------------------')

        Return = Trial()
        toc = time.perf_counter()
        AllReturns.append(Return)
        AllTimesPerAction.append(round((toc - tic) / acts_executed, 3))
    print('\n---------------------------')
    print(algo.Algorithm)
    print('---------------------------')
    print(env.env_name)
    print('---------------------------')
    print(f'D: {algo.D}, BU_method: {algo.BU_method}, gamma: {algo.gamma}, trials: {trials}, episode len: {max_episode_length}')
    print('Return:', AllReturns, 'Average:', statistics.mean(AllReturns), 'Std deviation:', statistics.stdev(AllReturns))
    print('Time per act:', AllTimesPerAction, 'Average:', statistics.mean(AllTimesPerAction), 'Std deviation:', statistics.stdev(AllTimesPerAction))
    # print('Update time per act:', total_duration2 / total_acts_executed)


