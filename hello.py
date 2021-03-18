import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import psycopg2

class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = f'Grettings from {os.uname()[1]}.'
        print(message)
        dbname = os.environ['POSTGRES_DB']
        dbuser = os.environ['POSTGRES_USER']
        dbpass = os.environ['POSTGRES_PASSWORD']
        conn_str = f"host='db' dbname='{dbname}' user='{dbuser}' password='{dbpass}'"
        with psycopg2.connect(conn_str) as connection:
            cursor = connection.cursor()
            cursor.execute('insert into greetings (text) values (%s);', (message,))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str.encode(message))



print('Serving hello server on 0.0.0.0:8000')
httpd = HTTPServer(('0.0.0.0', 8000), HttpHandler)
httpd.serve_forever()


