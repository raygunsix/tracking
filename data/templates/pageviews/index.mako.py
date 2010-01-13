from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1260944194.6815341
_template_filename='/Users/chris/Documents/Aptana Studio Workspace/tracking/tracking/templates/pageviews/index.mako'
_template_uri='/pageviews/index.mako'
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
        __M_writer(u'\n\n<ul id="titles">\n\n')
        # SOURCE LINE 7
        for pv in c.pvs:
            # SOURCE LINE 8
            __M_writer(u'\n  <li>\n        ')
            # SOURCE LINE 10
            __M_writer(escape(pv.id))
            __M_writer(u' | ')
            __M_writer(escape(pv.content_id))
            __M_writer(u' | ')
            __M_writer(escape(pv.object_id))
            __M_writer(u' | ')
            __M_writer(escape(pv.search_terms))
            __M_writer(u' | ')
            __M_writer(escape(pv.referrer))
            __M_writer(u' | ')
            __M_writer(escape(pv.user_agent))
            __M_writer(u' | ')
            __M_writer(escape(pv.create_date))
            __M_writer(u'\n  </li>\n\n')
        # SOURCE LINE 14
        __M_writer(u'\n</ul>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Pageviews')
        return ''
    finally:
        context.caller_stack._pop_frame()


