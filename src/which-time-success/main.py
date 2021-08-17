#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../libs'))
from stacked_bar import plot_stacked_bar

def get_next(p: int, distribution: list):
    """Return next round distribution.

    Distribution represents the success times distribution after certain 
    round, assuming this game is independent repeated experiment.
    Given distribution in this round and the probability of success,
    return the distribution in next round.

    Args:
        p: The probability of success.
        distribution: The distribution of this round.

    Returns:
        A list contains the distribution of next round.
        res[i] represent the probability of having i+1 times success.

        [0.125, 0.375, 0.375, 0.125]

    Raises:
        AssertError: when distribution is empty, or p exceeds allowed range.
    """

    assert len(distribution) > 0, "Distribution is Empty."
    assert 0 <= p <= 1, "p is more than 1 or less than 0."

    res = []
    for i in range(len(distribution)):
        if i == 0:
            # the first
            res.append(distribution[i] * (1-p))
        else:
            res.append(distribution[i-1] * p + distribution[i] * (1-p))

        if i == len(distribution) - 1:
            res.append(distribution[i] * p)

    return res


def get_process(p, round):
    distributions = [[1]]

    for i in range(1, round):
        temp = get_next(p, distributions[-1])
        distributions.append(temp)
    
    return distributions


def format_data(distributions):
    data = {}
    max_length = max([len(x) for x in distributions])
    for i in range(len(distributions)):
        for j in range(max_length):
            if j not in data:
                data[(j)] = {i:0}
            else:
                data[j][i] = 0
    for i in range(len(distributions)):
        for j in range(len(distributions[i])):
                data[j][i] = distributions[i][j]
    
    return data




def main():
    config = {
        "width": 0.8,
        "title": "Success Time Distribution",
        "color_map_name": "tab20c",
        "legend": False
    }
    distributions = get_process(0.5, 20)
    data = format_data(distributions)
    # print(data)
    plot_stacked_bar(data, config)

if (__name__ == "__main__"):
    main()