import time

def update_rpc(rpc):
    start_time = int(time.time())
    rpc.update(
        details="/deface",
        state=".....",
        large_image="/deface",
        large_text="Agente en operación",
        small_image="https://cdn.nekotina.com/guilds/1314797349717016576/96473c3d-7cfd-4568-bdc3-e786d7ff6e9e.gif",
        small_text="Conectado",
        start=start_time,
        buttons=[
            {"label": "github", "url": "https://github.com/S1lf1z"},
            {"label": "InfernumSquad", "url": "https://discord.gg/deface"}
        ]
    )
