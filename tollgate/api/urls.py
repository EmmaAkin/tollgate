"""tollgate api urls
Copyright 2008-2010 Michael Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.conf.urls.defaults import *
from django.conf import settings
#from tollgate.frontend.forms import *
from tollgate.api.resources import NetworkHostResource


urlpatterns = patterns('tollgate.api.views',
#	(r'^xmlrpc/$', 'xmlrpc_handler'),
#	(r'^httpget/(?P<output_format>\w+)/(?P<method>[\w\d_]+)/$', 'httpget_handler'),
	
)
