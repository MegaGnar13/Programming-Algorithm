def solution(array, commands):
    answer_list = []

    for i in commands:

        start=i[0]
        end=i[1]
        what=i[2]
        if len(array)<end:
            return

        new_array=array[start-1:end]
        new_array.sort()
        answer=new_array[what-1]

        answer_list.append(answer)


    return print(answer_list)
solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])