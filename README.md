# nginx-templates
This is a Python program to create Nginx templates with a few edits.

## Usage
1. Clone this repo in a place as will.
2. Usage is like this:
```bash
nginx-gen [-h] -t TYPE [--server-name SERVER]
                 [--nodes NODES [NODES ...]] [--sslcert SSLCERT]
                 [--sslkey SSLKEY] [--root ROOT]
```
3. Available types are:
- Load Balancer: LB
- Simple server without SSL: SRVNOSSL
- Simple server with SSL: SRVSSL

4. To use this program globally, just make a soft link in /usr/bin/ to the executable:
ln -s /path/to/executable /usr/bin/nginx-gen

## To be done
- Packaging!
- Maybe I'll try to integrate with Let's Encrypt certbot, idk
