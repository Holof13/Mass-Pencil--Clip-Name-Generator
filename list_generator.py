import os
import time
import re
import platform
import shutil

## cwd = os.getcwd()
cwd = "."
template = open(f"{cwd}/src/template.scad",'r').read()
out_dir = cwd + "/out/"
stl_dir = out_dir + "stls/"
temp_dir = out_dir + "temp/"
ls_path = cwd + "/list.txt"
example = "EXAMPLE"

## Clear ./out/temp/ of all files
def clear_temp():
    for f in os.listdir(temp_dir):
        os.remove(temp_dir + f)

## Clear ./out/stls of all files
def clear_stls():
    for f in os.listdir(stl_dir):
        os.remove(stl_dir + f)


def parse_list(ls_path) -> list:
    ls = list(open(ls_path, 'r').read().upper().split("\n"))
    parsed = []
    for line in ls:
        match = re.match(r"([a-z]+) ([0-9]+)", line, re.I)
        if match:
            items = match.groups()
            name = items[0]
            k = int(items[1])
            i = 0
            while i < k:
                i += 1
                file_name = f"{name}-{i}"
                parsed.append((f"{name}", f"{file_name}"))
        else:
            parsed.append((f"{line}", f"{line}-0"))
    return parsed

def scad_gen(ls_path, temp_dir, template, example):
    for item in parse_list(ls_path):
        filename = temp_dir + item[0] + ".scad"
        if not os.path.isfile(filename):
            open(filename, "w").write(template.replace(example, item[0]))
        print(f"Generated {filename}")

def stl_gen(ls_path, stl_dir, temp_dir):
    i = 0
    li = parse_list(ls_path)
    for item in li:
        i += 1
        filename = stl_dir + item[1] + ".stl"
        files = os.listdir(stl_dir)

        repeat = False
        for f in files:
            if str(f).startswith(item[0]):
                print(f"[{i}/{len(li)}] Found repeated file: {filename}")
                shutil.copyfile(f"{stl_dir}{f}", filename)
                repeat = True
                break

        if not repeat:
            tin = time.perf_counter()
            if platform.system() == "Windows":
                scad_path = "\"C:\Program Files\OpenSCAD\openscad.exe\""
                cmd = scad_path + f" -q -o {filename} {temp_dir + item[0]}.scad"
            
            if platform.system() == "Linux":
                cmd = f"openscad -o {filename} {stl_dir + item[0] + ".scad"}"
            
            print(f"Generating {filename}...")
            os.system(cmd)
            tan = time.perf_counter()
            print(f"[{i}/{len(li)}] Generated ({tan - tin:0.4f}s)")

def main():
    
    yes = {"yes", "y", "YES", "Y", ""}

    inp = input("Clear temp .scad files? (Y/N)") 
    if inp in yes:
        clear_temp()
    
    inp = input("Clear .stl files? (Y/N)") 
    if inp in yes:
        clear_stls()
    
    inp = input("Generate .scad files? (Y/N)") 
    if inp in yes:
        scad_gen(ls_path, temp_dir, template, example)

    inp = input("Generate .stl files? (Y/N)") 
    if inp in yes:
        tan = time.perf_counter()
        stl_gen(ls_path, stl_dir, temp_dir)
        ton = time.perf_counter()
        print(f"Total time: {ton - tan:0.4f}s")

if __name__ == "__main__":
    main()