function my_function(n) {
    // Тут нужно написать решение
    if (n == 1) {
        return n;
    }
    my_fuction(n - 1);
    return n;
}

my_function(9)