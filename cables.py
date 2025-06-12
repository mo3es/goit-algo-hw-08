import heapq
import random

# Найменша загальна сума повторних попарних сум буде дорівнювати 
# попарним сумам найменших елементів послідовності, оскільки більші величини
# меншу кількість раз беруть участь у формуванні фінального результату

def get_min_cables_sum(cables_length):

    if len(cables_length) <= 1:
        return 0

    heapq.heapify(cables_length)

    result_sum = 0

    while len(cables_length) > 1:

        current_sum = heapq.heappop(cables_length) + heapq.heappop(cables_length)
        result_sum += current_sum
        heapq.heappush(cables_length, current_sum)

    return result_sum


if __name__ == "__main__":

    test_list = []
    for i in range(10):
        test_list.append(random.randint(1,10)*10)
    print(test_list)
    print(get_min_cables_sum(test_list))