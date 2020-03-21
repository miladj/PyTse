
from pytse.pytse import PyTse,SymbolData
from unittest.mock import patch
from pathlib import Path
from nose.tools import assert_equal,assert_is_not_none,assert_is_instance

def test_server_response():

    with patch('pytse.pytse.PyTse._PyTse__get_data_from_server') as mock_get:
        
        mock_get.return_value=Path("tests/sampledata.txt").read_text()
        
        pytse=PyTse()
        symbols=pytse.symbols_data
        symbol=symbols["IRO1NIKI0001"]
        print(symbol)
        assert_is_not_none(symbol)
        assert_is_instance(symbol,SymbolData)
        assert_equal(symbol.tvol,8566607)
        assert_equal(symbol.pmax,11396)
        assert_equal(symbol.pmin,10570)
        assert False
        
        
