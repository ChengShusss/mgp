#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
src: https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html

"""
import random
import matplotlib.pyplot as plt


def plot_heat_map(data, config):
    # 加载配置
    # width = config.get("width", 0.8)
    title = config.get("title", "default title")
    color_map = config.get("color_map", "cool")
    norm = plt.Normalize(vmax=1, vmin=0)
    # color_map = plt.get_cmap(color_map_name).colors

    # 绘制热力图
    plt.imshow(data, cmap=color_map, norm=norm)


    # 设置题目和图例
    plt.title(title)
    if config.get("legend", True):
        plt.legend()

    plt.tight_layout()


def main():
    # 配置绘图细节
    config = {
        "width": 0.8,
        "title": "Temp for heat map",
        "color_map_name": "tab20c",
        "legend": False,
    }

    # 生成假数据
    data = []
    row_size = 4
    col_size = 10
    for i in range(row_size):
        data.append([])
        for j in range(col_size):
            data[i].append(random.random())

    # 自定义数据，请取消注释下一行，参考data变量的数据结构
    # print(data)

    # 绘图
    plot_heat_map(data, config)

if (__name__ == "__main__"):
    main()
    plt.show()