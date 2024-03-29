from pytse.pytse import PyTse,SymbolData


if(__name__=="__main__"):
    PyTse.request_timeout = 20#changing timeout default=30 !apply to all requests
    pytse=PyTse()#read_symbol_data=True,read_client_type=False
    pytse.read_client_type() # در صورت نیاز به اطلاعات حقیقی
    symbols=pytse.symbols_data
    symbol=symbols["IRO1SIPA0001"]
    symbol.fill_data() #درصورت نیاز به اطلاعات "میانگین حجم ماه "و "سهام شناور" فرخوانی شود
    symbol_history_data=symbol.get_symbol_history()
    print(symbol_history_data["20210106"])
    print(symbol)
    print(symbol.pl)
    print(symbol.ct.Buy_CountI) #fill_data()
    print(symbol["ct"]["Buy_CountI"]) #fill_data(
    print(pytse.symbols_data_by_symbol["خساپا"])
    print(pytse.symbols_data_by_id["44891482026867833"])
