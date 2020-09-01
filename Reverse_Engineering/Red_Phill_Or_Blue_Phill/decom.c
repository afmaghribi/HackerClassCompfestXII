void __noreturn start()
{
  int v0; // eax
  int v1; // eax
  int v2; // eax
  int v3; // eax
  int v4; // eax
  int v5; // eax
  void *retaddr; // [esp+0h] [ebp+0h]
  signed int v7; // [esp+4h] [ebp+4h]
  signed int i; // [esp+4h] [ebp+4h]
  signed int v9; // [esp+4h] [ebp+4h]
  signed int v10; // [esp+8h] [ebp+8h]
  int j; // [esp+Ch] [ebp+Ch]

  v0 = sys_read(0, input, 0x100u);
  v7 = -1;
  do
    ++v7;
  while ( *(int *)(input[v7]));
  if ( v7 == 29 )
  {
    for ( i = -1; ++i < 29; (char *)&retaddr[i + 20] = j )
    {
      v10 = -1;
      for ( j = 0; ++v10 < 29; j = (v1 + j) % 127 )
      {
        v1 = 29 * v10;
        LOWORD(v1) = byte_804A100[29 * v10 + i] * input[v10];
      }
    }
    v9 = -1;
    while ( ++v9 < 29 )
    {
      if ( byte_804A478[v9] != (BYTE *)&retaddr[v9 + 20])
      {
        v3 = sys_write(1, "Not Horray", 0xEu);
        goto LABEL_16;
      }
    }
    v2 = sys_write(1, "Horray", 0xAu);
  }
  else
  {
    v4 = sys_write(1, "Not The correct Lenght", 0x17u);
  }
LABEL_16:
  v5 = sys_exit(1);
}