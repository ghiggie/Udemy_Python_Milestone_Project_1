from typing import List, Dict, Union

version: str = "0.2"
creator: str = "Garrett Higginbotham"
updated: str = "April 18, 2021"

movie_list: List[Dict[str, Union[str, int]]] = []
metadata_list: List[str] = ['Title']
running: bool = True


def welcome_message() -> None:
    print("Welcome to the movie library created by {0}.".format(creator))
    print("This is version {0}, and was last updated on {1}.\n".format(version, updated))


def add_movie() -> None:
    global movie_list

    movie_dic: Dict[str, Union[str, int]] = {}
    for meta in metadata_list:
        meta_val = input(meta + '? ')
        movie_dic[meta] = meta_val.strip()

    movie_list.append(movie_dic)


def find_movie() -> None:
    print('Movie Finder')
    print('------------\n')

    print('At the moment, this program can only search by movie title.')

    option = input('''What is the title of the movie you would like to find?
>> ''')
    try:
        for movie in movie_list:
            if movie['Title'] == option:
                for key in movie:
                    print(movie[key])
    except KeyError:
        print('Movie not found.')


def remove_movie() -> None:
    print('Movie Removal')
    print('-------------\n')

    option = input('''What is the title of the movie you would like to remove?
>> ''')
    try:
        for movie in movie_list:
            if movie['Title'] == option:
                movie_list.remove(movie)
    except KeyError:
        print('No such movie exists.')


def edit_movie() -> None:
    # raise NotImplementedError()
    print('At the moment, this program can only search by movie title.')
    movie_choice = input('''What is the title of the movie you would like to edit?
>> ''')
    print('Which metadata would you like to edit? You may choose from the following list:')
    print_metadata()
    meta_choice = input('>> ')
    new_meta = input('''What is the new metadata value?
>> ''')
    for movie in movie_list:
        if movie['Title'] == movie_choice:
            movie[meta_choice.lower().capitalize()] = new_meta


def print_movie_list() -> None:
    for movie in movie_list:
        for key in movie:
            out_str = key + ': ' + movie[key]
            print(out_str)
        print('\n')


def metadata_menu() -> None:
    meta_menu: bool = True
    print('Metadata Menu')
    print('-------------\n')
    meta_options = {      'ADD': add_metadata,
                       'DELETE': remove_metadata,
                    'REARRANGE': rearrange_metadata,
                        'PRINT': print_metadata}

    while meta_menu:
        option = input('''You may choose from any of the following options:\n
        * Type 'add' to add movie metadata\n
        * Type 'delete' to remove movie metadata\n
        * Type 'rearrange' to rearrange movie metadata\n
        * Type 'print' to print current metadata\n
        * Type 'back' to go back to the main menu\n
>> ''')
        print('\n')

        try:
            if option.strip().upper() == 'BACK':
                meta_menu = False
            else:
                call_meta = meta_options[option.strip().upper()]
                try:
                    call_meta()
                except NotImplementedError:
                    print('This feature has not been implemented yet.')
        except KeyError:
            print('Invalid entry. Please choose from the given list.')


def add_metadata() -> None:
    global movie_list
    global metadata_list
    new_data = input('What kind of data would you like to add to the metadata? ')
    metadata_list.append(new_data.strip().lower().capitalize())
    for movie in movie_list:
        movie[new_data.lower().capitalize()] = ""


def remove_metadata() -> None:
    # raise NotImplementedError('There are issues with this function.')
    global movie_list
    global metadata_list

    option_meta = input('''What metadata would you like to remove?\n
>> ''')
    try:
        metadata_list.remove(option_meta.lower().capitalize())
    except ValueError:
        print('That is not one of the current metadata types.')
    else:
        for movie in movie_list:
            movie.pop(option_meta.lower().capitalize())


def rearrange_metadata() -> None:
    raise NotImplementedError()
    # global metadata_list
    # global movie_list


def print_metadata() -> None:
    print('The following are the current metadata types:\n')
    for data in metadata_list:
        print('* ' + data)


def end_program() -> None:
    global running
    running = False


def menu() -> None:
    menu_dic = {   'ADD': add_movie,
                  'FIND': find_movie,
                'REMOVE': remove_movie,
                  'META': metadata_menu,
                 'PRINT': print_movie_list,
                  'EDIT': edit_movie,
                  'QUIT': end_program}

    print('Main Menu')
    print('---------\n')

    option_main = input('''You may choose from any of the following options:\n
    * Type 'add' to add a movie\n
    * Type 'find' to find a movie\n
    * Type 'remove' to remove a movie\n
    * Type 'meta' to edit movie metadata\n
    * Type 'print' to display all movies\n
    * Type 'edit' to change a movie entry\n
    * Type 'quit' to end the program\n
>> ''')
    print('\n')

    try:
        call_main = menu_dic[option_main.strip().upper()]
        try:
            call_main()
        except NotImplementedError:
            print("This feature has not been implemented yet.")
    except KeyError:
        print('Invalid entry. Please choose from the given list.')


def main() -> None:
    welcome_message()
    while running:
        menu()


if __name__ == "__main__":
    main()
