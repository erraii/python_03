import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    total_arguments = len(sys.argv)
    arguments_received = total_arguments - 1
    # At the beginning of the game, your inventory is usually empty ;)
    inv_data: dict[str, int] = {}
    if (total_arguments < 2):
        print("No inventory data provided!")
    else:
        for arg in sys.argv[1:]:
            # Invalid parameter check
            if arg.count(":") != 1:
                print(f"Error - invalid parameter '{arg}'")
            else:
                item = arg.split(":")
                if item[0] in inv_data:
                    print(f"Redundant item '{item[0]}' - discarding")
                else:
                    try:
                        inv_data.update({item[0]: int(item[1])})
                    except Exception as e:
                        print(f"Quantity error for 'key': {e}")
        # print data if dictionary has item
        inv_len = len(inv_data)
        item_list = []
        quant_list = []
        if inv_len > 0:
            print(f"Got inventory: {inv_data}")
            for key in inv_data.keys():
                item_list.append(key)
                max_abundant = inv_data[key]
                min_abundant = inv_data[key]
            print(f"Item list: {item_list}")
            for value in inv_data.values():
                quant_list.append(value)
                if value >= max_abundant:
                    max_abundant = value
                if value <= min_abundant:
                    min_abundant = value
            print(f"Total quantity of the {inv_len} items: {sum(quant_list)}")
            max_item: str = ""
            min_item: str = ""
            for key in inv_data.keys():
                repr_perc = round((inv_data[key] / sum(quant_list)) * 100, 1)
                if not max_item:
                    if inv_data[key] == max_abundant:
                        max_item = key
                if not min_item:
                    if inv_data[key] == min_abundant:
                        min_item = key
                print(f"Item {key} represents {repr_perc}%")
            print(f"Item most abundant: {max_item}", end=" ")
            print(f"with quantity {inv_data[max_item]}")
            print(f"Item least abundant: {min_item}", end=" ")
            print(f"with quantity {inv_data[min_item]}")
    inv_data.update({"magic_item": 1})
    print(f"Updated inventory: {inv_data}")
    # print(f"Total inventory data: {total_arguments}")
