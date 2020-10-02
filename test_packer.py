from py3dbp import Packer, Bin, Item
from plotter import plot_multiple_package
import json
import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def random_bin():
    name_len = random.randrange(5, 10)
    bin_name = get_random_string(7).upper()
    
    w = round(random.uniform(5000.0, 10000.0), 2)
    h = round(random.uniform(5000.0, 10000.0), 2)
    d = round(random.uniform(5000.0, 10000.0), 2)
    mw = round(random.uniform(50000.0, 100000.0), 2)
    new_bin = Bin(bin_name, w, h, d, mw)
    print(new_bin.string())
    return new_bin


def random_item():
    name_len = random.randrange(3, 6)
    item_name = get_random_string(4)
    
    w = round(random.uniform(1000.0, 2000.0), 2)
    h = round(random.uniform(1000.0, 2000.0), 2)
    d = round(random.uniform(1000.0, 2000.0), 2)
    mw = round(random.uniform(500.0, 1000.0), 2)
    new_item = Item(item_name, w, h, d, mw)
    print(new_item.string())
    return new_item


packer = Packer()

total_bin = random.randrange(1, 3)
for i in range(total_bin):
    packer.add_bin(random_bin())
print()
total_item = random.randrange(20, 60)
for i in range(total_item):
    packer.add_item(random_item())


# packer.add_bin(Bin("The Container", 150, 150, 150, 10000))
# for i in range(27):
#     print(i)
#     packer.add_item(Item("Item"+str(i), 50, 50, 50, 1))


''' Test 1 From example '''
# packer.add_bin(Bin('small-envelope', 11.5, 6.125, 0.25, 10))
# packer.add_bin(Bin('large-envelope', 15.0, 12.0, 0.75, 15))
# packer.add_bin(Bin('small-box', 8.625, 5.375, 1.625, 70.0))
# packer.add_bin(Bin('medium-box', 11.0, 8.5, 5.5, 70.0))
# packer.add_bin(Bin('medium-2-box', 13.625, 11.875, 3.375, 70.0))
# packer.add_bin(Bin('large-box', 12.0, 12.0, 5.5, 70.0))
# packer.add_bin(Bin('large-2-box', 23.6875, 11.75, 3.0, 70.0))
# packer.add_item(Item('50g [powder 1]', 3.9370, 1.9685, 1.9685, 1))
# packer.add_item(Item('50g [powder 2]', 3.9370, 1.9685, 1.9685, 2))
# packer.add_item(Item('50g [powder 3]', 3.9370, 1.9685, 1.9685, 3))
# packer.add_item(Item('250g [powder 4]', 7.8740, 3.9370, 1.9685, 4))
# packer.add_item(Item('250g [powder 5]', 7.8740, 3.9370, 1.9685, 5))
# packer.add_item(Item('250g [powder 6]', 7.8740, 3.9370, 1.9685, 6))
# packer.add_item(Item('250g [powder 7]', 7.8740, 3.9370, 1.9685, 7))
# packer.add_item(Item('250g [powder 8]', 7.8740, 3.9370, 1.9685, 8))
# packer.add_item(Item('250g [powder 9]', 7.8740, 3.9370, 1.9685, 9))


''' Test 2 Edge case that needs rotation '''
# packer.add_bin(Bin("Le grande box", 100, 100, 300, 1500))
# packer.add_item(Item("Item 1", 150, 50, 50, 1500))


# ''' Test 3 Test three items fit into smaller bin '''
# packer.add_bin(Bin("Le petite box", 296, 296, 8, 1000))
# packer.add_bin(Bin("Le grande box", 2960, 2960, 80, 10000))
# packer.add_item(Item("Item 1", 250, 250, 2, 200))
# packer.add_item(Item("Item 2", 250, 250, 2, 200))
# packer.add_item(Item("Item 3", 250, 250, 2, 200))


''' Test 4 Test three items fit into larger bin '''
# packer.add_bin(Bin("Le petite box", 296, 296, 8, 1000))
# packer.add_bin(Bin("Le grande box", 2960, 2960, 80, 10000))
# packer.add_item(Item("Item 1", 2500, 2500, 20, 2000))
# packer.add_item(Item("Item 2", 2500, 2500, 20, 2000))
# packer.add_item(Item("Item 3", 2500, 2500, 20, 2000))


''' Test 5 1 bin with 7 items fit into '''
# packer.add_bin(Bin("Bin 1", 220, 160, 100, 110))
# packer.add_item(Item("Item 1", 20, 100, 30, 10))
# packer.add_item(Item("Item 2", 100, 20, 30, 10))
# packer.add_item(Item("Item 3", 20, 100, 30, 10))
# packer.add_item(Item("Item 4", 100, 20, 30, 10))
# packer.add_item(Item("Item 5", 100, 20, 30, 10))
# packer.add_item(Item("Item 6", 100, 100, 30, 10))
# packer.add_item(Item("Item 7", 100, 100, 30, 10))


packer.pack(distribute_items=False, bigger_first=False)


figure_num = 0
for b in packer.bins:
    print("\n:::::::::::Box", str(figure_num + 1))
    print(":::::::::::", b.string())

    result_dict = {}
    result_dict["weight"] = float(b.max_weight)
    result_dict["width"] = float(b.width)
    result_dict["height"] = float(b.height)
    result_dict["length"] = float(b.depth)
    result_dict["volume"] = float(b.width * b.height * b.depth)
    result_dict["placement"] = []

    print("FITTED ITEMS:")
    for item in b.items:
        print("====> ", item.string())
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

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    if len(b.items) > 0:
        # print()
        result_json = json.dumps(result_dict)
        # print(result_json)

        plt1 = plot_multiple_package(result_json, "Box " + str(figure_num + 1) + " " + b.name, figure_num)
        plt1.show()
        figure_num+=1
    
    print("\n")

