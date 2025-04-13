from config import load_config
from rpc_connect import connect_rpc
from rpc_update import update_rpc
from rpc_loop import keep_alive_loop

def main():
    config = load_config()
    rpc = connect_rpc(config["client_id"])
    update_rpc(rpc)
    keep_alive_loop(rpc)

if __name__ == "__main__":
    main()
