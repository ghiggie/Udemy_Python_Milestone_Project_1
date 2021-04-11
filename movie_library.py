version = '0.1'
creator = 'Garrett Higginbotham'
updated = 'April 11, 2021'

movie_list = []
metadata_list = []
running = True

def welcome_message():
    print('Welcome to the movie library created by {0}'.format(creator))
    print('This is version {0}, and was last updated on {1}\n'.format(version, updated))

def add_movie():
    global movie_list

    for meta in metadata_list:
        movie_dic = {}
        meta_val = input(meta + '? ')
        movie_dic[meta] = meta_val

        try:
            movie_list.append(movie_dic)
        except:
            print('''Something went wrong when trying to append to the global
            movie_list in function 'add_movie()'.''')


def find_movie():
    raise NotImplementedError()


def remove_movie():
    raise NotImplementedError()


def edit_movie():
    raise NotImplementedError()


def print_movie_list():
    for movie in movie_list:
        for key in movie:
            out_str = key + ': ' + movie[key]
            print(out_str)


def metadata_menu():

    meta_menu = True
    print('Metadata Menu\n')
    print('-------------\n')
    meta_options = {      'ADD':  add_metadata,
                       'DELETE':  remove_metadata,
                    'REARRANGE':  rearrange_metadata,
                        'PRINT':  print_metadata}

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
            if (option.upper() == 'BACK'):
                meta_menu = False
            else:
                call = meta_options[option.upper()]
                try:
                    call()
                except NotImplementedError:
                    print('This feature has not been implemented yet.')
        except KeyError:
            print('Invalid entry. Please choose from the given list.')


def add_metadata():
    global metadata_list
    new_data = input('What kind of data would you like to add to the metadata? ')
    metadata_list.append(new_data)


def remove_metadata():
    global movie_list
    global metadata_list

    option = input('''What metadata would you like to remove?\n
>> ''')
    try:
        metadata_list.remove(option)
        for movie in movie_list:
            movie.pop(option)
    except ValueError:
        print('That is not one of the current metadata types.')


def rearrange_metadata():
    raise NotImplementedError()
    global metadata_list
    global movie_list


def print_metadata():
    raise NotImplementedError()


def end_program():
    global running
    running = False


def menu():

    menu_dic = {   'ADD':  add_movie,
                  'FIND':  find_movie,
                'REMOVE':  remove_movie,
                  'META':  metadata_menu,
                 'PRINT':  print_movie_list,
                  'EDIT':  edit_movie,
                  'QUIT':  end_program}

    print('Main Menu\n')
    print('---------\n')

    option = input('''You may choose from any of the following options:\n
    * Type 'add' to add a movie\n
    * Type 'find' to find a movie\n
    * Type 'remove' to remove a movie\n
    * Type 'meta' to edit ovie metadata\n
    * Type 'print' to display all movies\n
    * Type 'edit' to change a movie entry\n
    * Type 'quit' to end the program\n
>> ''')
    print('\n')

    try:
        call = menu_dic[option.upper()]
        try:
            call()
        except NotImplementedError:
            print("This feature has not been implemented yet.")
    except KeyError:
        print('Invalid entry. Please choose from the given list.')


def main():
    welcome_message()
    while running:
        menu()


if __name__ == "__main__":
    main()
