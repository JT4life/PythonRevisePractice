
def safe_to_surf(fear_thresholds, conditions):
    """Given a dictionary of surfer fear_thresholds, check a list of conditions
    to determine if the surfer would be willing to surf.
    `fear_thresholds` is a dict that maps fear names to probability thresholds.
    `conditions` is a list of condition dicts.  Each condition is a dict with
    a string "name" and a "chance" integer from 0-100

    A surfer is willing to surf as long as none of the conditions' chances
    crosses the corresponding fear's threshold. If a surfer doesn't have a
    defined fear threshold for a condition that means they are not deterred
    by that condition.

    For example, given these params, the function should return False:

    fear_thresholds = {'lightning': 40,'rain': 40}
    conditions = [
        {'name': 'lightning', 'chance': '75'},
        {'name': 'rain', 'chance': 65},
        {'name': 'sharks', 'chance': 1}
    ]

    :param fear_thresholds:  A dict that maps fear names to fear thresholds.
    :param conditions:  A list of "condition" dicts, each with a "name" and a "chance".
    :return: A boolean, True if the surfer feels like it's safe to surf, False if not.
    """

    if fear_thresholds == {} or fear_thresholds == None:
        return True
    for condition in conditions:
        for key, value in fear_thresholds.items():
            if condition['name'] == key:
                if value <= int(condition['chance']):
                    return False
    else:
        return True


# fear_thresholds = {'lightning': 40,'rain': 40}
fear_thresholds = {"sharks": 10, "rain": 50}
# fear_thresholds = {}
conditions = [
    {"name": "sharks", "chance": 10},
    {"name": "rain", "chance": 50},
    ]
a = safe_to_surf(fear_thresholds, conditions)
print(a)

