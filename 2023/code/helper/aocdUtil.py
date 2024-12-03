def getData(day:int, year:int, save:bool=True):
    import aocd;
    data = aocd.get_data(day=day, year=year, block=True)
    if(save):
        with open('helper/input', 'w+') as f:
            f.write(data)
    return data

def submit(answer,day:int,year:int,part:str):
    import aocd;
    aocd.submit(answer=answer, day=day, year=year, part=part)