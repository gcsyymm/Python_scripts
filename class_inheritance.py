class char:
    def __init__(_, name, element, stat_atk, stat_def):
        _.name = name
        _.elm = element
        _.stat = [stat_atk, stat_def]
    def getid(_):
        print([_.name, _.elm])
    def stat(_):
        return _.stat()
    def getstat(_):
        print(f'ATK = {_.stat[0]},DEF = {_.stat[1]}')
ganyu = char('Ganyu', 'Cryro', 100, 70)
ganyu.getid()
ganyu.getstat()

class archer(char):
    pass
venti = archer('Venti','Anemo', 80, 80)
venti.getid()
venti.getstat()

class caster(char):
    def __init__(_, name, element, stat_atk, stat_def, nation):
        super().__init__(name, element, stat_atk, stat_def)
    #from here, the args appeared here in the super list will be inherited
    #to the new class initiation (as we defined the .name .elm . stat)      
        _.national = nation
    def getnation(_):
        print(_.national)
    def __str__(_):
        return f'{_.name}'

klee = caster('Klee', 'Pyro', 95, 75, 'Mondstatd')
print(klee)
klee.getid()
klee.getstat()
klee.getnation()
