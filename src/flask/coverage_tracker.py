# coverage_tracker.py

branch_coverage = {
    "show_server_banner_1": False,  # if branch for is_running_from_reloader()
    "show_server_banner_2": False,   # if app_import_path is not None:
    "show_server_banner_3": False,   # if debug is not None:
    "make_config_1": False,   # if instance_relative Flase
    "make_config_2": False,   # if instance_not_relative True
    "get_send_file_max_age_1": False,
    "get_send_file_max_age_2": False,
    "get_send_file_max_age_3": False,
    "dispatch_request_1": False,
    "dispatch_request_2": False,
    "dispatch_request_3": False,
    "create_url_adapter_1": False,  # if request is not None
    "create_url_adapter_2": False,  # if not self.subdomain_matching
    "create_url_adapter_3": False,  # if self.subdomain_matching
    "create_url_adapter_4": False,  # if self.config["SERVER_NAME"] is not None
    "create_url_adapter_5": False,   # else case (return None)
    "pop_1": False,
    "pop_2": False,
    "pop_3": False,
    "pop_4": False,
    "pop_5": False,
}

def track_coverage(branch_name):
    global branch_coverage
    branch_coverage[branch_name] = True