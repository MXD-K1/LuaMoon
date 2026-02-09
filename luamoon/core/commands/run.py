from os import system

def run_project(type_, entry_point):
    if type_ == 'project':
        system(f'lua {entry_point}')
    else:
        return  # todo: report error
