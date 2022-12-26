from classes import Univer

def main(univer):
    univer.create_table()
    univer.fill_DB()
    univer.print_help()
    while True:
        print('==============================================================')
        cmd = input('command: ').lower()
        print('==============================================================')
        if cmd == 'exit':
            break
        if cmd == 'help':
            univer.print_help()
        else:
            univer.query(*cmd.strip().split(' '))



if __name__ == '__main__':
    db = Univer()
    with db as univer:
        main(univer)

