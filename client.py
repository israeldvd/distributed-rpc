import xmlrpc.client

# Create an object to represent our server.
server_url = 'http://xmlrpc-c.sourceforge.net/api/sample.php'
server = xmlrpc.client.ServerProxy(server_url)

# Call the server and get our result.
result = server.sample.sumAndDifference(5, 3)
print("Sum:", result['sum'])
print("Difference:", result['difference'])
