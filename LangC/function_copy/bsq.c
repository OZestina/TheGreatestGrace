#include	<stdlib.h>

//make int[][] array of width * height
int	**set_square(int width, int height)
{
	int	idx;
	int	**square_map;

	square_map = (int **)malloc(sizeof(int *) * height);
	if (square_map == 0)
		return (0);
	square_map[0] = (int *)malloc(sizeof(int) * height * width);
	if (square_map[0] == 0)
	{
		free(square_map);
		return (0);
	}
	idx = 1;
	while (idx < height)
	{
		square_map[idx] = square_map[idx - 1] + width;
		idx++;
	}
	return (square_map);
}

//pre-set for width=0 & height=0
void	square_preset(int **square, int **map, int width, int height)
{
	int	idx_h;
	int	idx_w;

	idx_w = 0;
	while (idx_w < width)
	{
		if (map[0][idx_w] == 1)
			square[0][idx_w] = 0;
		else
			square[0][idx_w] = 1;
		idx_w++;
	}
	idx_h = 0;
	while (idx_h < height)
	{
		if (map[idx_h][0] == 1)
			square[idx_h][0] = 0;
		else
			square[idx_h][0] = 1;
		idx_h++;
	}
}

//set for width>0 & height>0
void	square_set(int **square, int **map, int width, int height)
{
	int	idx_h;
	int	idx_w;
	int	min;

	idx_h = 1;
	while (idx_h < height)
	{
		idx_w = 1;
		while (idx_w < width)
		{
			if (map[idx_h][idx_w] == 1)
				square[idx_h][idx_w] = 0;
			else
			{
				min = square[idx_h - 1][idx_w - 1];
				if (square[idx_h - 1][idx_w] < min)
					min = square[idx_h - 1][idx_w];
				if (square[idx_h][idx_w - 1] < min)
					min = square[idx_h][idx_w - 1];
				square[idx_h][idx_w] = min + 1;
			}
			idx_w++;
		}
		idx_h++;
	}
}

//return result[size, idx_h, idx_w, height, width]
int	*biggest_square(int **square, int width, int height, int *biggest)
{
	int	idx_h;
	int	idx_w;

	biggest[0] = square[0][0];
	biggest[1] = 0;
	biggest[2] = 0;
	biggest[3] = height;
	biggest[4] = width;
	idx_h = -1;
	while (++idx_h < height)
	{
		idx_w = -1;
		while (++idx_w < width)
		{
			if (biggest[0] < square[idx_h][idx_w])
			{
				biggest[0] = square[idx_h][idx_w];
				biggest[1] = idx_h;
				biggest[2] = idx_w;
			}
		}
	}
	return (biggest);
}

int	*square_num(int **map, int width, int height)
{
	int	**square_count;
	int	*biggest;

	square_count = set_square(width, height);
	if (square_count == 0)
		return (0);
	square_preset(square_count, map, width, height);
	square_set(square_count, map, width, height);
	biggest = (int *)malloc(sizeof(int) * 5);
	if (biggest == 0)
		return (0);
	biggest = biggest_square(square_count, width, height, biggest);
	return (biggest);
}
