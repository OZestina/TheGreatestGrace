char	*ft_strcat(char *dest, char *src)
{
	int	idx_d;
	int	idx_s;

	idx_d = 0;
	while (dest[idx_d] != '\0')
		idx_d++;
	idx_s = 0;
	while (src[idx_s] != '\0')
	{
		dest[idx_d + idx_s] = src[idx_s];
		idx_s++;
	}
	dest[idx_d + idx_s] = '\0';
	return (dest);
}
