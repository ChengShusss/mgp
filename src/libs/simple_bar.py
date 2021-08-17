#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
src: 

"""

import matplotlib.pyplot as plt
import random


def plot_simple_bar(x, y, config):
    # 加载配置
    width = config.get("width", 0.8)
    title = config.get("title", "default title")
    color_map = config.get("color_list", ['red' for _ in x])
    y_lim = config.get("ylim", (min(y), max(y)))


    plt.bar(x, y, width, color=color_map)
    plt.ylim(y_lim)


    # 设置题目和图例
    plt.title(title)
    if config.get("legend", True):
        plt.legend()



def main():
    # 配置绘图细节
    config = {
        "width": 0.8,
        "title": "Temp for bar",
        "color_map_name": "tab20c",
        "legend": False,
        "ylim": (0, 200)
    }

    # 生成假数据
    x = [x + 1 for x in list(range(100))]
    y = [random.randint(10, 100) for _ in x]
    color_list = ['r' for _ in x]
    for i in range(len(x) >> 1):
        color_list[random.randint(0, len(x) - 1)] = 'b'
    config["color_list"] = color_list

    # 绘图
    plot_simple_bar(x, y, config)
    plt.show()

if (__name__ == "__main__"):
    main()
