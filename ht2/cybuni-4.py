def unpack_sausages(truck):
    result = []

    for box in truck:
        for product in box:
            if "[" in product and "]" in product:
                if len(product) % 6 == 0:
                    if all([product[1] == product[i] for i in range(2,5)]):
                        result.append(product)
    for i in range(len(result)):
        if i % 4 == 0 and i != 0:
            result = [result[i] for i in range(len(result)) if i % 4 != 0 or i == 0]
    for i in range(len(result)):
        if result[i] and "[" in result[i] and "]" in result[i]:
            result[i] = result[i].replace("[", "").replace("]", "")
        result[i] = ' '.join(result[i])
    return " ".join(result)

# Приклад використання
truck = [
    ["(-)", "[IIII]", "[))))]"],
    ["IuI", "[llll]"],
    ["[@@@@]", "UwU", "[IlII]"],
    ["IuI", "[))))]", "x"],
    ["IuI", "[))))]", "x"],
    ["IuI", "[))))]", "x"],
    ["IuI", "[))))]", "x"],
    ["IuI", "[))))]", "x"]
]
result = unpack_sausages(truck)
print(result)