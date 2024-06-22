branch_coverage = {
    "create_url_adapter_1": False,  # if request is not None
    "create_url_adapter_2": False,  # if not self.subdomain_matching
    "create_url_adapter_3": False,  # if self.subdomain_matching
    "create_url_adapter_4": False,  # if self.config["SERVER_NAME"] is not None
    "create_url_adapter_5": False   # else case (return None)
}

def track_coverage(branch_name):
    global branch_coverage
    branch_coverage[branch_name] = True