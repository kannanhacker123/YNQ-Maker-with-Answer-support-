
aux1= [
'Do','Does',
'Did',
'Is','Am','Are',
'Was','Were',
'Has','Have','Had',
'Will','Shall',
'Would','Should' 
]
aux2 = [
'DO','DOES',
'DID',
'IS','AM','ARE',
'WAS','WERE',
'HAS','HAVE','HAD',
'WILL','SHALL',
'WOULD','SHOULD',
]
aux3 = [
'do','does',
'did',
'is','am','are',
'was','were',
'has','have','had',
'will','shall',
'would','should'
]
aux = aux1+aux2+aux3
t = True


def YNQM(state):
    NOE = 0
    s = state.split()
    stlen = len(state)
    for st in s:
        for i in aux:
            if stlen < 5 and st  == i:
                print('\n finded '+'"'+st+'"'+' as auxiliary  verb😎😎  ','  ')
                print("\n finded Auxiliary verb but can't find any valid sentence 🧐🥴    ")                
            elif stlen > 5 and st  == i:
                print('\n finded '+'"'+st+'"'+' as auxiliary  verb😎😎  ')
                x = state.replace(st,"")                
                print('yes/no Question ')
                print('   ',st,x,'?')
                print('Answer(if Yes):')
                print('    Yes,',state)
                print('Answer(if No):')
                staterepls = state.replace(st,st+"n't ")
                print('    No,',staterepls)
                print('OR')
                staterepls = state.replace(st,st+" not ")
                print('    No,',staterepls,'\n')                
                aux_yes = 'yes'
                continue              
            else:
                NOE += 1
                MNOE = len(s)*len(aux)
                if NOE == MNOE:
                    print('  \nerror😡  \n','     There is no valid sentence🤬  ')
                
          
    if stlen == 0:
        print('\n no sentence 🥱😡  ')               
        
while t :
    print('')
    print("\033[1;2;32;40m Programed by 'Programer_പൂച്ച' ")
    state = input('\033[1;32;2;40m enter the sentence >_ \033[1;0;32;40m'+" ")
    YNQM(state)
    
             
         