from settings import NICK, IDENT, SERVER, REALNAME, CHANNEL
from googleSearch import googleSearch
from geoLocate import geoLocate
from imdb import imdbSearch
import irc

# Event listeners
def handle_state(newstate):
    if newstate == 4:
        conn.send_string('JOIN {0}'.format(CHANNEL))

def handle_raw(line):
    print line

def handle_parsed(prefix, command, params):
    if command=='PRIVMSG':
        if(params[0] == CHANNEL
            and params[1].startswith('!g')
            and not params[1].startswith('!geo')):

            searchTerm = params[1][3:]
            conn.send_string(
                'PRIVMSG {0} :'.format(CHANNEL) + googleSearch(searchTerm)
            )

        if params[0] == CHANNEL and params[1].startswith('!geo'):

            searchTerm = params[1][5:]
            conn.send_string(
                'PRIVMSG {0} :'.format(CHANNEL) + geoLocate(searchTerm)
            )

        if params[0] == CHANNEL and params[1].startswith('!imdb'):

            searchTerm = params[1][6:]
            conn.send_string(
                'PRIVMSG {0} :'.format(CHANNEL) + imdbSearch(searchTerm)
            )


# Connection details
irc = irc.IRC_Object()
conn = irc.new_connection()

conn.nick = NICK
conn.ident = IDENT
conn.server = SERVER
conn.realname = REALNAME

# The event listeners
conn.events['state'].add_listener(handle_state)
conn.events['raw'].add_listener(handle_raw)
conn.events['parsed'].add_listener(handle_parsed)

while 1:
    irc.main_loop()
