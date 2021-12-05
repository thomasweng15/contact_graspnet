# Iterate over valid meshes/ and remove any meshes from splits that do not exist. 
import os
import json

meshes_path = '/checkpoint/thomasweng/acronym/meshes'
splits_path = '/checkpoint/thomasweng/acronym/splits_copy'

mesh_categories = os.listdir(meshes_path)
splits_jsons = os.listdir(splits_path)

count = 0
for json_name in splits_jsons:
    split = json.load(open(f"{splits_path}/{json_name}"))
    for key in split.keys():
        print("Before")
        print(split[key])
        for item in split[key]:

            # if item.replace('.json', '.h5') in mesh_categories:
            object_name = item.split('_')[0]
            mesh_obj = item.split('_')[1] + '.obj'
            if mesh_obj not in os.listdir(f"{meshes_path}/{object_name}"):
                split[key].remove(item)
                print(f"Removing {item}")
                count += 1
        
        print("After")
        print(split[key])

        # import IPython; IPython.embed()
    
    # break
print(f"removed: {count}")