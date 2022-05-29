# 문자열(str) 내에 문자열(to_find)이 있는지 확인하는 함수

char  *strstr(char *str, char *to_find)
{
  unsigned int  idx;
  unsigned int  idx_f;
  
  if (*to_find == '\0')
    return (str);
  idx = 0;
  while (str[idx] != '\0')
  {
    idx_f = 0;
    while (str[idx + idx_f] != '\0' && to_find[idx_f] != '\0')
    {
      if (str[idx + idx_f] == to_find[idx_f])
        idx_f++;
      else
        break ;
    }
    if (to_find[idx_f] == '\0')
      return (&str[idx]);
    idx++;
  }
  return (0);
}
