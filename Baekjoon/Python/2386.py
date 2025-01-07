if __name__ == "__main__":
    while True:
        question = input()
        if question == '#':
            break
        alphabet, sentence = question[0], question[1:].lower()
        print(alphabet, sentence.count(alphabet))

# 참고한것 다시 해보기