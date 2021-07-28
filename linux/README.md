# note-commands

# Check IP of CloudShell (?)	
curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//'
curl ifconfig.co

# Curl for connection check
curl -v *   https://internal-1-east4.carbon-predev.gcp.lowes.com/probe/hello
Trying 10.148.4.3:443...                                                                    

nslookup or dig (dig will give more information )