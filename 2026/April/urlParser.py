# URL Query Parser
# Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.

# The query string begins after the "?",
# each parameter is separated by "&",
# each key/value pair is separated by "="
# For example, given "https://example.com/search?name=Alice&age=30", return:

# {
#   "name": "Alice",
#   "age": "30"
# }
# All values should be returned as strings.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-29


def url_parser(url):
    query_string = url.split('?')[1]  # Get the part after '?'
    parameters = query_string.split('&')  # Split into key-value pairs
    result = {}
    
    for param in parameters:
        key, value = param.split('=')  # Split each pair into key and value
        result[key] = value  # Store in the result dictionary
    
    return result