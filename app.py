from flask import Flask, request, jsonify
from http_inspector import inspect_url
import requests

app = Flask(__name__)


@app.route('/inspect', methods=['GET'])
def inspect():
    """
    Endpoint that triggers inspection of an arbitrary URL.

    Example:
        GET /inspect?url=https://www.ek.dk/
    """
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'Missing "url" query parameter'}), 400

    try:
        inspect_url(url)
    except requests.RequestException as exc:
        # Error details are printed to stdout and a generic error is returned.
        print('Error while fetching URL:')
        print(f'  URL: {url}')
        print(f'  Exception: {exc}')
        return jsonify({'error': 'Error while fetching URL'}), 502

    # No HTML, just a small JSON acknowledgement.
    return jsonify({'message': 'Inspection complete. Check server stdout.'})
    

if __name__ == '__main__':
    # Simple development server; for production use a proper WSGI/ASGI server.
    app.run(host='0.0.0.0', port=5000, debug=True)
