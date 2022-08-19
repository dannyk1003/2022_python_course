'''def sort_test(num):
    for i in range(len(num)):
        for j in 
'''

'''[1,3,2,5,4]

function bubble_sort (array, length) {
    var i, j;
    for(i from 0 to length-1){   i  = 0 1 2 3 4
        for(j from 0 to length-1-i){
            if (array[j] > array[j+1])
                swap(array[j], array[j+1])
        }
    }
}

1 3 2 5 4




[1,2,3,4,5]'''

def bubble_sorted(iterable):
    new_list = list(iterable)
    list_len = len(new_list)
    for i in range(list_len):
        for j in range(list_len - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
                print(new_list)
    return new_list
iterable = [5,4,3,2,1]
bubble_sorted(iterable)