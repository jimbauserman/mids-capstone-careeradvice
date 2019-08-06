from string import punctuation

punc = punctuation.remove('-')

def clean_sum(summary):
    sum_list = list(summary)
    for i in range(0,len(sum_list)):
        if sum_list[i] in punctuation:
            sum_list[i-1], sum_list[i]=sum_list[i], sum_list[i-1]
    for i in range(0,len(sum_list)):        
        if sum_list[i] == '.' and i != len(sum_list):
            sum_list[i+2] = sum_list[i+2].upper()
    sum_list[0] = sum_list[0].upper()

    return ''.join(sum_list)