def get_recorde():
    """Retorna o recorde atual"""
    try:
        with open('recorde.txt', 'r') as a:
            l = a.readlines()
        x = l[0].split()
        for i in x:
            if i.isnumeric():
                return int(i)
        with open('recorde.txt', 'w') as a:
            a.write(f'recorde = 0')
        return 0
    except:
        return 0


def set_recorde(valor):
    """Seta o novo maior como recorde, se este for maior"""
    if valor > get_recorde():
        with open('recorde.txt', 'w') as a:
            a.write(f'recorde = {valor}')
