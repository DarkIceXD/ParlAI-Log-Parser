import re


def parse(log_file_name):
    data = {}
    with open(log_file_name, 'r') as file:
        is_data = False
        positions = []
        for line in file:
            time = line.find('| time')
            if time != -1:
                tokens = line[time + 1:].split()
                for token in tokens:
                    pair = token.strip().split(':')
                    key = pair[0]
                    value = float(re.sub(r'[^\d.]', '', pair[1]))
                    if key not in data:
                        data[key] = [value]
                    else:
                        data[key].append(value)
                is_data = True
            elif is_data:
                if line == '\n':
                    is_data = False
                    continue
                tokens = line.split()
                if len(tokens) <= 0:
                    continue
                if line.find(' ' + tokens[0].strip()) > 2:
                    positions = [{'end': 0}]
                    for token in tokens:
                        needle = token.strip()
                        if needle == '\\':
                            continue
                        positions.append(
                            {'token': needle, 'end': line.rfind(needle) + len(needle)})
                else:
                    task_name = tokens[0].strip()
                    if task_name not in data:
                        data[task_name] = {}
                    positions[0]['end'] = line.find(task_name) + len(task_name)
                    for i in range(1, len(positions)):
                        value_name = positions[i]['token']
                        if value_name not in data[task_name]:
                            data[task_name][value_name] = []
                        try:
                            value = float(
                                line[positions[i - 1]['end']:positions[i]['end']])
                            data[task_name][value_name].append(value)
                        except ValueError:
                            if len(data[task_name][value_name]) > 0:
                                data[task_name][value_name].append(
                                    data[task_name][value_name][-1])
                            else:
                                data[task_name][value_name].append(0)
    return data
