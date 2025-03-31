max_value : int = 10000
def main():
    current_term  = 0
    next_term = 1
    
    while current_term <= max_value:
        print(current_term)
        term_after_next = current_term + next_term
        current_term = next_term
        next_term = term_after_next
main()



