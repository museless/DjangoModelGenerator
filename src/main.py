#!/usr/bin/python3
#-*- coding:utf8 -*-

import sys

from copy import deepcopy
from pdb import set_trace
from collections import OrderedDict

from converter import FieldConverter


Data = {
    "fields": [
        {
            "n": "sports",
            "t": "c",
            "a": "运动",

            "fields": {
                "m": 128,
                "h": "Note: 以英文,分割",
                "d": "",
                "b": 1,
            }
        },

        {
            "n": "sweat_rate",
            "t": "c",
            "a": "出汗率",

            "fields": {
                "m": 1,
                "d": "",
                "b": 1,
                "c": "FUCKER_CHOICES",
            }
        },
    ]
}


def main(argv = sys.argv):
    fields = Data.get("fields")
    converter = FieldConverter()

    for field in fields:
        print("{}\n".format(converter.feed(field)))


if __name__ == "__main__":
    main()

