import sys

if "/usr/lib/python3/dist-packages" not in sys.path:
    sys.path.append("/usr/lib/python3/dist-packages")

import speechd

import random
import playsound as pa
from voxin import Voxin


def load_word_list():
    with open("word_list.txt") as f:
        data = f.read().split("\n")
        return [d.strip() for d in data if len(d.strip()) > 0]


def get_repetition_count():
    while True:
        try:
            count = int(
                input("\nPlease enter how many successive correct answer you'd like: ")
            )
            if count > 0:
                return count

            print("Please enter valid number > 0")
            continue
        except ValueError:
            print("Please enter valid number > 0")
            continue


def update_record(record, target_word, hit):
    if target_word not in record:
        record[target_word] = {"hit": 1, "missed": 0}
        return

    if hit == True:
        record[target_word]["hit"] = record[target_word]["hit"] + 1
    else:
        record[target_word]["missed"] = record[target_word]["missed"] + 1


def print_record(record):
    for word in record:
        hit = record[word]["hit"]
        missed = record[word]["missed"]
        total = hit + missed
        print(
            "{} success rate {:.2f}% {}/{}".format(
                word, 100.0 * hit / total, hit, total
            )
        )


def main():
    voxin = Voxin()
    counter = 0
    max_counter = get_repetition_count()
    word_list = load_word_list()
    target_word = random.choice(word_list)
    record = {}
    print(
        "Type the following word(s). If you've typed {} times correctly, you will be presented with new challenge".format(
            max_counter
        )
    )
    msg = "\ntarget word: {}".format(target_word)
    print(msg)
    voxin.speak(msg)

    while True:
        word = input().strip()
        if word == "--":
            voxin.speak("Goodbye")
            break

        if word == target_word:
            pa.playsound("open-object.wav")
            update_record(record, target_word, True)
            counter = counter + 1
        else:
            counter = 0
            update_record(record, target_word, False)
            pa.playsound("off.wav")

        if counter == max_counter:
            pa.playsound("news.wav")
            target_word = random.choice(word_list)
            counter = 0
            msg = "\nnext challenge word: {}".format(target_word)
            print(msg)
            voxin.speak(msg)
            continue

    voxin.close()
    print_record(record)


if __name__ == "__main__":
    main()
