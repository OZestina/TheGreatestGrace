unsigned int	len_count(char *addr)
{
	unsigned int	count;

	count = 0;
	while (addr[count] != '\0')
		count++;
	return (count);
}

unsigned int	ft_strlcat(char *dest, char *src, unsigned int size)
{
	unsigned int	idx;
	unsigned int	idx_s;

	idx = len_count(dest);
	if (idx >= size)
	{
		idx_s = len_count(src);
		return (idx_s + size);
	}
	size -= idx;
	idx_s = 0;
	while (src[idx_s] != '\0' && idx_s + 1 < size)
	{
		dest[idx + idx_s] = src[idx_s];
		idx_s++;
	}
	dest[idx + idx_s] = '\0';
	while (src[idx_s] != '\0')
		idx_s++;
	return (idx + idx_s);
}
