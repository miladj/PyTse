دریافت اطلاعات سایت
http://www.tsetmc.com

بروز رسانی اطلاعات نماد

```python
pytse.read_symbols()
```

بروز رسانی اطلاعات حقیقی حقوقی

```python
pytse.read_client_type()
```

پر شدن مقادیر میانگین حجم ماه و سهام شناور

بر روی آبجکت نماد باید فراخوانی شود مانند مثال پایین

```python
fill_data()
```

دریافت تاریخچه اطلاعات معاملاتی نماد(اطلاعات در خروجی متد قابل دریافت است)

```python
get_symbol_history()
```

```
pip install pytse
```

This is a http://www.tsetmc.com data crawler.

```python
from pytse.pytse import PyTse,SymbolData


if(__name__=="__main__"):
    PyTse.request_timeout = 20#changing timeout default=30 !apply to all requests
    pytse=PyTse()#read_symbol_data=True,read_client_type=False
    pytse.read_client_type() # در صورت نیاز به اطلاعات حقیقی
    symbols=pytse.symbols_data
    symbol=symbols["IRO1MKBT0001"]
    symbol.fill_data() #درصورت نیاز به اطلاعات "میانگین حجم ماه "و "سهام شناور" فرخوانی شود
    symbol_history_data=symbol.get_symbol_history()
    print(symbol_history_data["20210106"])
    print(symbol)
    print(symbol.pl)
    print(symbol.ct.Buy_CountI) #fill_data()
    print(symbol["ct"]["Buy_CountI"]) #fill_data()
    print(pytse.symbols_data_by_id["44891482026867833"])#دریافت اطلاعات نماد با isincode
    print(pytse.symbols_data_by_symbol["خساپا"])#دریافت اطلاعات با نماد Ver 1.6.2

```

You can refresh data by calling read_symbols

```python
pytse.read_symbols()
```

Read Client Type

```python
pytse.read_client_type()
```

|                  |                           |                                  |
| ---------------- | ------------------------- | -------------------------------- |
| فیلد             | توضیح                     |                                  |
| l18              | نماد                      |                                  |
| l30              | نام                       |                                  |
| tno              | تعداد معاملات             |                                  |
| tvol             | حجم معاملات               |                                  |
| tval             | ارزش معاملات              |                                  |
| py               | قیمت دیروز                |                                  |
| pf               | اولین قیمت                |                                  |
| pmin             | کمترین قیمت               |                                  |
| pmax             | بیشترین قیمت              |                                  |
| pl               | آخرین قیمت                |                                  |
| plc              | تغییر آخرین قیمت          |                                  |
| plp              | درصد تغییر آخرین قیمت     |                                  |
| pc               | قیمت پایانی               |                                  |
| pcc              | تغییر قیمت پایانی         |                                  |
| pcp              | درصد تغییر قیمت پایانی    |                                  |
| eps              | eps                       |                                  |
| pe               | p/e                       |                                  |
| tmin             | آستانه مجاز پایین         |                                  |
| tmax             | آستانه مجاز بالا          |                                  |
| z                | تعداد سهام                |                                  |
| mv               | ارزش بازار                |                                  |
| pd1              | قیمت خرید - سطر اول       |                                  |
| zd1              | تعداد خریدار - سطر اول    |                                  |
| qd1              | حجم خرید- سطر اول         |                                  |
| po1              | قیمت فروش - سطر اول       |                                  |
| zo1              | تعداد فروشنده - سطر اول   |                                  |
| qo1              | حجم فروش- سطر اول         |                                  |
| pd2              | قیمت خرید - سطر دوم       |                                  |
| zd2              | تعداد خریدار - سطر دوم    |                                  |
| qd2              | حجم خرید- سطر دوم         |                                  |
| po2              | قیمت فروش - سطر دوم       |                                  |
| zo2              | تعداد فروشنده - سطر دوم   |                                  |
| qo2              | حجم فروش- سطر دوم         |                                  |
| pd3              | قیمت خرید - سطر سوم       |                                  |
| zd3              | تعداد خریدار - سطر سوم    |                                  |
| qd3              | حجم خرید- سطر سوم         |                                  |
| po3              | قیمت فروش - سطر سوم       |                                  |
| zo3              | تعداد فروشنده - سطر سوم   |                                  |
| qo3              | حجم فروش- سطر سوم         |                                  |
| pd4              | قیمت خرید - سطر چهارم     |                                  |
| zd4              | تعداد خریدار - سطر چهارم  |                                  |
| qd4              | حجم خرید- سطر چهارم       |                                  |
| po4              | قیمت فروش - سطر چهارم     |                                  |
| zo4              | تعداد فروشنده - سطر چهارم |                                  |
| qo4              | حجم فروش- سطر چهارم       |                                  |
| pd5              | قیمت خرید - سطر پنجم      |                                  |
| zd5              | تعداد خریدار - سطر پنجم   |                                  |
| qd5              | حجم خرید- سطر پنجم        |                                  |
| po5              | قیمت فروش - سطر پنجم      |                                  |
| zo5              | تعداد فروشنده - سطر پنجم  |                                  |
| qo5              | حجم فروش- سطر پنجم        |                                  |
| bvol             | حجم مبنا                  |                                  |
| cs               | گروه صنعت                 |                                  |
| ct.Buy_CountI    | تعداد خریدار حقیقی        | با فراخوانی متد read_client_type |
| ct.Buy_CountN    | تعداد خریدار حقوقی        | با فراخوانی متد read_client_type |
| ct.Buy_I_Volume  | حجم خرید حقیقی            | با فراخوانی متد read_client_type |
| ct.Buy_N_Volume  | حجم خرید حقوقی            | با فراخوانی متد read_client_type |
| ct.Sell_CountI   | تعداد فروشنده حقیقی       | با فراخوانی متد read_client_type |
| ct.Sell_CountN   | تعداد فروشنده حقوقی       | با فراخوانی متد read_client_type |
| ct.Sell_I_Volume | حجم فروش حقیقی            | با فراخوانی متد read_client_type |
| ct.Sell_N_Volume | حجم فروش حقوقی            | با فراخوانی متد read_client_type |
| QTotTran5JAvg    | میانگین حجم ماه           | با فراخوانی متد fill_data        |
| KAjCapValCpsIdx  | سهام شناور                | با فراخوانی متد fill_data        |
| SectorPE         | P/E گروه                  | با فراخوانی متد fill_data        |
