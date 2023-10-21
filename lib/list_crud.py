import random;
def create_an_empty_list():
    return [];

def create_a_list():
    return [int(random.random() * 10) for i in range(4)];

def add_element_to_end_of_list(l, element):
    if (l == None): return [element];
    else:
        l.append(element);
        return l;

def add_element_to_start_of_list(l, element):
    if (l == None): return [element];
    else:
        l.insert(0, element);
        return l;

def remove_element_from_end_of_list(l):
    if (l == None): return None;
    else:
        l.pop();
        return l;

def remove_element_from_start_of_list(l):
    if (l == None): return None;
    elif (len(l) < 1): return [];
    else:
        l.remove(l[0]);
        return l;

def retrieve_first_element_from_list(l):
    if (l == None or len(l) < 1): return None;
    else: return l[0];

def retrieve_element_from_index(l, index):
    if (l == None or len(l) < 1): return None;
    elif (index < 0 or index > len(l) - 1): raise Exception("invalid index found and used here!");
    else: return l[index];

def retrieve_last_element_from_list(l):
    if (l == None or len(l) < 1): return None;
    else: return l[len(l) - 1];

#print(create_a_list());
