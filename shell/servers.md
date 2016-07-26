1. Connect to Postgres - bash `alias` is a nice tool for this
```
psql -h '<server_name>' -U '<user>' -d '<database>'
```

2. Some useful stuff for servers at work:
```
tail -f /var/log/uwsgi/app/application-api.log"
```
Restart sequence:
```
worker-control -r && sudo service uwsgi stop; sudo killall -9 /usr/bin/uwsgi-core; sudo service uwsgi restart"
```
Unit testing:
```
python -m unittest discover -p '*_test.py' -s `pwd`"
```

