; The program gets input from keypad and displays its ascii value on the
; LED bar
.include "m2560def.inc"

.def row = r16 							; current row number
.def col = r17 							; current column number
.def rmask = r18 						; mask for current row during scan
.def cmask = r19 						; mask for current column during scan
.def temp1 = r20
.def temp2 = r21

.equ PORTFDIR = 0xF0 					; PF7-4: output, PF3-0, input
.equ INITCOLMASK = 0xEF 				; scan from the leftmost column,
.equ INITROWMASK = 0x01 				; scan from the top row
.equ ROWMASK =0x0F 						; for obtaining input from Port F
RESET:
	ldi r26,10
	clr first_num
	clr second_num
	ldi temp1, PORTFDIR 				; PF7:4/PF3:0, out/in
	out DDRF, temp1
	ser temp1 							; PORTC is output
	out DDRC, temp1

inital_result:
	ldi result, 'F'

main:
	ldi cmask, INITCOLMASK 				; initial column mask
	clr col 							; initial column

colloop:
	cpi col, 4
	breq inital_result 					; if all keys are scanned, repeat.
	out PORTF, cmask 					; otherwise, scan a column
	ldi temp1, 0xFF 					; slow down the scan operation.

delay:
	dec temp1
	brne delay
	in temp1, PINF 					; read PORTF
	andi temp1, ROWMASK 				; get the keypad output value
	cpi temp1, 0xF 						; check if any row is low
	breq nextcol
										; if yes, find which row is low
	ldi rmask, INITROWMASK 				; initialize for row check
	clr row 							;
	jmp rowloop

rowloop:
	cpi row, 4
	breq nextcol 						; the row scan is over.
	mov temp2, temp1
	and temp2, rmask 					; check un-masked bit
	breq convert 						; if bit is clear, the key is pressed
	inc row 							; else move to the next row
	lsl rmask
	jmp rowloop

nextcol: 								; if row scan is over
	lsl cmask
	inc col 							; increase column value
	jmp colloop 						; go to the next column

convert:
	cpi col, 3 							; If the pressed key is in col. 3
	breq letters 						; we have a letter
										; If the key is not in col. 3 and
	cpi row, 3 							; if the key is in row3,
	breq symbols 						; we have a symbol or 0
	mov temp1, row 						; Otherwise we have a number in 1-9
	lsl temp1
	add temp1, row 						;
	add temp1, col 						; temp1 = row*3 + col
	subi temp1, -'1'					; Add the value of character ‘1’
	jmp convert_end

letters:
	ldi temp1, 'A'
	add temp1, row 						; Get the ASCII value for the key
	jmp overflow

symbols:
	cpi col, 0 							; Check if we have a star
	ldi temp1,'*'
	breq read_second_number
	cpi col, 1 							; or if we have zero
	ldi temp1,0
	breq convert_end 					; if not we have hash
	ldi temp1,'#'
	jmp caculate


convert_end:
	cp result, temp1					; if the input does not change, do nothing and return to first step
	breq main
	mov result, temp1 					; use result as a flag, judge if input changed
	mul second_num, r26
	clr r27
	cp r1,r27
	brne overflow
	mov second_num, r0
										; out PORTC, second
	add second_num, temp1 				; new first number is old one *10 + temp1
	brcs overflow						; in case of 256-259
	out PORTC, second_num
	jmp main



							; Restart main loop

