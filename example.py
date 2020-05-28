def hello():
    print('Hello')

def perfom_hello(user:str):
    print(f'Hi {user}')

def sum(a, b):
    return (a + b)

def div(a, b):
    if b < 0:
        print(f'{b} must be > 0')
        b = input('Enter new value: ')
    return (a/b)

if __name__ == "__main__":
    hello()
    perfom_hello('diego')
    print(sum(1,5))
    print(div(1,5))