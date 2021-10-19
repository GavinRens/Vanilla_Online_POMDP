# This is a `vanilla' online POMDP algorithm
# It uses tree-search from a given belief, with no pruning.

import math
import random
import sys
import time
from pathlib import Path

Algorithm = "Vanilla-POMDP"
gamma = 0.95  # discount factor
D = 3  # tree depth

# BU_method = 'exact'
BU_method = 'MaT'

M = None  # the POMDP model


def ExactObsProb(a, z, b):
    global M
    prob = 0
    for ss in M.S:
        t = 0
        for s, p in b.items():
            t += M.T(s, a, ss) * p
        prob += M.O(z, a, ss) * t
    return prob


def BeliefUpdate(a, z, b):
    global M
    bb = {}  # New belief to be returned
    mass = 0
    for ss in M.S:  # for every possible state
        trans_prob = 0
        p_z = M.O(z, a, ss)  # prob. of perceiving z in new state, given a
        if p_z != 0:
            for s, p in b.items():  # for every state in the current belief state
                trans_prob += M.T(s, a, ss) * p  # expected prob. of reaching new state ss
            if trans_prob != 0:  # only add states that are possible (i.e. w/ non-zero prob)
                bb[ss] = p_z * trans_prob
                mass += bb[ss]
    for ss, pp in bb.items():
        bb[ss] = bb[ss] / mass
    return bb


def BeliefUpdateMT(a, z, b):
    global M
    bb = {}  # New belief to be returned
    mass = 0
    for ss in M.S:  # for every possible state
        trans_prob = 0
        p_z = M.O(z, a, ss)  # prob. of perceiving z in new state, given a
        if p_z != 0:
            for s, p in b.items():  # for every state in the current belief state
                trans_prob += M.T(s, a, ss) * p  # expected prob. of reaching new state ss
            if trans_prob != 0:  # only add states that are possible (i.e. w/ non-zero prob)
                bb[ss] = p_z * trans_prob
                mass += bb[ss]

    mean = round(mass / len(bb), 5)
    bbb = {}
    mass = 0

    # Keep only states with weight at least the mean
    for ss, pp in bb.items():
        if round(pp, 5) >= mean:
            bbb[ss] = pp
            mass += pp

    # Normalize
    for sss, ppp in bbb.items():
        bbb[sss] = ppp / mass
    return bbb


def Search(b, d):
    global gamma
    global M
    global Nodes
    global nuof_nodes_gened
    global D

    if d == 0: return 0

    maxValue = -sys.maxsize
    random.shuffle(M.A)
    for a in M.A:
        r = M.ExpectedReward(a, b)
        summ = 0
        for z in M.Z:
            if BU_method == 'exact':
                bb = BeliefUpdate(a, z, b)
            if BU_method == 'MaT':
                bb = BeliefUpdateMT(a, z, b)
            summ += ExactObsProb(a, z, b) * Search(bb, d - 1)
        if r + gamma * summ > maxValue:
            maxValue = r + gamma * summ

    return maxValue


def SelectAction(b, m):
    global gamma
    global D
    global M
    M = m
    global nuof_nodes_gened
    nuof_nodes_gened = 0

    bestAction = None
    maxValue = -sys.maxsize
    random.shuffle(M.A)
    for a in M.A:
        r = M.ExpectedReward(a, b)
        summ = 0
        for z in M.Z:
            if BU_method == 'exact':
                bb = BeliefUpdate(a, z, b)
            if BU_method == 'MaT':
                bb = BeliefUpdateMT(a, z, b)
            summ += ExactObsProb(a, z, b) * Search(bb, D)
        if r + gamma * summ > maxValue:
            maxValue = r + gamma * summ
            bestAction = a
    return bestAction

