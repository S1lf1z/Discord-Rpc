from pypresence import Presence

def connect_rpc(client_id):
    rpc = Presence(client_id)
    rpc.connect()
    return rpc
