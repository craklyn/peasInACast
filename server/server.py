import time
import BaseHTTPServer
import makePodcastPage as mpp

HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8080 # Maybe set this to 9000.

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write(mpp.make_podcast_page(s.path[1:]))  
        # If someone went to "http://something.somewhere.net/foo/bar/", then s.path equals "/foo/bar/".
        s.wfile.write("<hr><h2>Debug information:</h2><p>You accessed path: %s</p>" % s.path)
        s.wfile.write("""<p>If you are unsure what to do, try (tbd...) 
        <a href="localhost:8080/T.B.D.">localhost:8080/T.B.D.</a></p>
        or
        WHO KNOWS??? Something else??</p>
        """)
        s.wfile.write("</body></html>")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
