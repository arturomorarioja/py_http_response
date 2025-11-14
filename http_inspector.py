import requests


def inspect_url(url: str, body_preview_length: int = 500) -> None:
    """
    Fetches the given URL and prints HTTP response parts to stdout.
    Intended for demonstration purposes.
    """
    print('========================================')
    print(f'Inspecting URL: {url}')
    print('========================================')

    response = requests.get(url)

    # ----- STATUS -----
    print('=== RESPONSE STATUS ===')
    print(f'URL: {response.url}')
    print(f'Status code: {response.status_code}')
    print(f'Reason: {response.reason}')
    print(f'OK: {response.ok}')
    print()

    # ----- HEADERS -----
    print('=== RESPONSE HEADERS ===')
    for name, value in response.headers.items():
        print(f'{name}: {value}')
    print()

    # ----- BODY PREVIEW -----
    print(f'=== RESPONSE BODY (first {body_preview_length} characters) ===')
    text = response.text
    print(text[:body_preview_length])
    print('=== END BODY PREVIEW ===')
    print()