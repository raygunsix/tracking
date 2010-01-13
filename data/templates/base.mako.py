from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1260943970.9355481
_template_filename='/Users/chris/Documents/Aptana Studio Workspace/tracking/tracking/templates/base.mako'
_template_uri='/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n<html>\n  <head>\n    <title>Tracking</title>\n    ')
        # SOURCE LINE 6
        __M_writer(escape(h.stylesheet_link('/screen.css')))
        __M_writer(u'\n  </head>\n\n  <body>\n\n    <div class="content">\n\n      <h1 class="main">')
        # SOURCE LINE 13
        __M_writer(escape(self.header()))
        __M_writer(u'</h1>\n\n      ')
        # SOURCE LINE 15
        __M_writer(escape(next.body()))
        __M_writer(u'')
        # SOURCE LINE 16
        __M_writer(u'\n      <p class="footer"></p>\n\n    </div>\n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


