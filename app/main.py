from flask import Flask, send_from_directory
from loguru import logger
from utils.log import Log, FlaskInterceptHandler
from handler.routes import main as main_blueprint

import os

#log setup
Log.setup_default()

app = Flask(__name__,static_folder='frontend/dist')
app.register_blueprint(main_blueprint)
FlaskInterceptHandler.setup_default()

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        logger.debug(f"app.static_folder={app.static_folder}, path={path}")
        return send_from_directory(app.static_folder, path)
    else:
        logger.debug(f"app.static_folder={app.static_folder}, path=index.html")
        return send_from_directory(app.static_folder, "index.html")
    

@logger.catch
def main():
    """Main."""
    logger.info("")

    # logger.info(f"log_level={settings.log_level}")
    # logger.info(f"environment={settings.env_for_dynaconf}")

    # Flask
    app.run(host="0.0.0.0",port=5000)

if __name__ == "__main__":
    """__main__

    Run when executed as a script.
    """
    logger.info("")

    try:
        main()

    except Exception as e:
        logger.error(f"Exited due to exception: {e}")
        raise e  # Get traceback