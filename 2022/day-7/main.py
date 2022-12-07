with open('input.txt') as file:
    data = [line for line in file.read().split('\n') if len(line) > 0]

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = []

    def __repr__(self):
        return f'dir {self.name}'

    def add(self, item):
        if isinstance(item, Directory):
            item.parent = self
        self.children.append(item)

    def get_size(self):
        size = 0
        for el in self.children:
            size += el.get_size()
        return size

    def find(self, item_name):
        for child in self.children:
            if child.name == item_name:
                return child
        else:
            print('Item not found:', item_name, 'in', self.name)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.size} {self.name}'

    def get_size(self):
        return self.size

# Build up the tree
tree = Directory('/')
wd = None
cur_line = 0
while cur_line < len(data):
    line = data[cur_line]
    if line[0] == '$':
        # Parse the command
        cmd = line[2:4]
        if cmd == 'cd':
            dir_name = line[5:]
            
            if dir_name == '..':
                wd = wd.parent
            elif dir_name == '/':
                wd = tree
            else:
                wd = wd.find(dir_name)
            cur_line += 1

        elif cmd == 'ls':
            cur_line += 1
            line = data[cur_line]
            while data[cur_line][0] != '$':
                if line[:3] == 'dir':
                    dir_name = line[4:]
                    new_dir = Directory(dir_name)
                    wd.add(new_dir)
                else:
                    line = line.split()
                    size = int(line[0])
                    file_name = line[1]
                    new_file = File(file_name, size)
                    wd.add(new_file)
                
                cur_line += 1
                if cur_line >= len(data):
                    break
                line = data[cur_line]

        else:
            print('Unknown command while parsing:', cmd)

def traverse(d, depth=0):
    s = ' ' * depth
    s += str(d)
    if isinstance(d, Directory):
        for el in d.children:
            s += '\n' + str(traverse(el, depth+1))
    return s

#print(traverse(tree))

# Part 1
# Traverse the tree and calculate the directory sizes
total_size = 0
def calc_size(cur_dir):
    global total_size
    size = cur_dir.get_size()
    if size <= 100000:
        total_size += size

    for obj in cur_dir.children:
        if isinstance(obj, Directory):
            calc_size(obj)

calc_size(tree)

print(f'(Part 1) Size: {total_size}')

# Part 2
total_used = tree.get_size()
total_free = 70000000 - total_used
needed_size = 30000000 - total_free

print(f'  Filesystem has {total_used} of used space. Need to free at least {needed_size} more.')

smallest_size = total_used

def find_smallest(cur_dir):
    global smallest_size
    size = cur_dir.get_size()
    if size < smallest_size and size >= needed_size:
        smallest_size = size

    for obj in cur_dir.children:
        if isinstance(obj, Directory):
            find_smallest(obj)

find_smallest(tree)

print(f'(Part 2) Smallest directory size: {smallest_size}')
