# Initialize an empty dictionary to store URL references with identifiers
defs = {}

# Example URL reference and identifier
id = "example_id"
g = "https://www.example.com"

# Store the URL reference 'g' with the identifier 'id' in the dictionary
defs[id] = g

# Later, you can retrieve the URL reference associated with a specific identifier
if id in defs:
    url_reference = defs[id]
    print(f"The URL reference for {id} is: {url_reference}")
else:
    print(f"No URL reference found for identifier: {id}")
