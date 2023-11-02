import chromadb

api_client = chromadb.Client()
print(api_client.heartbeat())

api_httpclient = chromadb.HttpClient(host="localhost", port="8000")

print(api_httpclient.heartbeat())
