import click, itertools, random, time


@click.command()
@click.argument('domain')
class Numbers:
    start_time = time.time()
    print('Start process...')

    def __init__(self, domain=''):
        self.domain = domain
        self.execution()
        file_name = str('num_dict' + self.domain + '.txt')
        self.write(file_name)

    def execution(self):
        exec = list(map(''.join, itertools.product('0123456789', repeat=int(self.domain))))
        self.exec = (sorted(exec, key=lambda exec: random.random()))
        print('\nNumber of combinations: ' + str(len(exec)))

    def write(self, file_name):
        with open(file_name, 'w') as file:
            file.write('\n'.join(self.exec))
        print(f'\nCompleted in: {time.time() - self.start_time:.2f} sec.')


search = Numbers()
