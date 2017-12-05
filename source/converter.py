#-*- coding:utf8:*-

from collections import OrderedDict
from pdb import set_trace
from copy import deepcopy


class FieldConverter:
    fieldsmap = {
        # bool
        "b": "BooleanField",

        # integer
        "B": "BigIntegerField",
        "p": "PositiveIntegerField",
        "pm": "PositiveSmallIntegerField",
        "f": "FloatField",
        "s": "SmallIntegerField",

        # char
        "c": "CharField",
        "t": "TextField",

        # date
        "d": "DateTimeField",
        "tm": "TimeField",

        # special
        "i": "GenericIPAddressField",
        "uu": "UUIDField",
        "u": "URLField",
        "e": "EmailField",

        # foreign
        "fo": "ForeignKey",
    }

    template = "    {n} = {t}(\n        \"{a}\",{params}\n    )"

    def feed(self, field):
        datas = deepcopy(field)
        datas["t"] = self.fieldsmap[datas["t"]]

        fields = field["fields"]

        converter = ParamsConverter()
        params = converter.feed(fields)

        if params:
            params = "\n{}".format(params)

        datas["params"] = params

        return  self.template.format(**datas)


class ParamsConverter:
    spaces = 8 * " "

    paramsmap = OrderedDict([
        ("m", ["max_length", "num"]),
        ("d", ["default", "mix"]),

        ("b", ["blank", "bool"]),
        ("n", ["null", "bool"]),

        ("c", ["choices", "value"]),
        ("v", ["validators", "validators"]),

        ("aa", ["auto_now_add", "bool"]),
        ("an", ["auto_now", "bool"]),

        ("h", ["help_text", "str"]),
        ("v", ["verbose_name", "str"]),
    ])

    def feed(self, datas):
        rsets = self.result_set(datas)
        result = self.pretty_code(rsets) 

        return  result

    def result_set(self, datas):
        rsets = []

        for key, params in self.paramsmap.items(): 
            value = datas.get(key)

            if value == None:
                continue

            field_name, method_name = params

            res = getattr(self, "get_{}".format(method_name))(value)
            res = "{} = {}".format(field_name, res)

            rsets.append(res)

        return  rsets

    def pretty_code(self, rsets, width = 80):
        line = self.spaces
        code = ""

        for res in rsets:
            res_utf8_len = len(res.encode())
            line_utf8_len = len(line.encode())

            if res_utf8_len + line_utf8_len >= width and line != self.spaces:
                code += "{}\n".format(line)
                line = self.spaces

            if line.endswith(","):
                line += " "

            line += "{},".format(res)

        code = line if not code else code + line

        return  code

    def get_value(self, value):
        return  str(value)

    def get_bool(self, value):
        return  bool(value)

    def get_str(self, value):
        return  "\"{}\"".format(value)

    def get_num(self, value):
        return  value

    def get_mix(self, value):
        if isinstance(value, str):
            return  self.get_str(value)

        if isinstance(value, bool):
            return  self.get_bool(value)

        return  self.get_num(value)

