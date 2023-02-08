def totalFruit(fruits) -> int:
    baskets = {}
    baskets_total = 0
    max_picked = 0

    last_continous_fruit = None
    last_continous_amount = None

    for i, fruit in enumerate(fruits):
        if len(baskets) < 2:
            if fruit in baskets:
                baskets[fruit] += 1
                baskets_total += 1
            else:
                baskets[fruit] = 1
                baskets_total += 1
                last_continous_fruit = fruit
                last_continous_amount = 1
            continue

        if fruit in baskets:
            baskets[fruit] += 1
            baskets_total += 1
            if last_continous_fruit == fruit:
                last_continous_amount += 1
            else:
                last_continous_fruit = fruit
                last_continous_amount = 1
        else:
            max_picked = max(max_picked, baskets_total)

            baskets.clear()
            baskets[last_continous_fruit] = last_continous_amount
            baskets[fruit] = 1
            baskets_total = last_continous_amount + 1

            last_continous_fruit = fruit
            last_continous_amount = 1


    max_picked = max(max_picked, baskets_total)
    return max_picked

print(totalFruit(fruits = [6,2,1,1,3,6,6]))
