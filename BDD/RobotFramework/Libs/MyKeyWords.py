from robot.api import logger
from robot.api.deco import keyword


class MyKeyWords:
    
    @keyword('Dictionary ${dic} should contain ${value}')
    def dictionary_should_contain_value(self, dic, value):
        """Dictionary should contain given value on the first level of keys"""
        
        if value.lower() == "empty": value = []
        values = list(dic.values())

        logger.info(f"Target dict is: {dic}")
        logger.info(f"Target value is: {value}")

        try:
            if value == []: assert len(values) == 0
            else: assert value in str(values)
        except AssertionError:
            raise AssertionError("{} не содержит {}".format(dic.values(), value))
