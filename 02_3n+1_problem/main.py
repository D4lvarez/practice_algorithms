def cycle_length(value: int, limit: int) -> list[int]:
    counter = 0
    results: list[int] = [value]

    for n in results:
        if counter != 0 and n == 1:
            break

        if n >= limit:
            break

        if n % 2 != 0:
            n = (n * 3) + 1
        else:
            n = n / 2

        results.append(int(n))
        counter += 1

    results.insert(1, limit)
    return results


if __name__ == "__main__":
    values = input("Insert pair of numbers: ")

    data = values.split(" ")
    data = [int(n) for n in data]

    for n in data:
        if n < 0 or n > 10_000:
            raise ValueError("min: 1 - max: 10.000")

    results = cycle_length(data[0], data[1])

    response = len(results[2:])

    print(f"{data[0]} {data[1]} {response}")
