# Use: 
# python3 example_script.py --data_file data/pride_and_prejudice.txt -n 3 --results_dir results/test

import argparse
import os
import pdb
import datetime

def log(msg): 
    # get the current time  + date 
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{date_string}] {msg}")
    if log.logfile is not None:
        with open(log.logfile, 'a') as f:
            f.write(f"[{date_string}] {msg}\n")

log.logfile = None

def parse_args():
    # Create the parser
    parser = argparse.ArgumentParser(description='Example script')
    # Add the arguments
    # --data_file, required 
    parser.add_argument('--data_file', type=str, required=True, 
                        help='Path to data file, must be txt')
    # -n argument for order of shannon n-gram 
    parser.add_argument('-n', type=int, default=2, 
                        help='Order of Shannon n-gram')

    # results_dir, mandatory,
    parser.add_argument('--results_dir', type=str, required=True,
                        help='Directory to save results')

    # Parse the arguments
    args = parser.parse_args()
    return args


def load_data(data_file_path):
    # TODO 
    ...


def process_data(data):
    # TODO
    ...





def main():
    # Parse the arguments
    args = parse_args()
    # Set the log file

    log.logfile = os.path.join(args.results_dir, 'log.txt')
    # Log the arguments
    log('=== START OF TEST SCRIPT ===')
    log(f'Arguments: {args}')

    # Load the data
    data = load_data(args.data_file)

    # Process the data (all lowercase, extract list of all characters)
    data = process_data(data)

    # define a mapping from each character to 1 integer (probably a dictionary)
    # e.g., ctoi = {'a': 0, 'b': 1, ...}, itoc = {0: 'a', 1: 'b', ...}


    # define a numpy array of ones with shape [len(ctoi), len(ctoi), ...] where the number of dimensions is the order of the n-gram

    """ 
    DISCUSSION - not real code, this is pseudocode

    next_token_freqs = one_gram_frequencies[prev_char_id]
    # normalize next_token_freqs, a numpy array of shape [len(ctoi)]
    next_token_freqs = next_token_freqs / np.sum(next_token_freqs)




    two_gram_frequencies[char_i-2][char_i-1] = [list_of_character_frequencies_i]

    char_freqs = two_gram_frequencies[char_i-2][char_i-1]
    # normalize char_freqs, a numpy array of shape [len(ctoi)]
    char_freqs = char_freqs / np.sum(char_freqs)
    """



    
    


if __name__ == '__main__':
    main()
