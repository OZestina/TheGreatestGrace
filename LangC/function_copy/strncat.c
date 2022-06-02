char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	unsigned int	idx;
	unsigned int	idx_s;

	idx = 0;
	while (dest[idx] != '\0')
		idx++;
	idx_s = 0;
	while (idx_s < nb && src[idx_s] != '\0')
	{
		dest[idx + idx_s] = src[idx_s];
		idx_s++;
	}
	dest[idx + idx_s] = '\0';
	return (dest);
}
