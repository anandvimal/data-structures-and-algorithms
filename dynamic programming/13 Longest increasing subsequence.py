numbers = [3, 1, 5, 2, 6, 4, 9]

def longest_increasing_subsequence(numbers):
    #empty case:
    if not numbers:
        return []
    # longest_ending_at[i] = longest increasing subsequence ending with numbers[i] # i_th row
    longest_ending_at = [] # this is 2d array. 
    for number in numbers:
        # longest_endiing_at[i] = longest sequence ending with numbers[i]
        # initially we form just [numbers]
        best_seq = [number]
        # consider all sequences found so far.
        for seq in longest_ending_at:
            # can we extend it monotonically wwith 'number' ?
            if seq[-1] < number:
                # does it lead to a longer sequence?
                if len(seq) + 1 > len(best_seq):
                    best_seq = seq + [number]
        #store the result
        longest_ending_at.append(best_seq)
    # find the longest of all sequences

    longest_increasing_subsequence_answer = []
    for row in longest_ending_at:
        if len(row) > len(longest_increasing_subsequence_answer):
            longest_increasing_subsequence_answer = row

    #return max(longest_ending_at, key=len), longest_ending_at
    return longest_increasing_subsequence_answer, longest_ending_at

result, longest_ending_at = longest_increasing_subsequence(numbers)
print(result)
