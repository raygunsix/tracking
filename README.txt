======================
Deployment
======================

Deploy the tracking application as follows:

fab <environment> deploy

For example:

fab qa deploy

Available Commands:

fab qa deploy       Deploys to tracking.qa.suite101.com
fab live deploy     Deploys to tracking.suite101.com

fab test            Runs unit tests locally

======================
Manual Installation and Setup
======================

Install ``tracking`` using easy_install::

    easy_install tracking

Make a config file as follows::

    paster make-config tracking config.ini

Tweak the config file as appropriate and then setup the application::

    paster setup-app config.ini

Then you are ready to go.