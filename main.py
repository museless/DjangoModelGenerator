#-*- coding:utf8 -*-

import sys

from source.generator import generator


Dataset = {
    "model": {
    },

    "fields": [
        {
            "n": "channel",
            "t": "fo",
            "a": "Channel",

            "fields": {
                "od": "CASCADE",
            }
        },
        {
            "n": "code",
            "t": "pm",
            "a": "Http status code",

            "fields": {
                "b": 1
            }
        },
        {
            "n": "threshold",
            "t": "pm",
            "a": "Threshold for status code",

            "fields": {
                "b": 1,
            }
        },
        {
            "n": "email",
            "t": "e",
            "a": "Email for alarm",

            "fields": {
                "b": 1,
            }
        }
    ]
}


def main(argv = sys.argv):
    generator(Dataset)


if __name__ == "__main__":
    main()

