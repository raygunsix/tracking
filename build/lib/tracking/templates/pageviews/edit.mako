<%inherit file="/base.mako"/>\

<%def name="header()">Editing ${c.id}</%def>

${h.secure_form(url('save_page', title=c.id))}
  ${h.textarea(name='id', rows=7, cols=40, content=c.id)} <br />
  ${h.submit(value='Save changes', name='commit')}
${h.end_form()}
