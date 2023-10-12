from websocket_chat import create_app
from websocket_chat.config import config

app = create_app()

if __name__ == "__main__":
    app.run(
        host=config.host,
        port=config.port,
        debug=config.debug_mode,
    )
