import json
import rsa
from EncDec import enc, dec
import RSASign
import rsa
import check_trans
import save_changes
import Network
import os


class BlockChain:
    net = Network.Network()
    def get_package(self, package):
        '''
        Исходя из типа пакета, который пришел из сети, определяем, что с ним делать дальше
        :param package:
        :return:
        '''
        # package = dec(package)
        if package.get('type') == 'tx':
            package.pop('type')
            self.proc_transaction(package)
        elif package.get('type') == 'block':
            package.pop('type')
            self.proc_block(package)
        elif package.get('type') == 'synchronize':
            package.pop('type')
            self.synchronize(package)
        elif package.get('type') == 'chain':
            package.pop('type')
            self.chain(package)

    def proc_transaction(self, trans):
        '''
        проверка подписи транзакции
        '''
        hash = trans.get('from')
        ok = RSASign.RSASign().find_ok(hash)
        try:
            verif = RSASign.RSASign().verif_sign_trans(trans, ok)
        except Exception:
            print('Verification failed')
            verif = False
        else:
            if verif:
                with open('tx_buffer.txt', 'a') as buffer:
                    buffer.write(json.dumps(trans, sort_keys=True)+'\n')
        return verif

    def proc_block_transaction(self, trans):
        for i in range(len(trans)):
            current_tx = json.loads(trans[i])
            hash = current_tx.get('from')
            ok = RSASign.RSASign().find_ok(hash)
            try:
                verif = RSASign.RSASign().verif_sign_trans(current_tx, ok)
            except Exception:
                print('Verification failed')
                return False
        return True

    def proc_block(self, block):
        miner_hash = block.get('miner_hash')
        miner_ok = RSASign.RSASign().find_ok(miner_hash)

        try:
            verif_block, block = RSASign.RSASign().verif_sign_block(block, miner_ok)
            print(' Verification BLOCK OK')
        except Exception:
            print(' Verification BLOCK failed')
            return 0
        else:
            trans = block.get('tx')
            if self.proc_block_transaction(trans):
                chain_len = len(os.listdir('C:\\Users\\USER\\PycharmProjects\\Blockchain-master\\chain'))
                with open('C:\\Users\\USER\\PycharmProjects\\Blockchain-master\\chain\\block'+str(chain_len+1)+'.txt', 'w') as block_file:
                    block_file.write(json.dumps(block, sort_keys=True))

    def synchronize(self, pack):
        id = int(pack.get('chain'))
        ip = pack.get('ip')
        my_len = len(os.listdir('C:\\Users\\USER\\PycharmProjects\\Blockchain-master\\chain'))
        if my_len > id:
            for i in range(id+1, my_len+1):
                with open('C:\\Users\\USER\\PycharmProjects\\Blockchain-master\\chain\\block'+str(i)+'.txt', 'r') as block:
                    row = block.readline()
                    row = json.loads(row)
                    row.update({'type': 'block'})
                    row = json.dumps(row, sort_keys=True)
                    self.net.send_to_user(ip, row)

    def chain(self, pack):
        ch = enc(pack)
        print(ch)
