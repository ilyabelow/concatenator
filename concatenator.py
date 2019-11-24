# Goals:
# 1. Expand local includes in the correct order and only once
# 2. Move stdlib includes to the top and delete duplicats
# 2. Move defines to the top and delete duplicats
# 3. Delete header guardians

# Order:
# 1. stdlib includes and defines
# 2. Headers in the correct order
# 3. Sources right after corresponding header
# 4. int main()

# ONE HEADER CAN HAVE NOT MORE THAT ONE CPP
# CPP MUST HAVE THE SAME NAME AS HPP
# If I were to make more general concatenator, I would have to parse Makefile,
# which is too complicated and I'm lazy

import os.path

main = "main.cpp"
united = "united.cpp"
included_hpp = []
included_stdlib = []
global_defines = []

def expand(filename):
    cur_dir = filename[:filename.rfind('/')+1]
    f = open(filename, 'r')
    concatinated = []
    for line in f:
        splited = line.split()
        # Preprocessor derectives processing
        if len(splited) > 0 and splited[0][0] == '#':
            first = splited[0]
            # Includes processings
            if first == '#include':
                # Local includes processing
                if splited[1][0] == '"':
                    hpp_name = splited[1][1:-1]
                    if hpp_name in included_hpp:
                        continue
                    included_hpp.append(hpp_name)
                    concatinated += expand(cur_dir + hpp_name)
                    continue
                # Stdlib includes processing
                if line not in included_stdlib:
                    included_stdlib.append(line)
            # Defines processing
            if first == '#define' and len(splited) == 3:
                if line not in global_defines:
                    global_defines.append(line)
                continue
            # Header guardian processing
            # (this line is totally useless btw)
            if first == '#endif' or first == '#ifndef' or (first == '#define' and len(splited) == 2):
                continue
        # Ordinary lines processing
        else:
            concatinated.append(line)
    f.close()
    # CPP processing
    # To each .hpp or .h file corresponds one cpp with the same name
    if filename[-3:] == 'hpp' or filename[-1] == 'h':
        cpp_file = filename[:-3] + 'cpp'
        if os.path.exists(cpp_file):
            concatinated += expand(cur_dir + cpp_file)
    return concatinated

done = expand(main)

for line in global_defines:
    done.insert(0, line)
done.insert(0, '\n')
for line in included_stdlib:
    done.insert(0, line)

united_file = open(united, 'w')
united_file.seek(0)
for line in done:
    united_file.write(line)
united_file.truncate()
united_file.close()
