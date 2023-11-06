def largest_radial_sum(honor_list: list, d: int) -> int:
    amount_of_groups = int(len(honor_list) / d)
    i = 0
    result_sum = []
    while i < amount_of_groups:
        result_sum.append(0)
        j = i
        while j < len(honor_list):
            result_sum[i] += honor_list[j]
            j += amount_of_groups
        i += 1
    return max(*result_sum)