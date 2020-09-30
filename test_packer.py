from py3dbp import Packer, Bin, Item
from plotter import plot_multiple_package
import json

packer = Packer()

packer.add_bin(Bin('small-envelope', 11.5, 6.125, 0.25, 10))
packer.add_bin(Bin('large-envelope', 15.0, 12.0, 0.75, 15))
packer.add_bin(Bin('small-box', 8.625, 5.375, 1.625, 70.0))
packer.add_bin(Bin('medium-box', 11.0, 8.5, 5.5, 70.0))
packer.add_bin(Bin('medium-2-box', 13.625, 11.875, 3.375, 70.0))
packer.add_bin(Bin('large-box', 12.0, 12.0, 5.5, 70.0))
packer.add_bin(Bin('large-2-box', 23.6875, 11.75, 3.0, 70.0))

packer.add_item(Item('50g [powder 1]', 3.9370, 1.9685, 1.9685, 1))
packer.add_item(Item('50g [powder 2]', 3.9370, 1.9685, 1.9685, 2))
packer.add_item(Item('50g [powder 3]', 3.9370, 1.9685, 1.9685, 3))
packer.add_item(Item('250g [powder 4]', 7.8740, 3.9370, 1.9685, 4))
packer.add_item(Item('250g [powder 5]', 7.8740, 3.9370, 1.9685, 5))
packer.add_item(Item('250g [powder 6]', 7.8740, 3.9370, 1.9685, 6))
packer.add_item(Item('250g [powder 7]', 7.8740, 3.9370, 1.9685, 7))
packer.add_item(Item('250g [powder 8]', 7.8740, 3.9370, 1.9685, 8))
packer.add_item(Item('250g [powder 9]', 7.8740, 3.9370, 1.9685, 9))

packer.pack()
    

# for b in packer.bins:
#     print(":::::::::::", b.string())

#     print("FITTED ITEMS:")
#     for item in b.items:
#         print("====> ", item.string())

#     print("UNFITTED ITEMS:")
#     for item in b.unfitted_items:
#         print("====> ", item.string())

#     print("***************************************************")
#     print("***************************************************")


figure_num = 0
for b in packer.bins:
    print(":::::::::::", b.string())

    result_dict = {}
    result_dict["weight"] = float(b.max_weight)
    result_dict["width"] = float(b.width)
    result_dict["height"] = float(b.height)
    result_dict["length"] = float(b.depth)
    result_dict["volume"] = float(b.width * b.height * b.depth)
    
    result_dict["placement"] = []
    for item in b.items:
        item_dict = {}
        item_dict["name"] = item.name
        item_dict["x"] = float(item.position[0])
        item_dict["y"] = float(item.position[1])
        item_dict["z"] = float(item.position[2])

        w, h, d = item.get_dimension()
        item_dict["width"] = float(w)
        item_dict["height"] = float(h)
        item_dict["length"] = float(d)
        result_dict["placement"].append(item_dict)

        print("====> ", item.string())
        print("Default Dimen", item.width, item.height, item.depth)
        print("GET Dimension", item.get_dimension())
        print("Rotation Type", item.rotation_type)
        print()

    result_json = json.dumps(result_dict)
    print(result_json)
    print("\n\n")

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    
    if len(b.items) > 0:
        plt1 = plot_multiple_package(result_json, 'Packages', figure_num)
        plt1.show()
        figure_num+=1