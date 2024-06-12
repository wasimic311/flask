# coverage_tracker.py

branch_coverage = {
    "show_server_banner_1": False,  # if branch for is_running_from_reloader()
    "show_server_banner_2": False,   # if app_import_path is not None:
    "show_server_banner_3": False,   # if debug is not None:
    "make_config_1": False,   # if instance_relative Flase
    "make_config_2": False   # if instance_not_relative True
}

def track_coverage(branch_name):
    global branch_coverage
    branch_coverage[branch_name] = True