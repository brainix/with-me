#------------------------------------------------------------------------------#
#   handlers.py                                                                #
#                                                                              #
#   Copyright (c) 2011, Code A La Mode, original authors.                      #
#                                                                              #
#       This file is part of with-me.                                          #
#                                                                              #
#       with-me is free software; you can redistribute it and/or modify        #
#       it under the terms of the GNU General Public License as published by   #
#       the Free Software Foundation, either version 3 of the License, or      #
#       (at your option) any later version.                                    #
#                                                                              #
#       with-me is distributed in the hope that it will be useful,             #
#       but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#       GNU General Public License for more details.                           #
#                                                                              #
#       You should have received a copy of the GNU General Public License      #
#       along with with-me.  If not, see <http://www.gnu.org/licenses/>.       #
#------------------------------------------------------------------------------#


import logging
import os

from google.appengine.ext.webapp import template

from config import DEBUG, TEMPLATES
import base


_log = logging.getLogger(__name__)


class NotFound(base.WebHandler):
    """Request handler to serve a 404: Not Found error page."""

    def get(self, *args, **kwds):
        """Someone has issued a GET request on a nonexistent URL."""
        return self.serve_error(404)


class Home(base.WebHandler):
    """Request handler to serve the homepage."""

    def get(self):
        """Serve the homepage."""
        path = os.path.join(TEMPLATES, 'home.html')
        debug = DEBUG
        title = ''
        html = template.render(path, locals(), debug=debug)
        self.response.out.write(html)
