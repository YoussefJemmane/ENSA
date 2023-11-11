import http.server

PORT = 8000
server_address = ("",PORT)

server = http.server.HTTPServer 
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]

print("Server connected on ", PORT)

httpd = server(server_address,handler)
httpd.serve_forever()