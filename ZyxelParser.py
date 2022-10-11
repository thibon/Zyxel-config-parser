import csv
import argparse

class ZyxelRule:
    def __init__ (self,number,name, desc, user, schedule,zone_from, zone_to, src_ip, src_port,dest_ip, service,log, action, status):
        self.number = number
        self.name = name
        self.desc = desc
        self.user = user
        self.schedule = schedule
        self.zone_from = zone_from
        self.zone_to = zone_to
        self.src_ip = src_ip
        self.src_port = src_port
        self.dest_ip = dest_ip
        self.service = service
        self.log = log
        self.action = action
        self.status = status

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(self.number,
        self.name,self.desc,self.user,self.schedule,
        self.zone_from,self.zone_to,self.src_ip,
        self.src_port,self.dest_ip,self.service,
        self.log,self.action,self.status)

    def __iter__(self):
        return iter([self.number,
        self.name,self.desc,self.user,self.schedule,
        self.zone_from,self.zone_to,self.src_ip,
        self.src_port,self.dest_ip,self.service,
        self.log,self.action,self.status])

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help="Input configuration file path (e.g: secure-policy.txt)", required=True, type=argparse.FileType('r'))
parser.add_argument('-o', '--output', help="Output configuration file name (will be a csv)", type=argparse.FileType('w'), required=True)
args = parser.parse_args()

zyxelRules = []
for line in args.input.readlines():
    
    multi_line_attribs = line.split(',')
    for attributes in multi_line_attribs:
        attribute = attributes.rstrip().lstrip().split(':')

        if "secure-policy" in attribute[0] : tmp_number = attribute[1]
        if "name" in attribute[0] : tmp_name = attribute[1]
        if "description" in attribute[0]:tmp_desc = attribute[1]
        if "user" in attribute[0]: tmp_user = attribute[1]
        if "schedule" in attribute[0]: tmp_schedule = attribute[1]
        if "from" in attribute[0]: tmp_from = attribute[1]
        if "to" in attribute[0]  : tmp_to = attribute[1]
        if "source IP" in attribute[0]: tmp_src_ip = attribute[1]
        if "source port" in attribute[0]: tmp_src_port = attribute[1]
        if "destination IP" in attribute[0]: tmp_dst_ip = attribute[1]
        if "service" in attribute[0]: tmp_service = attribute[1]
        if "log" in attribute[0] : tmp_log = attribute[1]
        if "action" in attribute[0] : tmp_action = attribute[1]
        if "status" in attribute[0] : 
            tmp_status = attribute[1]
            newZyxelRule = ZyxelRule(tmp_number,tmp_name,tmp_desc,tmp_user, tmp_schedule,tmp_from,tmp_to,tmp_src_ip,tmp_src_port,tmp_dst_ip,tmp_service,tmp_log,tmp_action,tmp_status)
            zyxelRules.append(newZyxelRule)

fieldnames = ['number', 'name', 'description','user','schedule','from','to','source IP','source port','destination IP','service','log','action','status']
writer = csv.writer(args.output)
writer.writerow(fieldnames)
for rule in zyxelRules:
    writer.writerow(list(rule))