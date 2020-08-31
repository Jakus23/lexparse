def t_error(t):
    "Error handling rule"
    print("Illegal character '%s' in line %s" % (t.value[0], t.lineno))
    t.lexer.skip(1)
tokens =('ATTRIBUTE','COMMENT','ELLIPSIS','ASSIGN','NEWLINE','TAB','EXAMPLE')
def t_TAB(t):
    r'\t '
    return t
def t_NEWLINE(t):
    #Define a rule so we can track line numbers
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t
def t_ATTRIBUTE(t):
    r'[\@\:\!/\\a-z0-9 ]+'
    t.value = t.value.strip()
    return t
def t_COMMENT(t):
    r'\#[a-zA-Z0-9_ ]+'
    t.value = str(t.value).strip()
    return t
def t_ASSIGN(t):
    r'=[/\\a-zA-Z0-9\,\-\_\@\.\/\#\&\+\- ]+'
    return t
t_EXAMPLE=r'/[/\\a-z\,\-\_A-Z0-9 ]+'
    
t_ELLIPSIS = r'\.\.\.'
import ply.lex as lex
lexer = lex.lex()




    

# Parsing rules

def p_attributes(t):
    '''code : attribute
            | context
            | attribute code
            | context code'''
def p_attribute(t):
    'attribute : ATTRIBUTE'
    state['description']=list(t)
    state['token']='attribute'
    if state['indent'] >= len(list_of_types)-1:
        list_of_types.append(list(t)[1])
    else:
        list_of_types[state['indent']+1]=list(t)[1]
    if list(t)[1][0] in (':'):
        records.append([list_of_types[state['indent']],'has-a',list(t)[1][1:]])
    if list(t)[1][0] in ('@'):
        records.append([list_of_types[state['indent']],'is dependent on',list(t)[1][1:]])
    if list(t)[1][0] not in (':','@'):
        records.append([list_of_types[state['indent']].replace(':','').replace('@',''),'can-be-a',list(t)[1]])
    #print(state)
def p_assign(t):
    'context : ASSIGN'
    state['description']=list(t)
    state['token']='assign'
    records.append([list_of_types[state['indent']+1],'has value',list(t)[1][1:].split(",")])
    #print(state)
def p_comment(t):
    'context : COMMENT'
    state['description']=list(t)
    state['token']='comment'
    #print(state)
def p_newline(t):
    'context : NEWLINE'
    state['description']=list(t)
    state['token']='newline'
    state['indent']=0
    state['line']+=1
def p_ellipsis(t):
    'context : ELLIPSIS'
    state['token']='ellipsis'
    state['description']=list(t)
def p_tab(t):
    'context : TAB'
    state['description']=list(t)
    state['token']='tab'
    state['indent']+=1
    #print(state)
def p_example(t):
    'context : EXAMPLE'
    state['description']=list(t)
    state['token']='example'
    state['indent']+=1
    #print(state)
def p_error(t):
    print("Syntax error at '%s'" % t.value)
    input()
import ply.yacc as yacc
parser = yacc.yacc()

def parse_file(slug):
    parser.parse(str(open(slug, 'r').read()).replace('    ','\t'))
    list_of_types=[ntpath.basename(slug)]

#initiate   
import ntpath
list_of_types=[]
records=[]
state={'indent':0,'line':1,'description':None,'token':None}

if __name__=='__main__':
    parse_file("https://repl.it/@Jakusvan/lexparse#strategy.txt")