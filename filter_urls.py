# checks whether the API response is a list or a dictionary
def filter_urls_csv(data):
    if isinstance(data, list):
        return [url for url in data if url.endswith(".csv")]
    elif isinstance(data, dict):
        return [value for value in data.values() if isinstance(value, str) and value.endswith(".csv")]
    else:
        return []


def filter_urls_csv_success(data):
    if isinstance(data, list):
        return [url for url in data if "SUCESSO" in url and url.endswith(".csv")]
    elif isinstance(data, dict):
        return [value for value in data.values() if isinstance(value, str) and "SUCESSO" in value.endswith(".csv")]
    else:
        return []
