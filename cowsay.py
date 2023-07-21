from heifer_generator import HeiferGenerator
import sys

#returns list of cow names
def list_cows(cows):
    x = []
    for i in cows:
        x.append(i.name)
    return x

#returns cow mathing name arg passed in
def find_cow(name,cows):
    for i in cows:
        if i.name == name:
            return i


def main():

    #imports cow list
    cows = HeiferGenerator.get_cows()
    fileCows = HeiferGenerator.get_file_cows()

    #list all command line args
    args = sys.argv

    #prints cow list
    if args[1] == '-l':
        print("Cows available:", *list_cows(cows))
        print("File cows available: ", *list_cows(fileCows))


    #finds specified cow and prints its image and message
    elif args[1] == '-n':
        if find_cow(args[2],cows) == None:
            print(f'Could not find {args[2]} cow!')
        else:
            print(*args[3:])
            print(find_cow(args[2], cows).image)
            if find_cow(args[2], cows).name == 'dragon':
                print('This dragon can breathe fire.')
            elif find_cow(args[2], cows).name == 'ice-dragon':
                print('This dragon cannot breathe fire.')

    elif args[1] == '-f':
        if find_cow(args[2],fileCows) == None:
            print(f'Could not find {args[2]} cow!')
        else:
            print(*args[3:])
            print(find_cow(args[2], fileCows).image.decode())
     #default cow and msg       
    else:
        print(*args[1:])
        print(cows[0].image)

    




if __name__ == "__main__":
    main()