from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from controller.url_controller import url_blueprint


def create_app():
    app = Flask(__name__)

    cfg = Config.get_instance()
    CORS(app, origins=cfg.CORS_ORIGINS)

    app.register_blueprint(url_blueprint, url_prefix='/api/url')

    return app


app = create_app()

@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True)
