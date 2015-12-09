#!/usr/bin/python
"""via ssh, get the old password"""
import re
import sys
confFile = '/var/aegir/config/includes/global.inc'
passline = re.compile("\$conf\\['slac_ldap_admin_password'\\]")
newpattern = re.compile("\'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}\'")

def grok (confFile,passline) :
    try:
        for i, line in enumerate(open(confFile)):
            for match in re.finditer(passline, line):
                thismatch = line.strip()
                myline = re.findall(newpattern,thismatch)
                return myline[0].strip('\'')

    except IOError as e:
        print "Unable to find the file you're looking for"
    except RuntimeError:
        print "Error in your syntax"
    except:
        print "Unexpected error:", sys.exec_info()[0]

if __name__ == '__main__':
    grok(confFile, passline)