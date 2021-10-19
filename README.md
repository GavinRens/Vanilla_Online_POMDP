# Vanilla_Online_POMDP
A simple POMDP planner for online planning from a given belief state. No pruning or any optimization is applied. Can be used for only very small environments.

Run main.py
Set "max_episode_length" and "trials" as desired

In Vanilla_POMDP.py, set D (the look-ahead depth / horizon)

The action stochasticity factor can be set in procedure initializeStateAndBelief() -> last argument of class POMDP
