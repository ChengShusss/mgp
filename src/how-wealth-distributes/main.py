#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
    if a plate is heated evenly, but has some random factors,
    how does its temprature increases?
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../libs'))

import matplotlib.colors
import matplotlib.cm
import matplotlib.pyplot as plt
from simple_bar import plot_simple_bar
import random



EXCHANGE_VALUE = 1
PERSON_NUMBER = 100
INIT_WEALTH = 100
MAX_VALUE = 450


class Person:
    def __init__(self, index, wealth) -> None:
        self.index = index
        self.wealth = wealth

    def decrease(self):
        if self.wealth <= 0 :
            return 0
        self.wealth -= EXCHANGE_VALUE
        return EXCHANGE_VALUE

    def increase(self, v):
        self.wealth += v

    def get_value(self):
        return self.wealth
    
    def get_index(self):
        return self.index


class Group:
    def __init__(self, n, init_w) -> None:
        self.group = []
        for i in range(n):
            self.group.append(Person(i + 1, init_w))

    def exchange_once(self):
        for i in range(len(self.group)):
            v = self.group[i].decrease()
            target = random.randint(0, len(self.group) - 1)
            self.group[target].increase(v)

    def get_distri(self):
        return [x.get_value() for x in self.group]

    def get_distri_sorted(self):
        return sorted(self.get_distri())
    
    def get_index(self):
        return [x.get_index() for x in self.group]
    
    def get_sorted_data(self):
        res = []
        for i in range(len(self.group)):
            res.append([
                self.group[i].get_index(),
                self.group[i].get_value()
            ])
        res.sort(key=lambda x:x[1])

        return res
    
    def sort_by_wealth(self):
        self.group.sort(key=lambda x: x.get_value())
        for i in range(len(self.group)):
            self.group[i].index = i + 1


def plot(group: Group, i):
    
    indexs = group.get_index()
    res = group.get_sorted_data()
    maxx = max(x[1] for x in res)

    config = {
            "width": 0.8,
            "title": f"Result of round {i} (max{maxx})",
            "color_map_name": "tab20c",
            "legend": False,
            "ylim": (0, MAX_VALUE)
        }
    norm = matplotlib.colors.Normalize(vmin=0, vmax=150)
    mapper = matplotlib.cm.ScalarMappable(
        norm=norm, cmap=matplotlib.cm.get_cmap("hot"))
    config["color_list"] = [mapper.to_rgba(x[0]) for x in res]
    plot_simple_bar(indexs, [x[1] for x in res], config=config)


def main():
    group = Group(PERSON_NUMBER, INIT_WEALTH)
    
    rounds_per_time = 500

    for _ in range(rounds_per_time):
        group.exchange_once()
    group.sort_by_wealth()

    plt.ion()
    plt.tight_layout()
    for i in range(20):
        for _ in range(rounds_per_time):
            group.exchange_once()
        plt.clf()
        plot(group, (i + 1) * rounds_per_time)
        plt.pause(0.5)
    plt.ioff()
    
    plt.show()

    print(group.get_sorted_data())



if (__name__ == "__main__"):
    main()
