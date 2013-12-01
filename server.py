import tornado.ioloop
import tornado.web
from CSHLDAP import CSHLDAP

class IbuttonHandler(tornado.web.RequestHandler):

    def get(self):
        # Do the actual work here
        # Call out to ldap, return a json dict
        # contents: entryUUID, username
   	
	# To move to production, change these initialization values
	# to a user/pass which can search ibuttons     
	ldap = CSHLDAP('user', 'password', app=True)
	# get the ibutton from the arguments
	ibutton = self.get_argument('ibutton')
	entry = ldap.search(ibutton=ibutton)[0]
	response = {
            'username': entry[1]['uid'],
            'entryUUID': entry[1]['entryUUID']
            }
	# return it
        self.write(response)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", IbuttonHandler),
    ])

    application.listen(6969)
    tornado.ioloop.IOLoop.instance().start()
