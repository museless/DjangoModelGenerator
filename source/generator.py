#-*- coding:utf8 -*-

from pdb import set_trace

from .converter import FieldConverter


def generator(dataset):
    fields = dataset.get("fields")
    converter = FieldConverter()

    for field in fields:
        print("{}\n".format(converter.feed(field)))

