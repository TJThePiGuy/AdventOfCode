from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(day = 20, year = 2017)

def sign(num):
    if num == 0:
        return 0
    return 1 if num > 0 else -1
    

def part_a():
    time_steps = -1
    data = puzzle.input_data
    points = [_.split(', ') for _ in data.split('\n')]
    for point in points:
        pos = np.array([int(i) for i in point[0][3:-1].split(',')], dtype=int)
        vel = np.array([int(i) for i in point[1][3:-1].split(',')], dtype=int)
        acc = np.array([int(i) for i in point[2][3:-1].split(',')], dtype=int)

        p_s = [sign(i) for i in pos]
        v_s = [sign(i) for i in vel]
        a_s = [sign(i) for i in acc]
        curr_t = 0
        while(any(a_s[i] != 0 and (p_s[i]*a_s[i] < 0 or v_s[i]*a_s[i] < 0) for i in range(3))):
            curr_t += 1
            vel = vel + acc
            pos = pos + vel
            
            p_s = [sign(i) for i in pos]
            v_s = [sign(i) for i in vel]
        time_steps = max(time_steps, curr_t)

    shortest_dist = float('inf')
    shortest_ind = 0
    for idx, point in enumerate(points):
        pos = np.array([int(i) for i in point[0][3:-1].split(',')], dtype=int)
        vel = np.array([int(i) for i in point[1][3:-1].split(',')], dtype=int)
        acc = np.array([int(i) for i in point[2][3:-1].split(',')], dtype=int)

        for step in range(time_steps):
            vel = vel + acc
            pos = pos + vel
        dist = sum(abs(i) for i in pos)
        if(dist < shortest_dist):
            shortest_dist = dist
            shortest_ind = idx
    puzzle.answer_a = shortest_ind
    print(shortest_ind)
    pass

def get_int(p_diff, v_diff, a_diff):
    sets:list[set[int]] = []
    for idx in range(3):
        times = set()
        p = p_diff[idx]
        v = v_diff[idx]
        a = a_diff[idx]
        if(a == 0):
            if(v!= 0):
                times.add(-p/(v))
            elif(p == 0):
                times = set(range(200))
        else:
            discr = (2*v+a)**2 - 8 * a * p
            if(discr > 0):
                first = -(2*v+a)

                times.add((first + np.sqrt(discr))/(2*a))
                times.add((first - np.sqrt(discr))/(2*a))
        sets.append(times)

    times = sets[0].intersection(sets[1]).intersection(sets[2])
    return(times)

def part_b():
    data = puzzle.input_data
    # data = 'p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>\np=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>\np=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>\np=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>'
    points = [_.split(', ') for _ in data.split('\n')]
    pos = []
    vel = []
    acc = []
    for point in points:
        pos.append(np.array([int(i) for i in point[0][3:-1].split(',')], dtype=int))
        vel.append(np.array([int(i) for i in point[1][3:-1].split(',')], dtype=int))
        acc.append(np.array([int(i) for i in point[2][3:-1].split(',')], dtype=int))

    collisions:list[tuple[int,int,int] ]= list()

    for idx in range(len(points)):
        p1 = pos[idx]
        v1 = vel[idx]
        a1 = acc[idx]
        for jdx in range(idx+1, len(points)):
            p2 = pos[jdx]
            v2 = vel[jdx]
            a2 = acc[jdx]
            intersect = get_int(p1-p2, v1-v2, a1-a2)
            # print(idx, jdx, len(intersect))
            if(len(intersect)!= 0):
                for time in intersect:
                    collisions.append((time, idx, jdx))

    collisions.sort(key = lambda item: item[0])
    collision_times = sorted(list(set(item[0] for item in collisions)))
    still_alive:set[int] = set(range(len(points)))
    for time in collision_times:
        to_remove = set()
        for collision in collisions:
            if collision[0] != time:
                continue
            if not(collision[1] in still_alive) or not(collision[2] in still_alive):
                continue
            to_remove.add(collision[1])
            to_remove.add(collision[2])
        still_alive.difference_update(to_remove)
        # print(time)
    puzzle.answer_b = len(still_alive)
    print(len(still_alive))


part_a()
part_b()