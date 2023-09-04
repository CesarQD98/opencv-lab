import time

DATA_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_current_datetime():
    current_time = time.localtime()
    formatted_datetime = time.strftime("%Y-%m-%d_%H-%M-%S", current_time)
    filename = f"{formatted_datetime}"
    return filename


def main():
    with open(f"./logs/{get_current_datetime()}.csv", "w") as file:
        for elem in DATA_ARRAY:
            file.write(f"{elem}\n")

    file.close()


if __name__ == "__main__":
    main()
