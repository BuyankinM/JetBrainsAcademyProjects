def selection_sort(elements):
    for i in range(len(elements) - 1):
        index = i

        for j in range(i + 1, len(elements)):
            if elements[j] > elements[index]:
                index = j

        elements[i], elements[index] = elements[index], elements[i]