from unipath import Path as pp
import subprocess

# Need install mdbtools

BASE_DIR = pp(__file__).parent
BASE_PF = BASE_DIR + "/isrc_db.mdb"
print(BASE_PF)


script = (
    "for TT in $(/usr/bin/mdb-tables " + BASE_PF + "); do  "
    "mdb-export -D '%Y-%m-%d %H:%M:%S' " + BASE_PF + " "
    "$TT > ${TT}.csv; done "
)

subprocess.call(script, shell=True)
