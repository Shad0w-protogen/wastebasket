#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Функция для преобразования числа в двоичную строку
char* to_binary_string(int n) {
    static char binary[32]; // Буфер для хранения двоичного представления (32 бита достаточно для int)
    int index = 31;
    binary[index] = '\0'; // Завершаем строку

    if (n == 0) {
        binary[--index] = '0';
    } else {
        while (n > 0) {
            binary[--index] = (n % 2) ? '1' : '0';
            n /= 2;
        }
    }
    return &binary[index];
}

// Функция transform_number из Python
int transform_number(int n) {
    char* binary = to_binary_string(n);
    int len = strlen(binary);
    char transformed_binary[64] = ""; // Буфер для преобразованной двоичной строки

    if (n % 2 == 0) { // Чётное число
        char last_two[3] = "00"; // По умолчанию — два нуля

        if (len >= 2) {
            // Берём последние два символа
            last_two[0] = binary[len - 2];
            last_two[1] = binary[len - 1];
        } else if (len == 1) {
            // Если один символ, дополняем нулём слева
            last_two[0] = '0';
            last_two[1] = binary[0];
        } // Если len == 0, оставляем "00"

        // Конкатенируем: binary + last_two
        strcpy(transformed_binary, binary);
        strcat(transformed_binary, last_two);
    } else { // Нечётное число
        // Формируем строку: '1' + binary + '1'
        transformed_binary[0] = '1';
        strcpy(&transformed_binary[1], binary);
        transformed_binary[strlen(transformed_binary) + 1] = '\0';
        transformed_binary[strlen(transformed_binary)] = '1';
    }

    // Преобразуем двоичную строку обратно в число
    int result = 0;
    int power = 1;
    int transformed_len = strlen(transformed_binary);

    for (int i = transformed_len - 1; i >= 0; i--) {
        if (transformed_binary[i] == '1') {
            result += power;
        }
        power *= 2;
    }

    return result;
}

int main() {
    for (int i = 0; i < 70; i++) {
        int transformed = transform_number(i);
        if (transformed > 70) {
            printf("%d\n", i);
            break;
        }
    }
    return 0;
}
