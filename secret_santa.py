import random


fail_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0,'g':0,'h':0, 'i':0, 'j':0}


def get_number():
    num_players = input('number of participants? ')
    while int(num_players) < 2:
        num_players = input('number of participants? ')
    return int(num_players)


def get_names(num_players):
    list_names = []
    for i in range(num_players):
        new_name = input('give me name #{}: '.format(i+1))
        list_names.append(new_name)
        i += 1
    return list_names


def get_pairs(list_names):
    pairs = {}
    available_picks = []
    available_picks += list_names
    i = 0
    fail_count = 0
    while i < len(list_names):
        element = list_names[i]
        recipient = random.choice(available_picks)
        available_picks.remove(recipient)
        if element == recipient:
            # print("{} picked their own name.".format(element))
            fail_dict[element] += 1
            fail_count += 1
            i = 0
            available_picks = []
            available_picks += list_names
            pairs = {}
            continue
        else:
            pairs[element] = recipient
            i += 1
    return pairs, fail_count


def secret_santa():
    # num_players = get_number()
    # list_names = get_names(num_players)
    fail_list = []
    for i in range(100000):
        pairs, fail_count = get_pairs(['a','b','c','d','e','f','g','h','i','j'])
        fail_list.append(fail_count)
    print(sum(fail_list)/len(fail_list))
    print(max(fail_list))
    for key in fail_dict:
        print(key, fail_dict[key]/100000)
    # pairs, fail_count = get_pairs(list_names)
    # for key in pairs:
    #     print("{} buys a gift for {} ".format(pairs[key], key))
    # print("fail count: {}".format(fail_count))
secret_santa()
