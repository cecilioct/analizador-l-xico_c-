import ply.lex as lex
import re
import sys 

tokens = (
#OPERADORES ARITMETICOS Y RELACIONALES     
"SUMA", "MENOS", "MULTIPLICAR", "DIVISION",
"IGUALQUE", "MENORQUE", "MENORIGUALQUE", "MAYORQUE", "MAYORIGUALQUE", "PARENTIZQ", "PARENTDER", "COMA",
"PTCOMA", "PUNTO","IGUALIGUAL","COMILLA","DOPUNTOS","MODULO",

#PALABRAS RESERVADAS
"USING", "CLASS", "STATIC", "VOID", "INT", "DOUBLE", "IF", "WHILE", "THIS", "RETURN", "ELSE", "TRUE", "FALSE",
"IN", "CONST", "FOR", "NEW", "STRING", "CASE", "CHAR","AS",
"BREAK","CONTINUE","DEFAULT","DO", "FINALLY","LONG","NAMESPACE","NULL", "PRIVATE",
"PUBLIC","PROTECTED","REF","STRUCT","SWITCH","MAIN", "LLAVEDER", "LLAVEIZQ", "PARENTDE", "PARENTIZ", 
"CORCHETEIZQU","CORCHETEDERE", "SYSTEM","STRING","BOOL",

#OTHERS
"ID","NUMBER", "COMMENT","DECIMAL"
)

#IGNORAR CARACTER
t_ignore =        '\t'

def t_space(t):
    r"\s+"
    t.lexer.lineno += t.value.count("\n")

def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(chr(27) + "[1;31m" + "\t ERROR: Caracter Illegal" + chr(27) + "[0m")
    print("\t\tLine: " + str(t.lexer.lineno) + "\t=> " + t.value[0])
    t.lexer.skip(1)

#OPERADORES ARITMETICOS Y RELACIONALES 

t_SUMA =          r'\+'
t_MENOS =         r'\-'
t_MULTIPLICAR =   r'\*'
t_DIVISION =      r'/'
t_IGUALQUE =      r'='
t_MENORQUE =      r'<'
t_MENORIGUALQUE = r'<='
t_MAYORQUE =      r'>'
t_MAYORIGUALQUE =  r'>='
t_IGUALIGUAL = r'=='
t_COMILLA = r'"'
t_MODULO = r'%'

#SIMBOLOS
t_CORCHETEIZQU = r'\['
t_CORCHETEDERE = r'\]'
t_PARENTIZ =     r'\('
t_PARENTDE =     r'\)'
t_LLAVEIZQ =   r'\{'
t_LLAVEDER =   r'\}'
t_COMA =          r','
t_PTCOMA =        r';'
t_PUNTO =         r'\.'
t_DOPUNTOS =      r':'

#PALABRAS RESERVADAS

def t_STRING(t):
    r'String'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_USING(t):
    r'using'
    return t

def t_MAIN(t):
    r'main'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_VOID(t):
    r'void'
    return t

def t_INT(t):
    r'int'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_IF(t):
    r'if'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_THIS(t):
    r'this'
    return t

def t_RETURN(t):
    r'return'
    return t
 
def t_ELSE(t):
    r"else"
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_IN(t):
    r'in'
    return t

def t_CONST(t):
    r'const'
    return t

def t_FOR(t):
    r'for'
    return t

def t_NEW(t):
    r'new'
    return t

def t_STRING(t):
    r'string'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_AS(t):
    r'as'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DO(t):
    r'do'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_LONG(t):
    r'long'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_NULL(t):
    r'null'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_SYSTEM(t):
    r'System'
    return t

#OTHERS

def t_ID (t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

#r'-*\d+[.]*\d+'
def t_NUMBER(t):
    r'[0-9]'
    t.value = int(t.value)
    return t

def t_DECIMAL(t):
    #r'd+(?.d{1,3})?'
    r'\d+.\d+'
    t.value = float(t.value)
    return t

def t_COMMENT(t):
    r'[\/{2}\w+\s+]+'
    pass 


lexer = lex.lex()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script = sys.argv[1]

        scriptfile = open(script, "r")
        scriptdata = scriptfile.read()
        lexer.input(scriptdata)

        print(chr(27) + "[0;36m" + "INICIA ANALISIS LEXICO" + chr(27) + "[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(
                "\t"
                + str(i)
                + " - "
                + "Line: "
                + str(tok.lineno)
                + "\t"
                + str(tok.type)
                + "\t-->  "
                + str(tok.value)
            )
            i += 1

        print(chr(27) + "[0;36m" + "TERMINA ANALISIS LEXICO" + chr(27) + "[0m")

    else:
        print(chr(27) + "[0;31m" + "Pase el archivo de scritp Cs como parametro")
        print(
            chr(27)
            + "[0;36m"
            + "\t$ python AnalizadorLexico.py"
            + chr(27)
            + "[1;31m"
            + " <filename>.cs"
            + chr(27)
            + "[0m"
        )
