<%inherit file="/base.mako"/>\

<%def name="header()">New Pageviews</%def>


 ${c.content_id} | ${c.object_id} | ${c.search_terms} | ${c.referrer} | ${c.user_agent}
