import requests as rq
import re
from pytse.constants import BASE_URL,CLIENT_TYPE_URL

class SymbolData:
    __regex = re.compile(r"(QTotTran5JAvg\=\'(?P<QTotTran5JAvg>\d+)\')|(KAjCapValCpsIdx\=\'(?P<KAjCapValCpsIdx>\d+)\')")    
    def __init__(self):
        super().__init__()
    def fill_data(self):        
        symbol_page_raw=rq.get("http://www.tsetmc.com/loader.aspx?ParTree=151311&i={inscode}".format(inscode=self.inscode), timeout=(3, 20)).text        
        matches = SymbolData.__regex.finditer(symbol_page_raw)
        for match in matches:
            groups=match.groupdict()
            for key in groups:
                value=groups[key]
                if value:
                    self[key]=value

    def __setattr__(self, name, value):
        return super().__setattr__(name, value)

    def __setitem__(self, name, value):
        setattr(self, name, value)

    def __getitem__(self, name):
        return getattr(self, name)

    def get(self, name, default=None):
        return getattr(self, name, default)
    def toJSON(self):
        import json
        return json.dumps(self.__dict__,default=lambda x: x.__dict__)
    def __str__(self):
        return self.toJSON()


class PyTse:
    def __init__(self, read_symbol_data=True,read_client_type=False):
        super().__init__()
        self.__symbols_data = {}
        self.__symbols_data_by_id = {}
        if(read_symbol_data):
            self.read_symbols()
            if(read_client_type):
                self.read_client_type()

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
            symbol_data["zd"+item[1]] = item[3]
            symbol_data["pd"+item[1]] = item[4]
            symbol_data["po"+item[1]] = item[5]
            symbol_data["qd"+item[1]] = item[6]
            symbol_data["qo"+item[1]] = item[7]
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
    def __get_data_from_server(self,url):
        return rq.get(url, timeout=(3, 20)).text
        
    def read_client_type(self):
        client_type_body=self.__get_data_from_server(CLIENT_TYPE_URL)
        client_type_cp=client_type_body.split(";")
        for cols in [x.split(",") for x in client_type_cp]:
            if cols[0] in self.__symbols_data_by_id:
                self.__symbols_data_by_id[cols[0]].ct=SymbolData()
                self.__symbols_data_by_id[cols[0]].ct["Buy_CountI"] = int(cols[1])
                self.__symbols_data_by_id[cols[0]].ct["Buy_CountN"] = int(cols[2])
                self.__symbols_data_by_id[cols[0]].ct["Buy_I_Volume"] = int(cols[3])
                self.__symbols_data_by_id[cols[0]].ct["Buy_N_Volume"] = int(cols[4])
                self.__symbols_data_by_id[cols[0]].ct["Sell_CountI"] = int(cols[5])
                self.__symbols_data_by_id[cols[0]].ct["Sell_CountN"] = int(cols[6])
                self.__symbols_data_by_id[cols[0]].ct["Sell_I_Volume"] = int(cols[7])
                self.__symbols_data_by_id[cols[0]].ct["Sell_N_Volume"] = int(cols[8])
                
        
    def read_symbols(self):
        page_body = self.__get_data_from_server(BASE_URL)
        page_components = page_body.split("@")
        first_part, second_part, symbols_data, other_symbols_data, *other = page_components
        symbols_splitted = symbols_data.split(";")
        bestLimit = self.__read_best_limits(other_symbols_data)
        for symbol_raw_data in symbols_splitted:
            symbol = self.__parse_symbol_data(symbol_raw_data)
            if(symbol.inscode in bestLimit):
                self.__merge_symbol_data(symbol, bestLimit[symbol.inscode])
            self.__symbols_data[symbol.iid] = symbol
            self.__symbols_data_by_id[symbol.inscode] = symbol
        
