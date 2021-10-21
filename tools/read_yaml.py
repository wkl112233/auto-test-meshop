import random

import yaml
from config import BASE_DIR


def read_yaml(filename):
    arr = []
    file_path = BASE_DIR + "/data/" + filename
    with open(file_path, "r", encoding="utf-8")as f:
        for i in yaml.safe_load(f).values():
            arr.append(tuple(i.values()))
        return arr


new_user = []
set_user = []
admin_new_arr = []
admin_set_arr = []
run_str = random.randint(0, 1999)
a = ['tester@meshop.net', 'Tester123456', 'autotest', 'autotest', 'autotest']
new_user.append((['Baby', 'Angel', ''.join(["jinpeng", str(run_str), "@meshop.net"]), '123456',
                  ''.join(["jinpeng", str(run_str), "@meshop.net"])]))
set_user.append(tuple([''.join(["jinpeng", str(run_str), "@meshop.net"]), '123456',
                       ''.join(["jinpeng", str(run_str), "@meshop.net"])]))

a[2::] = list(map(lambda x: x + str(run_str), a[2::]))
admin_new_arr.append(tuple(a))
a.insert(0, a.pop())
admin_set_arr.append(tuple(a[:-1]))
if __name__ == '__main__':
    print(set_user)
