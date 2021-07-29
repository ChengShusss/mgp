#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
src: https://blog.csdn.net/m0_45209371/article/details/108241200

"""

import matplotlib.pyplot as plt
import random


def plot_stacked_bar(data, config):
    # 加载配置
    width = config.get("width", 0.8)
    title = config.get("title", "default title")
    color_map_name = config.get("color_map_name", "tab20")
    color_map = plt.get_cmap(color_map_name).colors

    # 每次堆叠时的基准：buttom和color_map
    pos = [0] * max([len(data[k]) for k in data.keys()])
    color_index = 0
    for label, line in data.items():
        # 获取每行的值
        values = list(line.values())
        plt.bar(line.keys(), values, width, bottom = pos, label = label, color=color_map[color_index])

        # 更新基准值
        pos = [pos[i] + values[i] for i in range(len(values))]
        color_index += 1

    # 设置题目和图例
    plt.title(title)
    if config.get("legend", True):
        plt.legend()

    plt.show()


def main():
    # 配置绘图细节
    config = {
        "width": 0.8,
        "title": "Temp for stacked bar",
        "color_map_name": "tab20c",
    }

    # 生成假数据
    data = {}
    series_count = 4
    data_length = 10
    series = [f"series-{x}" for x in range(series_count)]
    x_label = [f"7-{x+1}" for x in range(data_length)]
    for item in series:
        temp = {}
        for label in x_label:
            temp[label] = random.randint(5, 20)

        data[item] = temp
    # 自定义数据，请取消注释下一行，参考data变量的数据结构
    # print(data)

    # 绘图
    plot_stacked_bar(data, config)

if (__name__ == "__main__"):
    main()
