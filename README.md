IRCyborg
========

a simple IRC bot written in python for the lulz. The bot is written using an [irc library](http://irclib.bitlbee.org/) by Maurits Dijkstra.

Setup is simple, just create __settings.py__ and fill in the following variables:

```python
# Connection details
NICK = ''
IDENT = ''
SERVER = ('irc.server.com', port)
REALNAME = ''
CHANNEL = ''

# Google API details
GAPIKEY = ''
GCUSTOMSEARCHID = ''

# Wunderground.com API details
WAPIKEY = 'b73331af55fc8f37'
```
And you're good to go!
