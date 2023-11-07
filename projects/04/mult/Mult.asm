// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// i = 1
@i
M=0
// sum = 0
@sum
M=0
@R1
D=M
// Save the value of R1 into variable named n
@n
M=D

(LOOP)
// Check if i is >= n
@i
D=M
@n
D=D-M
@STOP
D;JGE

// Add R0 to sum for the i'th time
@sum
D=M
@R0
D=D+M
@sum
M=D

// Increment i
@i
M=M+1

// Go back to top of loop to check condition
@LOOP
0;JMP

(STOP)
@sum
D=M
@R2
M=D

(END)
@END
0;JMP


