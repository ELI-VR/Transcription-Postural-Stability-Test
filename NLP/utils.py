import pickle


def handle_pickle(path, data=None, open_file=False):
    """
    saves and opens pickle file
    Args:
        path: path to save/open pickle file. When passing the path do not include the name of the pickle file.
        data: Object to be saved to pickle file
        open_file: if true, opens a pickle file

    Returns:

    """
    path= path + '/text_per_condition.pickle'

    if open_file:

        # Load data
        with open(path, 'rb') as handle:
            unserialized_data = pickle.load(handle)
            print(unserialized_data)

        return unserialized_data
    else:
        # Save data
        with open(path, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)



