printn(n, b) {
        extrn putchar;
        auto a;
        /* Wikipedia note: auto declares a variable with automatic
           storage (lifetime is function scope), not "automatic typing"
           as in C++11. */

        if (a = n / b)        /* assignment, not test for equality */
                printn(a, b); /* recursive */
        putchar(n % b + '0');
}

main() {
    printn("b");
}
