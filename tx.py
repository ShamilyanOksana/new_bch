import rsa
import json
import time
import hashlib
from base64 import b64decode, b64encode
import EncDec
import os

def get_hash(data):
    data = data.encode()
    hash = hashlib.sha256(data).hexdigest()
    return hash

def new_user(password):
    pass_hash = get_hash(password)
    p_k, pr_k = rsa.newkeys(512)
    pub_key = {
        'e': p_k.e,
        'n': p_k.n
    }
    priv_key = {
        'e': pr_k.e,
        'n': pr_k.n,
        'q': pr_k.q,
        'p': pr_k.p,
        'd': pr_k.d
    }
    pub_key = json.dumps(pub_key, sort_keys=True)
    priv_key = json.dumps(priv_key, sort_keys=True)
    hash = get_hash(pub_key)
    keys = {'ok': pub_key, 'ck': priv_key, 'hash': hash, 'pass_hash': pass_hash}
    keys = json.dumps(keys, sort_keys=True)
    # file_name = str(hash) + "_keys.txt"
    # print(file_name)
    f = open('ok-ck.txt', 'w')
    f.write(keys)
    f.close()


def get_pub_key(hash):
    f = open(hash+'.txt', 'r')
    keys = f.readline()
    f.close()
    keys = json.loads(keys)
    pub_key = json.loads(keys.get('ck'))
    pub_key = rsa.PublicKey(n=pub_key.get('n'), e=pub_key.get('e'))
    return pub_key


def get_priv_key(hash):
    f = open(hash+'.txt', 'r')
    keys = f.readline()
    f.close()
    keys = json.loads(keys)
    priv_key = json.loads(keys.get('ck'))
    priv_key = rsa.PrivateKey(n=priv_key.get('n'), e=priv_key.get('e'), d=priv_key.get('d'), p=priv_key.get('p'), q=priv_key.get('q'))
    f.close()
    return priv_key


def create_tx(to, value, pub_key):
    to_sign = str(to) + str(value)
    to_sign = json.dumps(to_sign)
    to_sign = to_sign.encode()
    sign = rsa.sign(to_sign, pub_key, "SHA-256")
    tx = {
        'to': to,
        'value': value,
        'sign': sign
    }
    return tx

def get_prehash(block_number):
    file_name = r'''C:\\Users\\Vyacheslav Salmanov\\PycharmProjects\\ws_m\\chain\\block''' + str(block_number-1) + '.txt'
    f = open(file_name)
    block = f.readline()
    block = json.loads(block)
    return block.get('hash')


def create_genezis_block(tx):
    genesis_block = {
        'number': 0,
        'timestamp': time.time(),
        'tx': tx,
        'pre_hash': '',
        'nonce': '0'
    }
    gen_block = json.dumps(genesis_block)
    hash = get_hash(gen_block)
    genesis_block.update({'hash': hash})
    gen_block = json.dumps(genesis_block).encode()
    sign = rsa.sign(gen_block, get_priv_key('6a55028ea67dd8f39a6f1a51b0cb0c70fcfe3a98e99bc313ac82de1a410a7920_keys.txt'), 'SHA-256')
    sign = b64encode(sign).decode()
    genesis_block.update({'sign': sign})
    genesis_block = json.dumps(genesis_block)
    f = open('C:\\Users\Vyacheslav Salmanov\PycharmProjects\ws_m\chain\\block0.txt', 'w')
    f.write(genesis_block)
    f.close()

def create_block(tx, chain_len):
    block = {
        'number': chain_len,
        'timestamp': time.time(),
        'ok': '{"e": 0, "n": 0}',
        'tx': [{'ck1'}],
        'pre_hash': get_prehash(chain_len),
        'nonce': '000'
    }
    _block = json.dumps(block)
    hash = get_hash(_block)
    block.update({'hash': hash})
    _block = json.dumps(block).encode()
    sign = rsa.sign(_block, get_priv_key('6a55028ea67dd8f39a6f1a51b0cb0c70fcfe3a98e99bc313ac82de1a410a7920_keys.txt'), 'SHA-256')
    sign = b64encode(sign).decode()
    block.update({'sign': sign})
    block = json.dumps(block)
    f = open('C:\\Users\Vyacheslav Salmanov\PycharmProjects\ws_m\chain\\block' + str(chain_len) + '.txt', 'w')
    f.write(block)
    f.close()
'''
def create_test_block(tx, ):
    test_block = {
        'number': len,
        'timestamp': time.time(),
        'ok': get_pub_key('6a55028ea67dd8f39a6f1a51b0cb0c70fcfe3a98e99bc313ac82de1a410a7920_keys.txt'),
        'tx': tx,
        'pre_hash': ),
        'nonce': '000',
        'hash': 'drfgvrs',
        'sign': 'sign'
    }
    print(get_prehash(1))
    test_block = json.dumps(test_block)
    f = open('block1.txt', 'w')
    f.write(test_block)
    f.close()
    #print(test_block)
'''

chain_len = len(os.listdir('C:\\Users\Vyacheslav Salmanov\PycharmProjects\ws_m\chain'))


# new_user()
# get_pub_key('user0_keys.txt')
# get_priv_key('user0_keys.txt')
# create_tx(1, 15, get_priv_key('user0_keys.txt'))


# create_genezis_block('transaction')

# f = open('txpool.txt', 'r')
# tx = f.readline()
# f.close()
# create_block(tx, 4)


#формировние INPUTов
def create_input(block_number):
    file_name = 'C:\\Users\\Vyacheslav Salmanov\\PycharmProjects\\ws_m\\chain\\block' + str(block_number) + '.txt'
    with open(file_name, 'r') as f:
        block = f.readline()
    # block.decode()
    block = json.loads(block)
    tx = block.get('tx')
    #СПИСОК ТРАНЗАКЦИЙ!!
    # for i in tx:
    tx_i = json.loads(tx)
    # user = tx_i.get('to')
    user = 'slava'
    input = {
    'from': tx_i.get('from'),
    'value': tx_i.get('value')
    }
    _input = {
        'value': tx_i.get('value')
    }
    input = json.dumps(input) + '\n'
    _input = json.dumps(_input) + '\n'
    file_name = user + '_inputs.txt'
    _file_name = user + '_useful_inputs.txt'
    with open(file_name, 'a') as f:
        f.write(input)
    with open(_file_name, 'a') as f:
        f.write(_input)

# create_input(2)

def get_money(value):
    inputs = open('slava_useful_inputs.txt')
    count = 0
    money = 0
    for line in inputs:

        if value >= money:
            line = line[:-1]
            line = json.loads(line)
            line = int(line.get('value'))
            money += line
            count += 1
        else:
            break
    if value > money:
        inputs.close()
        return 0
    else:
        inputs.close()
        return count

def delete_used_inputs(count):
    with open('slava_useful_inputs.txt') as inputs:
        useful = []
        for i in range(count,):
            inputs.readline()
        while True:
            a = inputs.readline();
            if a != '':
                useful.append(a)
            else:
                break
    f = open('slava_useful_inputs.txt', 'w').close()
    with open('slava_inputs.txt', 'a') as inputs:
        for i in useful:
            inp = useful[i]
            inputs.write(inp)


# print(get_money(25))
delete_used_inputs(3)

def money_transfer(hash_to, value, hash_from):
    tx = {
    'type': 1,
    'from': hash_from,
    'to': hash_to,
    'value': value
    }
    _tx = json.dumps(tx)
    _tx = json.dumps(tx).encode()
    sign = rsa.sign(_tx, get_priv_key(hash_from), 'SHA-256')
    sign = b64encode(sign).decode()
    tx.update({'sign': sign})
    tx = json.dumps(tx)
    return tx



