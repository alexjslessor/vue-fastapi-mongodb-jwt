import requests
from pprint import pprint


class DeroBase(object):
    headers = {'Connection': 'close'}

class DeroDaemon(DeroBase):

    _get_info = 'get_info'
    _get_height = 'getheight'
    _get_block_count = 'getblockcount'
    _query_key = 'query_key'
    _get_transactions = 'get_transactions'

    def __init__(self, rpc_url='http://localhost:20209/json_rpc'):
        self.rpc_url = rpc_url

    def _post_request(self, payload):
        r = requests.post(self.rpc_url,
                          json={'jsonrpc': '2.0', 'id': '1', 'method': payload}, 
                          headers=self.headers)

        if r.status_code == requests.codes.ok:
           d = r.json()
           print(d)
           return d
        else:
            return f'No Data: {r}'

    def _get_request(self, payload):
        r = requests.get(self.rpc_url,
                          json={'jsonrpc': '2.0', 'id': '1', 'method': payload}, 
                          headers=self.headers)

        if r.status_code == requests.codes.ok:
           d = r.json()
           print(d)
           return d
        else:
            return f'No Data: {r}'


    def get_info(self):
        return self._post_request(self._get_info)

    def get_block_count(self):
        return self._post_request(self._get_block_count)

    # def get_transactions(self):
        # return self._get_request(self._get_transactions)

    # def get_height(self):
        # return self._get_request(self._get_height)


class DeroWallet(DeroBase):
    _get_address = 'getaddress'
    _get_balance = 'getbalance'
    _get_height = 'getheight'

    _transfer = 'transfer'
    
    _make_integrated_addr = 'make_integrated_address'
    _split_integrated_addr = 'split_integrated_address'

    _get_transfer_by_txid = 'get_transfer_by_txid'
    _get_transfers = 'get_transfers'

    def __init__(self, rpc_url='http://localhost:20206/json_rpc'):
        self.rpc_url = rpc_url

    def _post_request(self, payload):
        r = requests.post(self.rpc_url,
                          json={'jsonrpc': '2.0', 'id': '1', 'method': payload}, 
                          headers=self.headers)
        return r.json()

    def get_address(self):
        return self._post_request(self._get_address)

    def get_balance(self):
        return self._post_request(self._get_balance)

    def get_height(self):
        return self._get_request(self._get_height)

    def post_transfer(self):
        pass

# d = DeroDaemon()
# d.get_info()
# d.get_block_count()
w = DeroWallet()
w.get_address()



# construct payload for HTTP request
#payload = {'jsonrpc': '2.0', 'id': '1', 'method': 'getblockcount'}
# payload = {'jsonrpc': '2.0', 'id': '1', 'method': 'get_info'}
# works
# r = requests.post('http://127.0.0.1:20209/json_rpc',
                #   json=payload, headers={'Connection': 'close'})
# works
#r = requests.post('http://localhost:20209/json_rpc', json=payload, headers={'Connection': 'close'})
# works
#r = requests.post('http://0.0.0.0:20209/json_rpc', json=payload, headers={'Connection': 'close'})

#r = requests.post('http://127.0.0.1:20206/json_rpc', json=payload, headers={'Connection': 'close'})

# print(r.json())

# if r.status_code == requests.codes.ok:
#    d = r.json()['result']
#    pprint(d)
