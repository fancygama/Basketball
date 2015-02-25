from __future__ import division
import random
class Team(object):
    def __init__(self,name,otov,o2pm,o2px,o3pm,o3px,oftm,dtov,d2pm,d2px,d3pm,d3px,dftm,orb,drb,pace):
        self.name=name
        self.otov=float(otov)
        self.o2pm=float(o2pm)
        self.o2px=float(o2px)
        self.o3pm=float(o3pm)
        self.o3px=float(o3px)
        self.oftm=float(oftm)
        self.dtov=float(dtov)
        self.d2pm=float(d2pm)
        self.d2px=float(d2px)
        self.d3pm=float(d3pm)
        self.d3px=float(d3px)
        self.dftm=float(dftm)
        self.orb=float(orb)
        self.drb=float(drb)
        self.pace=float(pace)
        self.w = 0
        self.l = 0
        self.pf = 0
        self.pa = 0
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
    def str(self):
        return self.name
    def play_game(self,opp,disp):
        gpf = 0
        gpa = 0
        ot = 0
        otov = .5*(self.otov+opp.dtov)
        o2pm = .5*(self.o2pm+opp.d2pm)
        o2px = .5*(self.o2px+opp.d2px)
        o3pm = .5*(self.o3pm+opp.d3pm)
        o3px = .5*(self.o3px+opp.d3px)
        oftm = .5*(self.oftm+opp.dftm)
        dtov = .5*(self.dtov+opp.otov)
        d2pm = .5*(self.d2pm+opp.o2pm)
        d2px = .5*(self.d2px+opp.o2px)
        d3pm = .5*(self.d3pm+opp.o3pm)
        d3px = .5*(self.d3px+opp.o3px)
        dftm = .5*(self.dftm+opp.oftm)
        orb  = .5*(self.orb+opp.drb)
        drb  = .5*(self.drb+opp.orb)
        b = 0
        poss = 0
        while poss < (int(.5*(self.pace+opp.pace)+.5)):
            a = 0
            while a == 0:
                rand = .001*random.randint(0,1000)
                if rand <= otov:
                    break
                elif rand <= o2pm:
                    gpf += 2
                    break
                elif rand <= o2px:
                    if .001*random.randint(0,1000) <= orb:
                        continue
                    else:
                        break
                elif rand <= o3pm:
                    gpf += 3
                    break
                elif rand <= o3px:
                    if .001*random.randint(0,1000) <= orb:
                        continue
                    else:
                        break
                elif rand <= oftm:
                    gpf += 2
                    break
                else:
                    if .001*random.randint(0,1000) <= .5*orb:
                        continue
                    else:
                        break
            if disp > 1:        
                print '%s %s-%s %s' % (self.name,gpf,gpa,opp.name)
            while a == 0:
                rand = .001*random.randint(0,1000)
                if rand <= dtov:
                    break
                elif rand <= d2pm:
                    gpa += 2
                    break
                elif rand <= d2px:
                    if .001*random.randint(0,1000) <= drb:
                        continue
                    else:
                        break
                elif rand <= d3pm:
                    gpa += 3
                    break
                elif rand <= d3px:
                    if .001*random.randint(0,1000) <= drb:
                        continue
                    else:
                        break
                elif rand <= dftm:
                    gpa += 2
                    break
                else:
                    if .001*random.randint(0,1000) <= .5*drb:
                        continue
                    else:
                        break
            if disp > 1:
                print '%s %s-%s %s' % (self.name,gpf,gpa,opp.name)
            poss += 1
            if poss >= int(.5*(self.pace+opp.pace)+.5) and gpf == gpa:
                poss = int((43/48)*.5*(self.pace+opp.pace)+.5)
                ot += 1
                if disp > 0:
                    print '----------Start of OT No. %s----------'%(ot)
        winner = ''
        if gpf >= gpa:
            winner = self
            loser = opp
            win = gpf
            loss = gpa
        else:
            winner = opp
            loser = self
            win = gpa
            loss = gpf
        if ot > 0:
            otstr = ' (' + str(ot) + 'OT)'
        else:
            otstr = ''
        if disp > 0:
            print 'Final: %s %s, %s %s%s' % (winner.name, win, loser.name, loss,otstr)
        if disp == 0:
            score = []
            score.append(gpf)
            score.append(gpa)
            return score
    def play_games(self,opp,num):
        i = 0
        gpf = 0
        gpa = 0
        w = 0
        while i < num:
            scores = self.play_game(opp,0)
            gpf += scores[0]
            gpa += scores[1]
            i += 1
            if scores[0]>scores[1]:
                w += 1
        gpf = int(gpf/num+.5)*(99.9/105)
        gpa = int(gpa/num+.5)*(99.9/105)
        wp = (100*w/num)
        if gpf >= gpa:
            winner = self
            loser = opp
            win = gpf
            loss = gpa
        else:
            winner = opp
            loser = self
            win = gpa
            loss = gpf
        if 2*w >= num:
            winteam = self
            wp = wp
        else:
            winteam = opp
            wp = 100-wp
        wp =  '%0.2f' % wp
        print 'Average Final Score: %s %s, %s %s' % (winner.name, '%0.1f' % win, loser.name, '%0.1f' % loss)
        print 'The %s won %s percent  of the time' % (winteam.name, str(wp))
class League(object):
        def __init__(self):
            f = open("C:\\Users\\Owner\\Documents\\GitHub\\Basketball\\nba_data.txt","r")
            s = f.read()
            f.close()
            s = s.split(',')
            t = []
            for each in s:
                temp = each.split('-')
                t.append(temp)
            teams = []
            for team in t:
                name = team[0]
                otov = team[1]
                o2pm = team[2]
                o2px = team[3]
                o3pm = team[4]
                o3px = team[5]
                oftm = team[6]
                dtov = team[7]
                d2pm = team[8]
                d2px = team[9]
                d3pm = team[10]
                d3px = team[11]
                dftm = team[12]
                orb  = team[13]
                drb  = team[14]
                pace = team[15]
                tm = Team(name,otov,o2pm,o2px,o3pm,o3px,oftm,dtov,d2pm,d2px,d3pm,d3px,dftm,orb,drb,pace)
                teams.append(tm)
            self.teams = teams
        def print_out(self):
            i = 0
            for each in self.teams:
                print 'ID no. %s: %s' % (i,each.str())
                i += 1
        def get_team(self,num):
            return self.teams(num)
        def play_game(self,team1,team2,disp):
            self.teams[team1].play_game(self.teams[team2],disp)
        def play_games(self,team1,team2,num):
            self.teams[team1].play_games(self.teams[team2],num)
def game_simulator():
    l = League()
    print ''
    print 'Welcome to the NBA Game Simulator'
    print ''
    print 'Note: Individual Games have a 5% scoring increase'
    print ' '
    l.print_out()
    print ' '
    print 'You can quit the program by entering a negative number'
    print ' '
    a = 0
    ch = str(raw_input('Would you like to see the result of multiple simulations? Enter y/n here: '))
    if ch.lower()=='y':
        while a >= 0:
            print ' '
            a = int(raw_input('Select the first ID no. to play: '))
            if a < 0:
                print 'Thank you for using the NBA Game Simulator'
                return
            b = int(raw_input('Select the second ID no. to play: '))
            if b < 0:
                print 'Thank you for using the NBA Game Simulator'
                return
            num = int(raw_input('No. of sims to average: '))
            if num < 0:
                print 'Thank you for using the NBA Game Simulator'
                return
            print ' '
            l.play_games(a,b,num)
    else:
        while a >= 0:
            print ' '
            a = int(raw_input('Select the first ID no.: '))
            if a < 0:
                print 'Thank you for using the NBA Game Simulator'
                return
            b = int(raw_input('Select the second ID no.: '))
            if b < 0:
                print 'Thank you for using the NBA Game Simulator'
                return
            d = str(raw_input('Would you like to see a running score? Enter y/n here: '))
            if d.lower()=='y':
                print ' '
                l.play_game(a,b,2)
            else:
                print ' '
                l.play_game(a,b,1)
game_simulator()
