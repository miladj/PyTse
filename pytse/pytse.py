import requests as rq
from pytse.constants import BASE_URL

# array_map=('tsid','isin','symbol',"companyname","heven","firstprice","closingprice","lastprice","tradecount","tradevolume","tradevalue","lowprice","highprice","yesterdayprice","eps","basevolume","visitcount","flow","cs","highthreshold","lowthreshold","sharecount","yval")
# for index,i in enumerate(array_map):
#     print(f"array_map[{index}]=\"{i}\"")

# array_map = [""]*23
# array_map[0] = "inscode"
# array_map[1] = "iid"
# array_map[2] = "l18"
# array_map[3] = "l30"
# array_map[4] = "heven"
# array_map[5] = "pf"
# array_map[6] = "pc"
# array_map[7] = "pl"
# array_map[8] = "tno"
# array_map[9] = "tvol"
# array_map[10] = "tval"
# array_map[11] = "pmin"
# array_map[12] = "pmax"
# array_map[13] = "py"
# array_map[14] = "eps"
# array_map[15] = "bvol"
# array_map[16] = "visitcount"
# array_map[17] = "flow"
# array_map[18] = "cs"
# array_map[19] = "tmax"
# array_map[20] = "tmin"
# array_map[21] = "z"
# array_map[22] = "yval"

# # for index,i in enumerate(array_map):
# #     print(f"symbol.{i} = symbol_splitted_data[{index}]")

class SymbolData:
    def __init__(self):
        super().__init__()

    def __setattr__(self, name, value):
        return super().__setattr__(name, value)

    def __setitem__(self, name, value):
        setattr(self, name, value)

    def __getitem__(self, name):
        return getattr(self, name)

    def get(self, name, default=None):
        return getattr(self, name, default)

    def __str__(self):
        import json
        return json.dumps(self.__dict__)


class PyTse:
    def __init__(self, read_symbol_data=True):
        super().__init__()
        self.__symbols_data = {}
        if(read_symbol_data):
            self.read_symbols()

    @property
    def symbols_data(self):
        return self.__symbols_data

    def __parse_symbol_data(self, symbol_raw_data):
        symbol_splitted_data = symbol_raw_data.split(",")
        symbol = SymbolData()
        symbol.inscode = symbol_splitted_data[0]
        symbol.iid = symbol_splitted_data[1]
        symbol.l18 = symbol_splitted_data[2]
        symbol.l30 = symbol_splitted_data[3]
        symbol.heven = symbol_splitted_data[4]
        symbol.pf = symbol_splitted_data[5]
        symbol.pc = int(symbol_splitted_data[6])
        symbol.pl = int(symbol_splitted_data[7])
        symbol.tno = int(symbol_splitted_data[8])
        symbol.tvol = int(symbol_splitted_data[9])
        symbol.tval = symbol_splitted_data[10]
        symbol.pmin = int(symbol_splitted_data[11])
        symbol.pmax = int(symbol_splitted_data[12])
        symbol.py = int(symbol_splitted_data[13])
        symbol.eps = None if symbol_splitted_data[14] == "" else int(
            symbol_splitted_data[14])
        symbol.bvol = symbol_splitted_data[15]
        symbol.visitcount = symbol_splitted_data[16]
        symbol.flow = symbol_splitted_data[17]
        symbol.cs = symbol_splitted_data[18]
        symbol.tmax = symbol_splitted_data[19]
        symbol.tmin = symbol_splitted_data[20]
        symbol.z = symbol_splitted_data[21]
        symbol.yval = symbol_splitted_data[22]

        symbol.pcc = symbol.pc-symbol.py
        symbol.pcp = round(100*symbol.pcc/symbol.py, 2)
        symbol.plc = 0 if symbol.tno == 0 else int(symbol.pl) - symbol.py
        symbol.plp = 0 if symbol.tno == 0 else round(
            100*symbol.plc / symbol.py, 2)
        symbol.pe = "" if not symbol.eps else round(
            100*symbol.pc / symbol.eps, 2)
        return symbol

    def __merge_symbol_data(self, symbol_data, best_limit):
        if(not hasattr(symbol_data, "best_limit")):
            symbol_data["best_limit"] = []
        best_limit_data = symbol_data.best_limit
        for item in best_limit:
            pos = int(item[1])
            symbol_data["zo"+item[1]] = item[2]
            symbol_data["zd"+item[1]]: item[3]
            symbol_data["pd"+item[1]]: item[4]
            symbol_data["po"+item[1]]: item[5]
            symbol_data["qd"+item[1]]: item[6]
            symbol_data["qo"+item[1]]: item[7]
            best_limit_data.insert(pos, {"zo": item[2],
                                         "zd": item[3],
                                         "pd": item[4],
                                         "po": item[5],
                                         "qd": item[6],
                                         "qo": item[7]})

    def __read_best_limits(self, best_limit_raw_data):
        bestLimit = {}
        for item in best_limit_raw_data.split(";"):
            best_limits_splitted = item.split(",")
            d = bestLimit.get(best_limits_splitted[0])
            if(d == None):
                d = []
                bestLimit[best_limits_splitted[0]] = d
            d.append(best_limits_splitted)
        return bestLimit
    def __get_data_from_server(self):
        return rq.get(
            "http://www.tsetmc.com/tsev2/data/MarketWatchInit.aspx?h=0&r=0").text
    def read_symbols(self):
        page_body = self.__get_data_from_server()
        page_components = page_body.split("@")
        first_part, second_part, symbols_data, other_symbols_data, *other = page_components
        symbols_splitted = symbols_data.split(";")
        bestLimit = self.__read_best_limits(other_symbols_data)
        for symbol_raw_data in symbols_splitted:
            symbol = self.__parse_symbol_data(symbol_raw_data)
            if(symbol.inscode in bestLimit):
                self.__merge_symbol_data(symbol, bestLimit[symbol.inscode])
            self.__symbols_data[symbol.iid] = symbol
