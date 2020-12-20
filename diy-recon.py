from asn_enum_manager import *

scope_domains = []

def read_scope_domain(scope_domain_path):
    with open(scope_domain_path, 'r') as scope_domain_file:
        for line in scope_domain_file.readlines():
            scope_domains.append(line.replace("\n", ""))

def main():
    org = input("Organization name: ")
    scope_domain_path = input("File with the scope domain: ")
    read_scope_domain(scope_domain_path)
    print("[*] Start running ASN enumeration.")
    run_asn_enum(org, scope_domains)

if __name__ == '__main__':
    main()