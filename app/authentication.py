import ldap3 as ldap
from ldap3 import Connection, Server

def auth(username, password):
    server = Server('ldap1.cape.saao.ac.za:389 ', get_info=ldap.ALL)
    conn = Connection(server,"uid=%s,ou=people,dc=saao" % username,password)
    print(conn.bind())
    if not conn.bind():
        return False
        print('error in bind', conn.result)

    else:
        print('successful',conn.result)
        return True

