from flask import Blueprint, request, jsonify, redirect
from service.url_service import UrlService
from util.url_validator import UrlValidator

url_blueprint = Blueprint('url', __name__)


@url_blueprint.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    validator = UrlValidator.get_instance()
    is_valid, normalized_url, error = validator.validate_url(original_url)
    if not is_valid:
        return jsonify({'error': error}), 400

    service = UrlService.get_instance()
    short_url = service.shorten(normalized_url)
    return jsonify({'short_url': short_url}), 201


@url_blueprint.route('/<short_url>', methods=['GET'])
def redirect_to_original_url(short_url):
    service = UrlService.get_instance()
    original_url = service.get_original(short_url)
    if not original_url:
        return jsonify({'error': 'URL not found'}), 404
    return redirect(original_url)


@url_blueprint.route('/<short_url>', methods=['DELETE'])
def delete_url(short_url):
    service = UrlService.get_instance()
    if not service.delete(short_url):
        return jsonify({'error': 'URL not found'}), 404
    return jsonify({'message': 'URL deleted successfully'}), 200


@url_blueprint.route('/', methods=['GET'])
def get_all_urls():
    service = UrlService.get_instance()
    return jsonify({'urls': service.get_all()}), 200

