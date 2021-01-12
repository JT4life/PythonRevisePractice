'''
implement group by owner function that
accepts a dict containing the file owner name for each file name
returns a dict containing a list of file names for each owner name in any order
'''
def group_by_owners(files):
    # result = {}
    # for file, owner in files.items():
    #     result[owner] = result.get(owner, []) + [file]
    # return result

    owner_dict = {}
    for key, value in files.items():
        if value in owner_dict:
            owner_dict[value].append(key)
        else:
            owner_dict[value] = [key]
            
    return owner_dict


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))