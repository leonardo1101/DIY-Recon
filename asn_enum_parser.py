from asn_enum_tool import *
import json

def get_asn_tools():
	asn_tools = []
	with open("config.json") as config_file:
		data = json.load(config_file)
		tools = data["asn_enumeration"]["tools"]
		for tool in tools:
			asn_tool = ASNTool(tool["name"], tool["path"],
							   tool["verbose"], tool["cmd_org"],
							   tool["cmd_domain"], tool["output_files"],
							   tool["output_path"])
			asn_tools.append(asn_tool)
	return asn_tools

def get_asn_enum_output():
	with open("config.json") as config_file:
		data = json.load(config_file)
		return data["asn_enumeration"]["output"]
	return ""

