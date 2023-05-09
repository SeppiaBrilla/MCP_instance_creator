from instance import Instance

instance = Instance(3,7,(7,20))

print(f'max_loads = {instance.max_load},\nsizes = {instance.size}')
instance.save_dzn()