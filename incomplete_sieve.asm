mov r1, n        ; r1 = n
mov r2, 2        ; r2 = starting index (2)
InitializeArray:
    mov [primes + r2], 1 ; Set primes[r2] to true
    inc r2
    cmp r2, r1
    jle InitializeArray

; Sieve Process
mov r2, 2            ; r2 = 2 (starting index)
SieveLoop:
    cmp r2, sqrt_n   ; If r2 > sqrt(n), end loop
    jg EndSieve

    mov r3, [primes + r2]
    cmp r3, 0        ; If primes[r2] is false, skip
    je NextIndex

    ; Mark all multiples of r2 as non-prime
    mov r4, r2       ; r4 = r2 (current prime)
    mul r4, r2       ; r4 = r4 * r2 (r4 = r2^2)
    MarkMultiples:
        cmp r4, n    ; If r4 > n, stop marking
        jg NextIndex

        mov [primes + r4], 0  ; Set primes[r4] to false
        add r4, r2            ; Increment r4 by r2 (next multiple)

        jmp MarkMultiples

    NextIndex:
    inc r2
    jmp SieveLoop
EndSieve:

mov r2, 2            ; r2 = 2 (starting index)
OutputLoop:
    cmp r2, n
    jg EndOutput

    mov r3, [primes + r2]
    cmp r3, 1        ; If primes[r2] is true, it's a prime
    jne NextPrime

    ; Output r2 as a prime number
    ; (Actual output depends on system/requirements)

    NextPrime:
    inc r2
    jmp OutputLoop
EndOutput:

