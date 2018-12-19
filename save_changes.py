import json
import rsa


class Changes:
    def get_transaction_from_bd(self, id_block):
        print('save_changes')
        trans = DatabaseBC.DataBaseBC().get_block_transaction(id_block)

        trans = json.loads(trans)
        trans = json.loads(trans)

        while True:
            id = 1
            id_tr = trans.get(str(id))
            if id_tr is None:
                break
            else:
                id_tr = json.loads(id_tr)
                ok, ck = rsa.newkeys(512)
                _ok = str(ok.e) + ' ' + str(ok.n)
                data = {
                    'fio': 'Oksana',
                    'OKo': '11111',
                    'role': '2'
                }
                trans = {
                    'code': str(1),
                    'ok': '1005',
                    'data': json.dumps(data, sort_keys=True)
                }
                check_trans.proof_trans(trans)




