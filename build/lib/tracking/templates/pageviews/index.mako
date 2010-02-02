<%inherit file="/base.mako"/>\

<%def name="header()">Pageviews</%def>

<ul id="titles">

% for pv in c.pvs:

  <li>
        ${pv.st_id} | ${pv.st_user_agent} | ${pv.st_url} | ${pv.st_spider_date}
  </li>

% endfor

</ul>