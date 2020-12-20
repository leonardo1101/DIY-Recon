import subprocess
import sys

class ASNTool:
	def __init__(self, name, path, verbose, cmd_org, cmd_domain,
				 output_files, output_path):
		self.name = name
		self.path = path
		self.verbose = verbose
		self.cmd_org = cmd_org.split()
		self.cmd_domain = cmd_domain.split()
		self.output_files = output_files
		self.output_path = output_path

	def __run_cmd(self, cmd):
		if '|' in cmd:
			process1 = subprocess.Popen(cmd[:cmd.index('|')],
								    	stdout=subprocess.PIPE)
			process2 = subprocess.Popen(cmd[cmd.index('|') + 1:],
									    stdin=process1.stdout,
									    stdout=subprocess.PIPE)
			process1.wait()
			process2.wait()
			if self.verbose:
				for line in process2.stdout:
					sys.stdout.write(line.decode("utf-8"))
		else:
			process = subprocess.Popen(cmd,
								   stdout=subprocess.PIPE)
			process.wait()
			if self.verbose:
				for line in process.stdout:
					sys.stdout.write(line.decode("utf-8"))

	def run_cmd_org(self, organization):
		if not self.cmd_org:
			return ""

		org_index = self.cmd_org.index("$org")
		tool_index = self.cmd_org.index("$tool")
		cmd_org = self.cmd_org.copy()

		cmd_org[org_index] = organization
		cmd_org[tool_index] = self.path
		self.__run_cmd(cmd_org)
		if self.output_files != "":
			return self.output_files
		return self.output_path

	def run_cmd_domain(self, domain):
		if not self.cmd_domain:
			return ""

		domain_index = self.cmd_domain.index("$domain")
		tool_index = self.cmd_domain.index("$tool")
		cmd_domain = self.cmd_domain.copy()

		cmd_domain[domain_index] = domain
		cmd_domain[tool_index] = self.path
		self.__run_cmd(cmd_domain)
		if self.output_files != "":
			return self.output_files
		return self.output_path