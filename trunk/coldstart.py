#------------------------------------------------------------------------------#
#   coldstart.py                                                               #
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
"""Initialization code to be run immediately on a cold instance start.

This module is intended to be imported at the very top of main.py, so that this
code gets run on a cold Google App Engine instance start before anything else.
The reason that we need this startup code is to tell App Engine which library
versions we want to use.  We have to do this first, before the rest of our
imports, to ensure that we import the correct library versions.
"""


# Let's get the ball rolling.  First things first: let's configure the logger.
import logging
from config import DEBUG
logging.getLogger().setLevel(logging.DEBUG if DEBUG else logging.INFO)
_log = logging.getLogger(__name__)


# Now that the logger is configured, before we do anything else, before we even
# import anything else, let's tell Google App Engine which library versions we
# want to use.  We have to do this now, before the rest of our imports, to
# ensure that we import the correct library versions.
#
# For more information, see:
#   http://code.google.com/appengine/docs/python/tools/libraries.html
from google.appengine.dist import use_library
from config import LIBRARIES
for library, version in LIBRARIES.items():
    _log.debug('using library %s %s' % (library, version))
    use_library(library, version)
