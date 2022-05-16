
def construct_pi(pattern):

    pi_table = [0]*len(pattern)

    prefix_counter = 0
    i = 1

    # O(M) linear running time
    while i < len(pattern):
        if pattern[i] == pattern[prefix_counter]:
            prefix_counter = prefix_counter + 1
            pi_table[i] = prefix_counter
            i = i + 1
        else:
            if prefix_counter != 0:
                prefix_counter = pi_table[prefix_counter-1]
            else:
                pi_table[i] = 0
                i = i + 1

    return pi_table


def search(text, pattern):

    pi_table = construct_pi(pattern)
    # index i tracks the text - index j tracks the pattern
    i = 0
    j = 0

    # iterate until the i index is less than the N length of the text
    # and have to make sure j is smaller than the M length of the pattern
    while i < len(text) and j < len(pattern):
        # if the letters are matching we increment both indexes
        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1
        if j == len(pattern):
            print('Pattern found at index %s' % (i-j))
            j = pi_table[j - 1]
        # if there is a mismatch
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = pi_table[j-1]
            else:
                i = i + 1


if __name__ == '__main__':

    search('my name is pyry', 'pyry')




