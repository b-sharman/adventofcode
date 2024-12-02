#include <cstring>
#include <iostream>
#include <openssl/md5.h>

int main()
{
    const char input[] = "abcdef";
    unsigned char output[MD5_DIGEST_LENGTH];// {};

    MD5(
        reinterpret_cast<const unsigned char *>(input),
        strlen(input),
        output
        );

    // segfaults for whatever reason
    std::cout << *output << std::endl;

    //unsigned char *test = const_cast<unsigned char *>("Hello, world!\n");
    //std::cout << *test << std::endl;

    return 0;
}
/*

    // the number to add to the input
    //int num = 1;
    int num = 609000;
    while (!valid(cmd_to_try(input, num)))
    {
        num++;
        if (num % 1000 == 0)
        {
            std::cout << "num is " << num << std::endl;
        }
        if (num < 0)
        {
            std::cout << "fail" << std::endl;
            break;
        }
    }

    std::cout << num << std::endl;
    return 0;
}
*/
