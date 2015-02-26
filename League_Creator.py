from __future__ import division
# -*- coding: cp1252 -*-
import random
class Team(object):
    def __init__(self,name,o,d,p):
        self.name = name
        self.o = o
        self.d = d
        self.p = p
        self.w = 0
        self.l = 0
        self.pf = 0
        self.pa = 0
        self.pyth = 16.5
    def proj_result(self,other,pr):
        pf = self.o * other.d * .5 * (self.p + other.p) * .0001
        pa = self.d * other.o * .5 * (self.p + other.p) * .0001
        chance = pf ** self.pyth / (pf ** self.pyth + pa ** self.pyth)
        if pr:
            print 'The projected score is %s %s, %s %s' % (self.name,int(round(pf,0)),other.name, int(round(pa,0)))
            print 'The odds of the %s winning are %s percent.' % (self.name,round(100*chance,1))
        rand = .01*random.randint(0,100)
        if chance > rand:
            if pr:
                print self.get_name() + ' win'
            self.add_w()
            other.add_l()
        else:
            if pr:
                print other.get_name() + ' win'
            self.add_l()
            other.add_w()
        return chance
    def greater_than(self, other):
        if self.w-self.l != other.w-other.l:
            return self.w-self.l > other.w-other.l
        return self.name < other.name
    def print_out(self):
        print '%s: Off: %s, Def: %s, Pace: %s' % (self.name,round(self.o,1),round(self.d,1),round(self.p,1))
    def get_name(self):
        return str(self.name)
    def get_wp(self):
        if self.w+self.l > 0:
            return ((self.w + 0.000) /(self.w+self.l))+0.000
        return .000
    def add_w(self):
        self.w += 1
    def add_l(self):
        self.l += 1
    def reset(self):
        self.w = 0
        self.l = 0
    def get_w(self):
        return self.w
    def get_l(self):
        return self.l
    def set_w(self,num):
        self.w = num
    def set_l(self,num):
        self.l = num
    def print_standing(self):
        print '%s: %s-%s, %s' % (self.name,self.w,self.l,"%0.3f" % self.get_wp())
    def get_gp(self):
        return self.w+self.l
    def get_pyth(self):
        return self.o ** self.pyth / (self.o ** self.pyth + self.d ** self.pyth)
class CollegeTeam(Team):
    def __init__(self,name,o,d,p,luck):
        self.name = name
        self.o = o
        self.d = d
        self.p = p
        self.w = 0
        self.l = 0
        self.pf = 0
        self.pa = 0
        self.pyth = 10.25
        self.luck = luck
    def proj_result(self,other,pr):
        pf = self.o * other.d * .5 * (self.p + other.p) * .0001
        pa = self.d * other.o * .5 * (self.p + other.p) * .0001
        luck = .5 * (self.luck - other.luck)
        pf += (luck/130)
        pa -= (luck/130)
        chance = pf ** self.pyth / (pf ** self.pyth + pa ** self.pyth)
        if pr:
            print 'The projected score is %s %s, %s %s' % (self.name,int(round(pf,0)),other.name, int(round(pa,0)))
            print 'The odds of the %s winning are %s percent.' % (self.name,round(100*chance,1))
        rand = .01*random.randint(0,100)
        if chance > rand:
            if pr:
                print self.get_name() + ' win'
            self.add_w()
            other.add_l()
        else:
            if pr:
                print other.get_name() + ' win'
            self.add_l()
            other.add_w()
        return chance
class League(object):
    def __init__(self,name,size,version):
        self.name = name
        l = []
        self.version = version
        if version == 0:
            f = open("team_name_list.txt","r")
            s1 = f.read()
            f.close()
            s1 = s1.split(',')
            f = open("top5000populated.txt","r")
            s2 = f.read()
            f.close()
            s2 = s2.split(',')
            for i in range(size):
                n1 = random.choice(s1)
                s1.remove(n1)
                n2 = random.choice(s2)
                s2.remove(n2)
                n = n2 + ' ' + n1
                o = 90+.1*random.randint(0,200)
                d = 90+.1*random.randint(0,200)
                p = 60+.1*random.randint(0,50)
                l.append(CollegeTeam(n,o,d,p,0))
                i += 1
                self.l = l
        elif version == 1:
            f = open("more_nba_data.txt","r")
            s = f.read()
            f.close()
            s = s.split('-')
            for each in s:
                tm = each.split(',')
                # had to fix an odd string appending to the first name below
                name = str(tm[0])
                ind = int(name.find('¿'))
                name = name[ind+1:]
                l.append(Team(str(name),float(tm[1]),float(tm[2]),float(tm[3])))
                self.l = l
        else:
            f = open("college_data.txt","r")
            s = f.read()
            f.close()
            s = s.split('@')
            l = []
            for i in range(size):
                tm = random.choice(s)
                s.remove(tm)
                tm = tm.split(',')
                # had to fix an odd string appending to the first name below
                name = str(tm[0])
                ind = int(name.find('¿'))
                name = name[ind+1:]
                l.append(CollegeTeam(name,float(tm[1]),float(tm[2]),float(tm[3]),float(tm[4])))
                i += 1
            self.l = l
    def print_out(self):
        if self.version == 1 or self.version == 0:
            print 'Teams in ' + self.name + ':'
        else:
            print 'NCAA teams in use:'
        for each in self.l:
            each.print_out()
    def play_random(self):
        team1 = random.choice(self.l)
        team2 = random.choice(self.l)
        while team1 == team2:
            team2 = random.choice(self.l)
        team1.proj_result(team2,True)
    def get_name(self):
        return self.name
    def sort_league(self):
        for i in range(0,len(self.l)-1):
            for r in range(i+1,len(self.l)):
                if not(self.l[i].greater_than(self.l[r])):
                    temp = self.l[r]
                    self.l[r] = self.l[i]
                    self.l[i] = temp
                r += 1
            i += 1
    def print_standings(self):
        print self.name + ' Standings:'
        self.sort_league()
        for each in self.l:
            if each.name[0] == '#':
                each.name = each.name[3:]
                if each.name[0] == ' ':
                    each.name = each.name[1:]
            if self.l.index(each) < (25/351)*len(self.l):
                each.name = '#' + str(self.l.index(each)+1) + ' ' + each.name
            each.print_standing()
    def get_list(self):
        return self.l
    def get_gp(self):
        gp = 0
        for each in self.l:
            gp += each.get_gp()
        return gp

def play_league(l,reset,num):
    if reset:
        for each in l.get_list():
            each.reset()
    count = 0
    r = int(num/len(l.get_list()))
    while l.get_gp() < num*len(l.get_list()):
        for each in l.get_list():
            for team in l.get_list(): 
                if each.get_gp() == num:
                    break
                if each.get_name() != team.get_name() and team.get_gp() < num:
                    each.proj_result(team,False)
        count += 1
        if count > r:
            break
    if l.get_gp() < num*len(l.get_list()):
        for each in l.get_list():
            each.set_w(int(num*each.get_pyth()+.5))
            each.set_l(num-each.get_w())
              
    print ' '
    l.print_standings()
    print ' '
    
def simulate_season():
    print 'Welcome to the Season Simulator'
    print ''
    ch = str(raw_input('Would you like to use real teams? Enter y/n here: '))
    if ch == 'y':
        while ch!='n' and ch!='c': 
            ch = str(raw_input('Would you like to use NBA teams or College teams? Enter n/c here: '))
        if ch == 'n':
            l = League('NBA',0,1)
            print ' '
            l.print_out()
            print ' '
            state = 0
            while state >= 0: 
                state = int(raw_input('No. of %s games to play (neg. number ends program): ' % (l.get_name())))
                if state < 0:
                    print ' '
                    print 'Thank you for using the Season Simulator'
                    return
                play_league(l,True,state)
        while not(ch >= 2 and ch <= 351):
            ch = int(raw_input('Enter a no. of random NCAA teams to use (from 2 to 351): '))
        l = League('NCAA',ch,2)
        print ' '
        l.print_out()
        print ' '
        state = 0
        while state >= 0:
            state = int(raw_input('No. of %s games to play (neg. number ends program): ' % (l.get_name())))
            if state < 0:
                print ' '
                print 'Thank you for using the Season Simulator'
                return
            play_league(l,True,state)
    n = str(raw_input('Enter a name for your league: '))
    num = int(raw_input('Enter an even amount of teams to generate in the ' + n + ' (from 2 to 30): '))
    while not(num >= 2 and num <=30 and num % 2 == 0):
        num = int(raw_input('Enter an even amount of teams to generate in the ' + n + ' (from 2 to 30): '))
    l = League(n,num,0)
    print ''
    print 'Congratulations on creating the %s!' % (l.get_name())
    print ' '
    l.print_out()
    print ''
    state = 0
    while state >= 0: 
        state = int(raw_input('No. of %s games to play (neg. number ends program) ' % (l.get_name())))
        if state < 0:
            print ' '
            print 'Thank you for using the Season Simulator'
            return
        play_league(l,True,state)
simulate_season()
