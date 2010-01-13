<%inherit file="/base.mako"/>\

<%def name="header()">Pageviews</%def>

<ul id="titles">

% for pv in c.pvs:

  <li>
        ${pv.id} | ${pv.content_id} | ${pv.object_id} | ${pv.search_terms} | ${pv.referrer} | ${pv.user_agent} | ${pv.create_date}
  </li>

% endfor

</ul>