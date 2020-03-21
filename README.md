دریافت اطلاعات سایت
http://www.tsetmc.com

```
pip install pytse
```

This is a http://www.tsetmc.com data crawler.

 
```python
from pytse.pytse import PyTse,SymbolData


if(__name__=="__main__"):
    pytse=PyTse()    
    symbols=pytse.symbols_data
    symbol=symbols["IRO1MKBT0001"] 
    print(symbol.l30)

```
You can refresh data by calling read_symbols
```python
pytse.read_symbols()
```
|--- |--- |
|فیلد|توضیح|
|(l18)|نماد|
|(l30)|نام|
|(tno)|تعداد معاملات|
|(tvol)|حجم معاملات|
|(tval)|ارزش معاملات|
|(py)|قیمت دیروز|
|(pf)|اولین قیمت|
|(pmin)|کمترین قیمت|
|(pmax)|بیشترین قیمت|
|(pl)|آخرین قیمت|
|(plc)|تغییر آخرین قیمت|
|(plp)|درصد تغییر آخرین قیمت|
|(pc)|قیمت پایانی|
|(pcc)|تغییر قیمت پایانی|
|(pcp)|درصد تغییر قیمت پایانی|
|(eps)|eps|
|(pe)|p/e|
|(tmin)|آستانه مجاز پایین|
|(tmax)|آستانه مجاز بالا|
|(z)|تعداد سهام|
|(mv)|ارزش بازار|
|(pd1)|قیمت خرید - سطر اول|
|(zd1)|تعداد خریدار - سطر اول|
|(qd1)|حجم خرید- سطر اول|
|(po1)|قیمت فروش - سطر اول|
|(zo1)|تعداد فروشنده - سطر اول|
|(qo1)|حجم فروش- سطر اول|
|(pd2)|قیمت خرید - سطر دوم|
|(zd2)|تعداد خریدار - سطر دوم|
|(qd2)|حجم خرید- سطر دوم|
|(po2)|قیمت فروش - سطر دوم|
|(zo2)|تعداد فروشنده - سطر دوم|
|(qo2)|حجم فروش- سطر دوم|
|(pd3)|قیمت خرید - سطر سوم|
|(zd3)|تعداد خریدار - سطر سوم|
|(qd3)|حجم خرید- سطر سوم|
|(po3)|قیمت فروش - سطر سوم|
|(zo3)|تعداد فروشنده - سطر سوم|
|(qo3)|حجم فروش- سطر سوم|
|(bvol)|حجم مبنا|
|(cs)|گروه صنعت|