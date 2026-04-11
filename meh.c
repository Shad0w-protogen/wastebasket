#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Функция для преобразования числа в восьмеричную строку (аналог cuck(a))
char* to_octal_string(int num) {
    static char buffer[32]; // Буфер для хранения результата (32 символа достаточно для int)
    sprintf(buffer, "%o", num); // Преобразуем число в восьмеричное представление
    return buffer;
}

// Функция проверки наличия чётной цифры до/после 4 (аналог has_even_around_4)
int has_even_around_4(const char* s) {
    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        if (s[i] == '4') {
            // Проверяем предыдущую цифру, если она есть
            if (i > 0) {
                int prev_digit = s[i - 1] - '0'; // Преобразуем символ в цифру
                if (prev_digit % 2 == 0) {
                    return 1; // true
                }
            }
            // Проверяем следующую цифру, если она есть
            if (i < len - 1) {
                int next_digit = s[i + 1] - '0';
                if (next_digit % 2 == 0) {
                    return 1; // true
                }
            }
        }
    }
    return 0; // false
}

int main() {
    int count = 0;

    // Перебираем числа от 10000 до 99999
    for (int i = 10000; i < 100000; i++) {
        // Преобразуем число в восьмеричную строку
        char* octal = to_octal_string(i);

        // Проверяем условие: нет чётных цифр рядом с 4 И первая цифра исходного числа — 2, 4, 6 или 8
        if (!has_even_around_4(octal)) {
            char first_digit = (i / 10000) + '0'; // Получаем первую цифру числа
            if (first_digit == '2' || first_digit == '4' ||
                first_digit == '6' || first_digit == '8') {
                count++;
            }
        }
    }

    printf("%d\n", count);
    return 0;
}
