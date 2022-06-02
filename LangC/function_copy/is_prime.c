int	ft_is_prime(int nb)
{
	int	n;

	if (nb < 2)
		return (0);
	if (nb == 2)
		return (1);
	if (nb % 2 == 0)
		return (0);
	n = 3;
	while (n <= nb / n)
	{
		if (nb % n == 0)
			return (0);
		n += 2;
	}
	return (1);
}
