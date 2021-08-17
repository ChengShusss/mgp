#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
    if a plate is heated evenly, but has some random factors,
    how does its temprature increases?
"""

import random
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../libs'))
from heat_map import plot_heat_map
import matplotlib.pyplot as plt


# ----------------
# Const setting
# ----------------
ROW_SIZE = 10
COL_SIZE = 10
CONDUCT_COEFFICIENT = 0.1
ITER_TIME = 100

DELTA_DOWN_LIM = 0.01
DELTA_GAP = 0.03


class Plate:
    def __init__(self, init_temp, iter_time) -> None:
        self.init_t = init_temp
        self.iter_time = iter_time
        self.round = 0
        self.data = []
        for _ in range(ROW_SIZE):
            self.data.append([init_temp] * COL_SIZE)

    def update_one(self, i, j):
        delta = 0

        if i > 0:
            delta += CONDUCT_COEFFICIENT * \
                (self.data[i-1][j] - self.data[i][j])
        if i < ROW_SIZE - 1:
            delta += CONDUCT_COEFFICIENT * \
                (self.data[i+1][j] - self.data[i][j])
        if j > 0:
            delta += CONDUCT_COEFFICIENT * \
                (self.data[i][j-1] - self.data[i][j])
        if j < ROW_SIZE - 1:
            delta += CONDUCT_COEFFICIENT * \
                (self.data[i][j+1] - self.data[i][j])

    def update(self):
        for i in range(ROW_SIZE):
            for j in range(COL_SIZE):
                self.update_one(i, j)
        for i in range(ROW_SIZE):
            for j in range(COL_SIZE):
                self.data[i][j] += DELTA_DOWN_LIM \
                     + DELTA_GAP * random.random()


    def get_norm_data(self):
        min_t = self.init_t
        max_t = self.init_t + (
                (DELTA_GAP + DELTA_DOWN_LIM) * self.iter_time
            )
        dis = (max_t - min_t)
        res = []
        for i in range(ROW_SIZE):
            res.append([(x - min_t)/dis for x in self.data[i]])

        # res[0][0] = 1
        return res
    
    def get_norm_new(self):
        min_t, max_t = self.get_range()
        dis = (max_t - min_t)
        min_t -= dis
        max_t += dis
        # print(f"max:{max_t}, min{min_t}")
        res = []
        for i in range(ROW_SIZE):
            res.append([])
            for j in range(COL_SIZE):
                nor = (self.data[i][j] - min_t) / (3 * dis)
                if nor > 1:
                    nor = 1
                res[-1].append(nor)

        return res

    
    def get_range(self):
        min_t = min([min(x) for x in self.data])
        max_t = max(max(x) for x in self.data)
        return min_t, max_t


def plot(data):
    config = {
        "title": "Temprature",
        "legend": False,
        "color_map": "hot"
    }
    plot_heat_map(data, config)


def main():
    plate = Plate(10, ITER_TIME)

    plate.update()
    plt.ion()
    for i in range(ITER_TIME):
        plate.update()
        plt.clf()
        # data = plate.get_norm_new()
        data = plate.get_norm_data()
        plot(data)
        max_t = max([max(x) for x in data])
        min_t = min([min(x) for x in data])
        print(f"{i}: max{max_t:.2f}, min:{min_t:.2f}")
        plt.pause(0.5)
    #     plt.ioff()

        # print(plate.get_range())
    


if (__name__ == '__main__'):
    main()
