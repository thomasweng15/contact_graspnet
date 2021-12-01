import os
import sys
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--grasp_dir', help="Path of acronym grasps", default='/checkpoint/thomasweng/acronym/grasps')
parser.add_argument('--models_dir', help="Input obj models path", default='/checkpoint/thomasweng/acronym/models')
parser.add_argument('--mesh_dir', help="Output mesh path", default='/checkpoint/thomasweng/acronym/meshes')
parser.add_argument('--overwrite', help="Overwrite mesh dir", action='store_true')
args = parser.parse_args()

if os.path.exists(args.mesh_dir):
    if args.overwrite:
        print(f"Overwriting {args.mesh_dir}")
        shutil.rmtree(args.mesh_dir)
        os.mkdir(args.mesh_dir)
    else:
        print("Error: mesh dir exists")
        sys.exit(1)

for fname in os.listdir(args.grasp_dir):
    name, obj, scale = fname.replace('.h5', '').split('_')
    print(f"{name} {obj}")
    if not os.path.exists(f"{args.mesh_dir}/{name}"):
        os.mkdir(f'{args.mesh_dir}/{name}')
    if os.path.exists(f'{args.mesh_dir}/{name}/{obj}.obj'):
        continue
    os.system(f'manifold {args.models_dir}/{obj}.obj {args.models_dir}/{obj}.watertight.obj -s')
    os.system(f'simplify -i {args.models_dir}/{obj}.watertight.obj -o {args.mesh_dir}/{name}/{obj}.obj -m -r 0.02')