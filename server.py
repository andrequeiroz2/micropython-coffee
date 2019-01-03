import machine

import file
import wifi

try:
    import usocket as socket
except:
    import socket

wifi_networks = wifi.get_networks()


def web_page():
    wifi_select = "<select name='name'>"
    for i in wifi_networks:
        wifi_select = wifi_select + "<option>" + i[0].decode('utf-8') + "</option>"

    wifi_select = wifi_select + "</select>"

    html = """<html><head> <title>Mqtt Coffee connection</title><link rel="icon" href="data:,">
    <style>.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head>
  <body>
  <center>
  <form action="/">
  <p>Network: """ + wifi_select + """</p>
  <p>Password: <input type="text" name="password"/></p>
  <p><input type="hidden" name="action" value="save"/></p>
  <p><input type="submit" class="button button2" value="Save"></p>
  </form>
  </center>
  </body></html>"""
    return html


def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request.decode("utf-8"))
        print('Content = %s' % request)
        wifi_save = request.find('action=save')
        if wifi_save > -1:
            url = request.split('HTTP/1.1')[0].replace("GET ", "")
            params = qs_parse(url)
            name = params["/?name"]
            password = params["password"]
            file.save_wifi(name, password)
            machine.reset()

        response = web_page()
        conn.send(response)
        conn.close()


def qs_parse(qs):
    parameters = {}
    ampersand_split = qs.split("&")
    for element in ampersand_split:
        equalSplit = element.split("=")
        parameters[equalSplit[0]] = equalSplit[1]
    return parameters
