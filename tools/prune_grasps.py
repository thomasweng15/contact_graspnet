# Creates a new directory with pruned grasps
import os
import sys
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--grasp_dir', help="Path of acronym grasps", default='/checkpoint/thomasweng/acronym/grasps')
parser.add_argument('--mesh_dir', help="Meshes path", default='/checkpoint/thomasweng/acronym/meshes')
parser.add_argument('--pruned_dir', help="Pruned grasps dir", default='/checkpoint/thomasweng/acronym/grasps_pruned')
args = parser.parse_args()

if os.path.exists(args.pruned_dir):
    if args.overwrite:
        print(f"Overwriting {args.pruned_dir}")
        shutil.rmtree(args.pruned_dir)
    else:
        print("Error: pruned dir exists")
        sys.exit(1)
os.mkdir(args.pruned_dir)

count = 0
for fname in os.listdir(args.grasp_dir):
    name, obj, scale = fname.replace('.h5', '').split('_')
    # print(f"{name} {obj} {scale}")
    # import IPython; IPython.embed()
    if not os.path.exists(f'{args.mesh_dir}/{name}/{obj}.obj'):
        continue
    os.system(f'cp {args.grasp_dir}/{fname} {args.pruned_dir}/{fname}')
    count += 1
print(count)