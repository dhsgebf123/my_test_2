#!/usr/bin/env python3
"""随机打印脑筋急转弯."""

from __future__ import annotations

import random
import textwrap

BRAIN_TEASERS: list[tuple[str, str]] = [
    ("什么东西越洗越脏？", "水"),
    ("什么帽不能戴？", "螺丝帽"),
    ("什么车最不听话？", "油嘴滑舌(油嘴滑舌车)"),
    ("什么东西有五个头却只有一条腿？", "五角星"),
    ("小王的妈妈有三个孩子，大毛、二毛，第三个是谁？", "小王"),
    ("明明是鸡蛋却不能吃，是什么？", "脸上的鸡蛋型痘"),
    ("什么东西没口却能吃饭？", "餐桌"),
    ("什么动物没有方向感？", "麋鹿(迷路)"),
    ("什么瓜不能吃也不能丢？", "傻瓜"),
    ("什么水永远用不完？", "泪水"),
    ("什么桥没有人能从桥上走过去？", "彩虹"),
    ("什么东西有头无尾？", "硬币"),
    ("什么东西大家都不喜欢吃？", "吃亏"),
    ("为什么狗越长越大却从不换牙？", "因为它的牙够用"),
    ("什么事你明明没做却会被惩罚？", "做梦"),
    ("什么样的球不需要气？", "地球"),
    ("太阳和月亮有什么区别？", "一个在白天出来，一个在晚上加班"),
    ("什么东西越冷越爱出来？", "鼻涕"),
    ("什么瓜最甜？", "傻瓜(因为人人都夸)"),
    ("什么时候四减一等于五？", "算错的时候"),
]


def get_random_teaser() -> tuple[str, str]:
    """Return a random brain teaser (question, answer)."""
    return random.choice(BRAIN_TEASERS)


def main() -> None:
    """Print ``count`` random brain teasers."""
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=1,
        help="number of brain teasers to output",
    )
    args = parser.parse_args()

    for _ in range(max(1, args.count)):
        q, a = get_random_teaser()
        print(textwrap.fill(q))
        print(f"答：{a}\n")


if __name__ == "__main__":
    main()
