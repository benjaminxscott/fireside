apt-get -qqy update
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip
pip install bleach
pip install oauth2client
pip install requests
pip install httplib2
su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb fireside'
su vagrant -c 'psql fireside -f /vagrant/tournament.sql'
