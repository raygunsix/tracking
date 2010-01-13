from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261371673.085356
_template_filename='/Users/chris/Documents/Aptana Studio Workspace/tracking/tracking/templates/pageviews/new.mako'
_template_uri='/pageviews/new.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n\n ')
        # SOURCE LINE 6
        __M_writer(escape(c.content_id))
        __M_writer(u' | ')
        __M_writer(escape(c.object_id))
        __M_writer(u' | ')
        __M_writer(escape(c.search_terms))
        __M_writer(u' | ')
        __M_writer(escape(c.referrer))
        __M_writer(u' | ')
        __M_writer(escape(c.user_agent))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'New Pageviews')
        return ''
    finally:
        context.caller_stack._pop_frame()


