import sys

# https://stackoverflow.com/a/21049038/9884253
# modifie to take  less screen space


def dump(obj, nested_level=0):
    spacing = '   '
    if type(obj) == dict:
        print('%s{' % ((nested_level) * spacing))
        for k, v in obj.items():
            print('%s%s: %s' %
                  ((nested_level + 1) * spacing, k, v))
        print('%s}' % (nested_level * spacing))
    elif type(obj) == list:
        print('%s[' % ((nested_level) * spacing), end='', flush=True)
        for v in obj:
            print('%s%s,' % (' ', v), end='', flush=True)
        print(' ]',  flush=True)
    else:
        print('%s%s' % (nested_level * spacing, obj))
