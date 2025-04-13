import time

def keep_alive_loop(rpc):
    print("RPC ACTIVO")
    print("Presiona Ctrl+C para cerrar el RPC o Suicidate")
    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("Cerrando RPC...")
        rpc.clear()
        rpc.close()
