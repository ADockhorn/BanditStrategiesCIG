from plotbandits import plot_scenario
from banditstrategy import BanditStrategy, greedy, soft_max, epsilon_greedy, random_choice


def ucb1(bandit: BanditStrategy):
    """
        Pick the bandit according to the UCB1 strategy.
        Return the index of the winning bandit.
    """

    return 0


def decaying_epsilon_greedy(bandit: BanditStrategy, epsilon=0.1):
    """
        Pick the bandit according to the Decaying Epsilon Greedy strategy.
        Return the index of the winning bandit.
    """

    return 0


def get_scenario(scenario_id=1):
    scenario_dict = {
        1: [0.05, 0.03, 0.06],
        2: [0.1, 0.1, 0.1, 0.1, 0.9],
        3: [0.1, 0.11, 0.09, 0.095, 0.12],
        4: [0.01, 0.02, 0.03, 0.04, 0.05]
    }
    if i in scenario_dict:
        return scenario_dict[i]
    else:
        raise ValueError('Scenario id ' + str(i) + ' not included in scenario_dict. Either add the scenario' +
                         ' or choose on of the keys: ' + str(list(scenario_dict.keys())))


if __name__ == "__main__":
    algorithm_names = ["Greedy", "Random", "$\epsilon$ Greedy", "Softmax", "decaying $\epsilon$ Greedy", "UCB1"]
    strategies = [greedy, random_choice,
                  epsilon_greedy, soft_max,
                  decaying_epsilon_greedy, ucb1]

    # plot your own scenario
    scenario = [0.1, 0.9]
    plot_scenario(strategies=strategies, names=algorithm_names, scenario=scenario)

    # plot the predefined scenarios
    for i in [1, 2, 3, 4]:
        scenario = get_scenario(i)
        plot_scenario(strategies=strategies, names=algorithm_names, scenario=scenario)
