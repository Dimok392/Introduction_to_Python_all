from pydoc import plain
from dict import sit_place_dic_creation as SPDC
from create_row import look_up_name as LUN 
from create_row import take_from_base as TFB
from create_row import rewrite_base as RW
places = {}
places["101"] = SPDC()
print(places)
places["101"][2][3][1] = '0'

RW(places,"Class.json")