from asn_enum_parser import *
from asn_enum_tool import *
import os
import re

ipv4 = []
ipv6 = []

def get_ipv4(file_path):
	with open(file_path, 'r') as ip_file:
		for ip in ip_file.readlines():
			if re.match("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}/\d{1,2}", ip) != None \
			   and ip not in ipv4:
				ipv4.append(ip.replace("\n", ""))

def get_ipv6(file_path):
	with open(file_path, 'r') as ip_file:
		for ip in ip_file.readlines():
			if re.match("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}/\d{1,2}", ip) == None \
			   and ip not in ipv6:
				ipv6.append(ip.replace("\n", ""))

def write_asn_enum_result(result_file):
	asn_enum_result = {}
	asn_enum_result["ipv4"] = ipv4
	asn_enum_result["ipv6"] = ipv6
	with open(result_file, 'w') as enum_file:
		json.dump(asn_enum_result, enum_file)

def process_files(outputs):
	for output in outputs:
		if os.path.exists(output):
			if os.path.isdir(output):
				files = os.listdir(output)
				for file in files:
					if os.path.isfile(output + file):
						get_ipv4(output + file)
						get_ipv6(output + file)
						os.remove(output + file)
			else:
				get_ipv4(output)
				get_ipv6(output)
				os.remove(output)

def run_asn_enum(org, domains):
	tools = get_asn_tools()
	result_file = get_asn_enum_output()
	for tool in tools:
		print("[ASN enumeration] Start running {0} tool.".format(tool.name))
		outputs = tool.run_cmd_org(org)
		process_files(outputs)
		for domain in domains:
			outputs = tool.run_cmd_domain(domain)
			process_files(outputs)
	write_asn_enum_result(result_file)

