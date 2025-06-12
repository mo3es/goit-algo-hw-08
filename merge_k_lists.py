import heapq
import random


#злиття та сортування несортованих списків
def merge_k_lists(lists):

    if lists is None or len(lists) < 1:
        return None

    result_list = []
    start_list = list(lists[0])
    heapq.heapify(start_list)

    for item_list in lists[1:]:
        for item in item_list:
            heapq.heappush(start_list, item)

    while len(start_list) > 0:
        result_list.append(heapq.heappop(start_list))

    return result_list



#злиття та сортування сортованих списків
def merge_k_sorted_lists(lists):

    result_list = []
    heap_translator = []

    for i, current_list in enumerate(lists):
        if current_list:
            heapq.heappush(heap_translator, (current_list[0], i, 0))

    while len(heap_translator) > 0:

        value, list_iterator_index, element_iterator_index = heapq.heappop(heap_translator)
        result_list.append(value)
        if element_iterator_index + 1 < len(lists[list_iterator_index]):
            heapq.heappush(heap_translator, (lists[list_iterator_index][element_iterator_index + 1], list_iterator_index, element_iterator_index + 1))

    return result_list


if __name__ == '__main__':

    lists = []

    for i in range(5):
        current_list = []
        for i in range(10):
            current_list.append(random.randint(0, 100))
        lists.append(current_list)

    print(lists)
    print(merge_k_lists(lists))


    lists_sorted = []
    for i in range(5):
        current_list = []
        for i in range(10):
            current_list.append(random.randint(0, 100))
        current_list.sort()
        lists_sorted.append(current_list)

    print(lists_sorted)
    print(merge_k_sorted_lists(lists_sorted))