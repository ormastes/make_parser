grammar Makefile;

IFEQ : 'ifeq';
ENDIF : 'endif';
WS : [ \t]+ -> skip; // Skip whitespace

// Parser rules
makefile : statement+ EOF;

identity : ~('\r'|'\n'|':'|'=')+ ;

conditional : IFEQ WS identity '\r'? '\n';
rule : identity ':' identity '\r'? '\n';
assign : identity '=' identity '\r'? '\n';

statement :
    conditional
    | rule
    | assign
    | ENDIF;

// Lexer rules
NL : '\r'? '\n'; // Matches end-of-line characters
