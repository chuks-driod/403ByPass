#!/in/evn python

import byPass403


target_url = "http://prestmit.com/blog/.htpasswd"
# target_url = "http://prestmit.com/blog/"
byPass = byPass403.Bypass(target_url)
# byPass.method_changer(target_url)
# byPass.byPass403()
# byPass.ip_ping()
byPass.host_header()