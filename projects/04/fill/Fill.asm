(INFLOOP)
@i
M=0
@8192
D=A
@rows
M=D
@KBD
D=M
@BLACKLOOP
D;JNE
@WHITELOOP
D;JEQ

(BLACKLOOP)
// Check loop condition
@i
D=M
@rows
D=D-M
@INFLOOP
D;JGE

// Black loop logic
@i
D=M
@SCREEN
A=D+A
M=-1

// Increment i
@1
D=A
@i
M=M+D
@BLACKLOOP
0;JMP

(WHITELOOP)
// Check loop condition
@i
D=M
@rows
D=D-M
@INFLOOP
D;JGE

// White loop logic
@i
D=M
@SCREEN
A=D+A
M=0

// Increment i
@1
D=A
@i
M=M+D
@WHITELOOP
0;JMP