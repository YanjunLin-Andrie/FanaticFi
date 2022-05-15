import PFanaticFi-UPDATE.ipynb





def AVGSTAT(DFSTATS,Status):
    MIN = 'min'
    for x in DFSTATS:
        
        if x == Status:
            if Status == 'FG%':
                FG = DFSTATS[x].describe()
                AVGFG = FG[MIN]
                return AVGFG
         
        
        if x == Status:
            if Status == 'FT%':
                FT = DFSTATS[x].describe()
                AVGFT = FT[MIN]
                return AVGFT
         
        
        if x == Status:   
            if x == '3P%':
                P3 = DFSTATS[x].describe()
                AVGP3 = P3[MIN]
                return AVGP3
        
        
        if x == Status:
            if x == 'APG':
                APG = DFSTATS[x].describe()
                AVGAPG = APG[MIN]
                return AVGAPG
        
        
        if x == Status:
            if x == 'PPG':
                PPG = DFSTATS[x].describe()
                AVGPPG = PPG[MIN]
                return AVGPPG
            
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#  GET player name 






# PGcalc(PG_25_df,'PPG')


# PG_25_df['Player']


def GETPLAYER(df,name):
    Player = 'Player'
    stats = ['FG%','FT%','Player','3P%','APG','PPG','Pos','Contract Worth']
    for x in df:
        if x == Player:
            find_player = df[x]
            for x in find_player:
                if x == name:
                    get_player = x
                    
                    player_Df = df[stats].set_index((Player))
                    
                    find_player =  player_Df.loc[get_player]
                    return find_player
            


#---------------------------------------------------------------------------------------------------------------------------------------------------------



def CURRENTSTAT(player,Status):
    PlayerSTATS = player[Status]
    return PlayerSTATS
   
      





#---------------------------------------------------------------------------------------------------------------------------------------------------------

def ADDPOINTS(x,a,avg,b):
  
    points = 0
    
    if x >= a:
        points = 3
        return  points
    elif x >= avg:
        points = 2
        return  points
    elif x >= b:
        points = 1
        return points
    elif x < b:
        points = 0
        return points
    else:
        points = 0
        return points
    #

    
def Profile(StatsDF,Name):
    stats = ['FT%','FG%', 'Player','3P%','APG','PPG','Pos']
    
    P = GETPLAYER(StatsDF,Name) 
   
    
    for x in stats:
        Status = x
   
   
        
        if x == Status:
            if Status == 'Pos':
                Position = P[Status]
                if Position == 'PG':
                    pos = Position
                    stats = ['FT%','FG%','3P%','APG','PPG']
                    for x in stats:
                         Status = x
                         
                         if x == Status:
                            if Status == '3P%':
                                
                                    _3above = AVGSTAT(PG_25_df,Status)
                                    
                                    _3avg = AVGSTAT(PG_50_df,Status)
                                    
                                    _3below = AVGSTAT(PG_75_df,Status)
                    
                                    _3PSTAT =CURRENTSTAT( P ,Status)
                                    _3P_points = ADDPOINTS( _3PSTAT,_3above , _3avg, _3below)  
                            
                            
                                    
                        
                         if x == Status:
                            if Status == 'FG%':
                                
                                    FGabove = AVGSTAT(PG_25_df,Status)
                                    
                                    FGavg = AVGSTAT(PG_50_df,Status)
                                    
                                    FGbelow = AVGSTAT(PG_75_df,Status)
                                    
            
                                    FGSTAT =CURRENTSTAT( P ,Status)
                                    FG_points = ADDPOINTS( FGSTAT,  FGabove, FGavg, FGbelow)
                            
                         if x == Status:           
                            if Status == 'FT%':
                                    FTGabove = AVGSTAT(PG_25_df,Status)
                                    
                                    FTGavg = AVGSTAT(PG_50_df,Status)
                                    
                                    FTGbelow = AVGSTAT(PG_75_df,Status)
                                    
                                    
                                    
                                    FGSTAT =CURRENTSTAT( P ,Status) 
                                    FG_points = ADDPOINTS( FGSTAT , FTGabove,FTGavg,FTGbelow )
         
                         if x == Status:
                            if Status == 'APG':
                                    
                                    APGabove = AVGSTAT(PG_25_df,Status)
                                    
                                    APGavg = AVGSTAT(PG_50_df,Status)
                                    
                                    APGbelow = AVGSTAT(PG_75_df,Status)
                            
                                    APGSTAT = CURRENTSTAT( P ,Status)       
                                    APG_points = ADDPOINTS( APGSTAT,APGabove,APGavg,APGbelow)
        
         
                         if x == Status:
                             if Status == 'PPG':
                                    
                                    PPGabove = AVGSTAT(PG_25_df,Status)
                                    
                                    PPGavg = AVGSTAT(PG_50_df,Status)
                                    
                                    PPGbelow = AVGSTAT(PG_75_df,Status)
                                
                                
                                
                                    PPGSTAT =CURRENTSTAT( P ,Status) 
                                    PPG_points = ADDPOINTS( PPGSTAT,PPGabove, PPGavg,PPGbelow)

                                    total = _3P_points +PPG_points +FG_points+APG_points  
                                    
                                    contract = P['Contract Worth']
                                    
                                    
                                    print(f'Player has {total} points with a contract of {contract} pos:{pos}')  
                
                elif Position == 'SG':
                    pos = Position
                    stats = ['FT%','FG%','3P%','APG','PPG']
                    for x in stats:
                         Status = x
                         
                         if x == Status:
                            if Status == '3P%':
                                
                                    _3above = AVGSTAT(SG_25_df,Status)
                                    
                                    _3avg = AVGSTAT(SG_50_df,Status)
                                    
                                    _3below = AVGSTAT(SG_75_df,Status)
                    
                                    _3PSTAT =CURRENTSTAT( P ,Status)
                                    _3P_points = ADDPOINTS( _3PSTAT,_3above , _3avg, _3below)  
                            
                            
                                    
                        
                         if x == Status:
                            if Status == 'FG%':
                                
                                    FGabove = AVGSTAT(SG_25_df,Status)
                                    
                                    FGavg = AVGSTAT(SG_50_df,Status)
                                    
                                    FGbelow = AVGSTAT(SG_75_df,Status)
                                    
            
                                    FGSTAT =CURRENTSTAT( P ,Status)
                                    FG_points = ADDPOINTS( FGSTAT,  FGabove, FGavg, FGbelow)
                            
                         if x == Status:           
                            if Status == 'FT%':
                                    FTGabove = AVGSTAT(SG_25_df,Status)
                                    
                                    FTGavg = AVGSTAT(SG_50_df,Status)
                                    
                                    FTGbelow = AVGSTAT(SG_75_df,Status)
                                    
                                    
                                    
                                    FGSTAT =CURRENTSTAT( P ,Status) 
                                    FG_points = ADDPOINTS( FGSTAT , FTGabove,FTGavg,FTGbelow )
         
                         if x == Status:
                            if Status == 'APG':
                                    
                                    APGabove = AVGSTAT(SG_25_df,Status)
                                    
                                    APGavg = AVGSTAT(SG_50_df,Status)
                                    
                                    APGbelow = AVGSTAT(SG_75_df,Status)
                            
                                    APGSTAT = CURRENTSTAT( P ,Status)       
                                    APG_points = ADDPOINTS( APGSTAT,APGabove,APGavg,APGbelow)
        
         
                         if x == Status:
                             if Status == 'PPG':
                                    
                                    PPGabove = AVGSTAT(SG_25_df,Status)
                                    
                                    PPGavg = AVGSTAT(SG_50_df,Status)
                                    
                                    PPGbelow = AVGSTAT(SG_75_df,Status)
                                
                                
                                
                                    PPGSTAT =CURRENTSTAT( P ,Status) 
                                    PPG_points = ADDPOINTS( PPGSTAT,PPGabove, PPGavg,PPGbelow)

                                    total = _3P_points +PPG_points +FG_points+APG_points  
                                    
                                    contract = P['Contract Worth']
                                    
                                    
                                    print(f'Player has {total} points with a contract of {contract} pos:{pos}')  
                
                
                
                
                elif Position == 'SF':
                    pos = Position
                    stats = ['FT%','FG%','3P%','APG','PPG']
                    for x in stats:
                         Status = x
                         
                         if x == Status:
                            if Status == '3P%':
                                
                                    _3above = AVGSTAT(SF_25_df,Status)
                                    
                                    _3avg = AVGSTAT(SF_50_df,Status)
                                    
                                    _3below = AVGSTAT(SF_75_df,Status)
                    
                                    _3PSTAT =CURRENTSTAT( P ,Status)
                                    _3P_points = ADDPOINTS( _3PSTAT,_3above , _3avg, _3below)  
                            
                            
                                    
                        
                         if x == Status:
                            if Status == 'FG%':
                                
                                    FGabove = AVGSTAT(SF_25_df,Status)
                                    
                                    FGavg = AVGSTAT(SF_50_df,Status)
                                    
                                    FGbelow = AVGSTAT(SF_75_df,Status)
                                    
            
                                    FGSTAT =CURRENTSTAT( P ,Status)
                                    FG_points = ADDPOINTS( FGSTAT,  FGabove, FGavg, FGbelow)
                            
                         if x == Status:           
                            if Status == 'FT%':
                                    FTGabove = AVGSTAT(SF_25_df,Status)
                                    
                                    FTGavg = AVGSTAT(SF_50_df,Status)
                                    
                                    FTGbelow = AVGSTAT(SF_75_df,Status)
                                    
                                    
                                    
                                    FGSTAT =CURRENTSTAT( P ,Status) 
                                    FG_points = ADDPOINTS( FGSTAT , FTGabove,FTGavg,FTGbelow )
         
                         if x == Status:
                            if Status == 'APG':
                                    
                                    APGabove = AVGSTAT(SF_25_df,Status)
                                    
                                    APGavg = AVGSTAT(SF_50_df,Status)
                                    
                                    APGbelow = AVGSTAT(SF_75_df,Status)
                            
                                    APGSTAT = CURRENTSTAT( P ,Status)       
                                    APG_points = ADDPOINTS( APGSTAT,APGabove,APGavg,APGbelow)
        
         
                         if x == Status:
                             if Status == 'PPG':
                                    
                                    PPGabove = AVGSTAT(SF_25_df,Status)
                                    
                                    PPGavg = AVGSTAT(SF_50_df,Status)
                                    
                                    PPGbelow = AVGSTAT(SF_75_df,Status)
                                
                                
                                
                                    PPGSTAT =CURRENTSTAT( P ,Status) 
                                    PPG_points = ADDPOINTS( PPGSTAT,PPGabove, PPGavg,PPGbelow)

                                    total = _3P_points +PPG_points +FG_points+APG_points  
                                    
                                    contract = P['Contract Worth']
                                    
                                    
                                    print(f'Player has {total} points with a contract of {contract} pos:{pos}')  
                
                
                elif Position == 'PF':
                    pos = Position
                    stats = ['FT%','FG%','3P%','APG','PPG']
                    for x in stats:
                         Status = x
                         
                         if x == Status:
                            if Status == '3P%':
                                
                                    _3above = AVGSTAT(PF_25_df,Status)
                                    
                                    _3avg = AVGSTAT(PF_50_df,Status)
                                    
                                    _3below = AVGSTAT(PF_75_df,Status)
                    
                                    _3PSTAT =CURRENTSTAT( P ,Status)
                                    _3P_points = ADDPOINTS( _3PSTAT,_3above , _3avg, _3below)  
                            
                            
                                    
                        
                         if x == Status:
                            if Status == 'FG%':
                                
                                    FGabove = AVGSTAT(PF_25_df,Status)
                                    
                                    FGavg = AVGSTAT(PF_50_df,Status)
                                    
                                    FGbelow = AVGSTAT(PF_75_df,Status)
                                    
            
                                    FGSTAT =CURRENTSTAT( P ,Status)
                                    FG_points = ADDPOINTS( FGSTAT,  FGabove, FGavg, FGbelow)
                            
                         if x == Status:           
                            if Status == 'FT%':
                                    FTGabove = AVGSTAT(PF_25_df,Status)
                                    
                                    FTGavg = AVGSTAT(PF_50_df,Status)
                                    
                                    FTGbelow = AVGSTAT(SG_75_df,Status)
                                    
                                    
                                    
                                    FGSTAT =CURRENTSTAT( P ,Status) 
                                    FG_points = ADDPOINTS( FGSTAT , FTGabove,FTGavg,FTGbelow )
         
                         if x == Status:
                            if Status == 'APG':
                                    
                                    APGabove = AVGSTAT(PF_25_df,Status)
                                    
                                    APGavg = AVGSTAT(PF_50_df,Status)
                                    
                                    APGbelow = AVGSTAT(PF_75_df,Status)
                            
                                    APGSTAT = CURRENTSTAT( P ,Status)       
                                    APG_points = ADDPOINTS( APGSTAT,APGabove,APGavg,APGbelow)
        
         
                         if x == Status:
                             if Status == 'PPG':
                                    
                                    PPGabove = AVGSTAT(PF_25_df,Status)
                                    
                                    PPGavg = AVGSTAT(PF_50_df,Status)
                                    
                                    PPGbelow = AVGSTAT(PF_75_df,Status)
                                
                                
                                
                                    PPGSTAT =CURRENTSTAT( P ,Status) 
                                    PPG_points = ADDPOINTS( PPGSTAT,PPGabove, PPGavg,PPGbelow)

                                    total = _3P_points +PPG_points +FG_points+APG_points  
                                    
                                    contract = P['Contract Worth']
                                    
                                    
                                    print(f'Player has {total} points with a contract of {contract} pos:{pos}')  
                 
                
                
                elif Position == 'C':
                
                    pos = Position
                    stats = ['FT%','FG%','3P%','APG','PPG']
                    for x in stats:
                         Status = x
                         
                         if x == Status:
                            if Status == '3P%':
                                
                                    _3above = AVGSTAT(C_25_df,Status)
                                    
                                    _3avg = AVGSTAT(C_50_df,Status)
                                    
                                    _3below = AVGSTAT(C_75_df,Status)
                    
                                    _3PSTAT =CURRENTSTAT( P ,Status)
                                    _3P_points = ADDPOINTS( _3PSTAT,_3above , _3avg, _3below)  
                            
                            
                                    
                        
                         if x == Status:
                            if Status == 'FG%':
                                
                                    FGabove = AVGSTAT(C_25_df,Status)
                                    
                                    FGavg = AVGSTAT(C_50_df,Status)
                                    
                                    FGbelow = AVGSTAT(C_75_df,Status)
                                    
            
                                    FGSTAT =CURRENTSTAT( P ,Status)
                                    FG_points = ADDPOINTS( FGSTAT,  FGabove, FGavg, FGbelow)
                            
                         if x == Status:           
                            if Status == 'FT%':
                                    FTGabove = AVGSTAT(C_25_df,Status)
                                    
                                    FTGavg = AVGSTAT(C_50_df,Status)
                                    
                                    FTGbelow = AVGSTAT(C_75_df,Status)
                                    
                                    
                                    
                                    FGSTAT =CURRENTSTAT( P ,Status) 
                                    FG_points = ADDPOINTS( FGSTAT , FTGabove,FTGavg,FTGbelow )
         
                         if x == Status:
                            if Status == 'APG':
                                    
                                    APGabove = AVGSTAT(C_25_df,Status)
                                    
                                    APGavg = AVGSTAT(C_50_df,Status)
                                    
                                    APGbelow = AVGSTAT(C_75_df,Status)
                            
                                    APGSTAT = CURRENTSTAT( P ,Status)       
                                    APG_points = ADDPOINTS( APGSTAT,APGabove,APGavg,APGbelow)
        
         
                         if x == Status:
                             if Status == 'PPG':
                                    
                                    PPGabove = AVGSTAT(SG_25_df,Status)
                                    
                                    PPGavg = AVGSTAT(SG_50_df,Status)
                                    
                                    PPGbelow = AVGSTAT(SG_75_df,Status)
                                
                                
                                
                                    PPGSTAT =CURRENTSTAT( P ,Status) 
                                    PPG_points = ADDPOINTS( PPGSTAT,PPGabove, PPGavg,PPGbelow)

                                    total = _3P_points +PPG_points +FG_points+APG_points  
                                    
                                    contract = P['Contract Worth']
                                    
                                    
                                    print(f'Player has {total} points with a contract of {contract} pos:{pos}')  
                
                    
                else :
                    print("No")
        
        
               
        
        
        
        
        
        