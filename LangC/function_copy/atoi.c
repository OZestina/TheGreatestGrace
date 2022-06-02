int	is_space(char c)
{
	if ((9 <= c && c <= 13) || c == ' ')
		return (1);
	return (0);
}

int	ft_atoi(char *str)
{
	int	idx;
	int	number;
	int	minus;

	idx = 0;
	number = 0;
	minus = 1;
	while (is_space(str[idx]))
		idx++;
	while (str[idx] == '+' || str[idx] == '-')
	{
		if (str[idx] == '-')
			minus *= -1;
		idx++;
	}
	while ('0' <= str[idx] && str[idx] <= '9')
	{
		number = number * 10 + (str[idx] - '0');
		idx++;
	}
	return (number * minus);
}
