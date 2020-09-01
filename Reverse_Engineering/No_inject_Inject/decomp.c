#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int  main(int argc, const char **argv, const char **envp)
{
  int i; 
  int v5;
  int v6;

  if ( strlen(argv[1]) != 42 ){
    // lose();
    printf("Harus 42\n");
    exit(0);
  }
  for ( i = 0; i < strlen(argv[1]); i += 2 )
  {
    v5 = argv[1][i];
    v6 = argv[1][i + 1];
    // if ( v5 + v6 != answer[i] || v6 * v5 != answer[i + 1] )
      // lose();
    printf("1. \n", v5);
    printf("2. \n", v6);
    printf("Kali. %d\n", v5 * v6);
    printf("Tambah %d\n", v5 + v6 );
  }
  puts("Mantap bang");
  return 0;
}


// [0x14AD00000092,0x18100000009D,0x12DE0000008B,0x1B3C000000A7,0x99200000063,0x2F16000000DD,0x2B66000000D3,0x2B32000000D3,0x27B5000000CA,0x29AE000000CF,0x28D2000000CD,0x2931000000CE,0x2D1E000000D7,0x29D2000000CF,0x2CDC000000D7,0x26F7000000C8,0x2D8C000000D8,0x270F000000C8,0x2B0C000000D3,0x2ED4000000DB,0x34BC000000E9]