import socketserver
import json

import robot as robosapien

class UDPHandlerForVRController(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = json.loads (self.request [0])
        socket = self.request [1]
        print("{} wrote:".format (self.client_address [0]))
        print(data)
		if data ['type'] == 'action':
			robosapien.do (data ['action'])
	        socket.sendto("The action " + data ['action'] + ' is sent to the robot.', self.client_address)
		elif data ['type'] == 'error':
	        socket.sendto("Error " + data ['error'] + ' is accepted.', self.client_address)
			

if __name__ == "__main__":
	robosapien.init ()
    HOST, PORT = "localhost", 9999
    server = socketserver.UDPServer((HOST, PORT), UDPHandlerForVRController)
    server.serve_forever()
