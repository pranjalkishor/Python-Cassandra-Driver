import random
import os
import sys
import re
import helper
import datetime
from datetime import datetime, timedelta
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra.query import PreparedStatement
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import ExecutionProfile
from cassandra.cluster import EXEC_PROFILE_DEFAULT



config = helper.read_config()
#isAstra = config['general']['isAstra']
#dcname = config['general']['dcname']
ksname = config['general']['ksname']
tblname = config['general']['tblname']

my_user = config['hosts']['username']
my_pwd = config['hosts']['password']
auth_provider = PlainTextAuthProvider(username=my_user, password=my_pwd)

host1 = config['hosts']['host1']
profile = ExecutionProfile(request_timeout=100)
cluster = Cluster([host1], auth_provider=auth_provider, execution_profiles={EXEC_PROFILE_DEFAULT: profile})
#cluster = Cluster(['10.166.64.182'], auth_provider=auth_provider, execution_profiles={EXEC_PROFILE_DEFAULT: profile})
#cluster = Cluster(['10.166.64.182'], execution_profiles={EXEC_PROFILE_DEFAULT: profile})

session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")

#query = session.prepare("insert into zdmks.t2 (id, data) values (?,?)")
#ksname = "zdmks"
#tblname = "t2"

ticket_select = "SELECT * FROM zdmks.t2 WHERE id=?"
ticketsel_prep = session.prepare(ticket_select)
#ticketsel_prep.consistency_level=ConsistencyLevel.QUORUM
print( "Read execution started" )
for i in range (10001,40000):
    bindval = 'id_' + str(i)
    ticksel_bind = ticketsel_prep.bind([bindval])
    selrows = session.execute(ticksel_bind)
    for row in selrows:
         print(row.id, row.data)

print( "Read execution finished" )
