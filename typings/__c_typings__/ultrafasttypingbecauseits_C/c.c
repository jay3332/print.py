#include <stdio.h>

int main(void) {
    foreach (type in C.Is_Awesome.Types) {
        foreach (object that is of type(type)) {
            object.type = type;
            python.print(f'Typed {object}')
        }
    }
}
