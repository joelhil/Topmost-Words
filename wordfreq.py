# wordfreq.py a part of lab 1
# Joel H 3/07-2020


def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        end = 0
        line = line + " "
        # if start is shorter than the length of line
        while start < len(line) and end < len(line):
            while line[start].isspace() and start+1 < len(line):
                start = start+1
            else:
                if start+1 >= len(line):
                    break

                elif line[start].isalpha():
                    end = start
                    while line[end].isalpha():
                        end = end + 1
                    this = line[start:end]
                    words.append(this.lower())
                    start = end

                elif line[start].isdigit():
                    end = start
                    while line[end].isdigit():
                        end = end + 1
                    words.append(line[start:end])
                    start = end
                else:
                    words.append(line[start])
                    start = start + 1
    return words


def countWords(words, stopWords):
    wordamount = {}
    stoplist = ["."]
    for line in stopWords:
        line = line.strip()
        stoplist.append(line)

    for word in words:
        if word not in stoplist:
            if word not in wordamount:
                wordamount[word] = 1
            elif word in wordamount:
                wordamount[word] = int(wordamount[word])+1

    return wordamount


def printTopMost(frequencies, n):
    count = 0
    for word, freq in sorted(frequencies.items(), key=lambda x: -x[1]):
        if count < n:
            print(word.ljust(20)+str(freq).rjust(5))
            count = count + 1
