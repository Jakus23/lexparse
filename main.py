def t_error(t):
    "Error handling rule"
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
tokens =('TYPE','DEPENDENT','PROPERTY','COMMENT','ELLIPSIS','ASSIGN','NEWLINE','TAB')
def t_TAB(t):
    r'\t '
    return t
def t_NEWLINE(t):
    #Define a rule so we can track line numbers
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t
def t_TYPE(t):
    r'[/\\a-z0-9 ]+'
    t.value = t.value.strip()
    t.value = t.value.replace('/','')
    t.value = t.value.replace('\\','')
    t.value = t.value.replace(' ','_')
    return t
def t_DEPENDENT(t):
    r'@[a-z0-9 ]+'
    t.value = t.value.replace('@','')
    t.value = str(t.value).strip()
    t.value = str(t.value).replace(' ','_')
    return t
def t_PROPERTY(t):
    r':|!|has-|[a-z0-9 ]+'
    t.value = str(t.value)[1:]
    t.value = str(t.value).strip()
    t.value = str(t.value).replace(' ','_')
    return t
def t_COMMENT(t):
    r'\#[a-zA-Z0-9_ ]+'
    t.value = str(t.value)[1:]
    t.value = str(t.value).strip()
    return t
def t_ASSIGN(t):
    r'=.*'
    t.value = str(t.value)[1:]
    t.value = str(t.value).strip()
    return t
t_ELLIPSIS = r'\.\.\.'
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

state={'current_type':[],'level':0}
def p_attributes(t):
    '''code : attribute
            | context
            | attribute code
            | context code'''
def p_attribute_type_assign_newline(t):
    'attribute : TYPE ASSIGN NEWLINE'
    if len(state['current_type'])<state['level']:
        for i in range(state['level']-len(state['current_type'])):
            state['current_type'].append(t[1])
    state['current_type'][state['level']-1]=t[1]
    print('TYPE ASSIGN NEWLINE:',list(t))
    state['level']=0
def p_attribute_type(t):
    'attribute : TYPE'
    ...#commit previous type
    if len(state['current_type'])<state['level']:
        for i in range(state['level']-len(state['current_type'])):
            state['current_type'].append(t[1])
    state['current_type'][state['level']-1]=t[1]
    print('TYPE:',list(t))
def p_attribute_property(t):
    'attribute : PROPERTY'
    print('PROPERTY:',list(t))
def p_attribute_dependent(t):
    'attribute : DEPENDENT'
    print('DEPENDENT:',list(t))
def p_attribute_assignment(t):
    'context : ASSIGN NEWLINE'
    state['level']=0
    print('ASSIGN:',list(t))
def p_attribute_comment(t):
    'context : COMMENT'
    print('COMMENT:',list(t))
def p_attribute_newline(t):
    'context : NEWLINE'
    print('NEWLINE:',list(t))
    state['level']=0
def p_attribute_ELLIPSIS(t):
    'context : ELLIPSIS'
    print('ELLIPSIS:',list(t))    
def p_attribute_tab(t):
    'context : TAB'
    state['level']+=1
def p_error(t):
    print("Syntax error at '%s'" % t.value)
    input()

import ply.yacc as yacc
parser = yacc.yacc()
#parser.parse("type=2\n\t\t:property\n")
def convert_slug_to_string(slug):
    return str(open(slug, 'r').read()).replace('    ','\t')
parser.parse(convert_slug_to_string("https://repl.it/@Jakusvan/lexparse#type"))

"""
if __name__=='__main__':
    def convert_slug_to_string(slug):
        return str(open(slug, 'r').read()).replace('    ','\t')
    lexer.input(convert_slug_to_string("C:\\Users\\Christine Van Rooyen\\Documents\\Jakus\\Code\\business_model"))
    line_start=0
    for token in lexer:
        if token.type=='NEWLINE': line_start = token.lexpos + 1
        print({'type':token.type,'value':token.value,'line': token.lineno,'position':token.lexpos,'column':((token.lexpos - line_start) + 1)})
"""