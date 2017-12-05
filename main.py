#-*- coding:utf8 -*-

import sys

from source.generator import generator


Dataset = {
    "fields": [
        {
            "n": "test",
            "t": "c",
            "a": "Test",

            "fields": {
                "m": 128
            }
        }
    ]
}


def main(argv = sys.argv):
    generator(Dataset)


if __name__ == "__main__":
    main()

