import Network
import DatabaseIP
from rsa import pkcs1
from rsa import sign, newkeys
import hashlib
import json
import datetime
import time
import Mining
import RSASign
import rsa
from EncDec import enc, dec
import RSASign
import save_changes

ok, ck = rsa.newkeys(512)
_ok = str(ok.e) + ' ' + str(ok.n)

for i in range(10):
    data = {
            'fio': 'Oksana',
            'OKo': _ok,
            'role': '1'
            }
    trans = {
             'code': str(1),
             'ok': _ok,
             'data': json.dumps(data, sort_keys=True)
             }

    for_sign = trans.copy()




    #берет словарь / возвращает словарь
    # print('Только создали транзакцию')
    trans = RSASign.RSASign().get_sign(for_sign, ck)

    time.sleep(0.25)

    trans.update({'type':'transaction'})
    trans = enc(trans)

    #берет битовую строку
    Network.Network().send_message(trans)

# block = enc(block)
# Network.Network().send_message(block)
#
#
# m = Maining.Maining()
# m.collecting_block(1)

# save_changes.Changes().get_transaction_from_bd(8)